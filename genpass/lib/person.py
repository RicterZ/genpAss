# coding=utf-8
from __future__ import print_function
import time
from itertools import product, permutations
from pinyin import PinYin
from genpass.rules import built_in
from genpass.config import PINYIN, DICT


__all__ = ['Person']


class Person(object):
    name = []
    username = []
    email = []
    qq_number = []
    mobile_phone = []
    birthday = None
    company = ''

    def __init__(self, dict_=None):
        if dict_ and isinstance(dict_, (dict, )):
            self.name = dict_.get('name', [])
            self.username = dict_.get('username', [])
            self.email = dict_.get('email', [])
            self.qq_number = dict_.get('qq_number', [])
            self.mobile_phone = dict_.get('mobile_phone', [])
            self.birthday = dict_.get('birthday', None)
            self.company = dict_.get('company', '')

            # TODO
            # self.passwords = dict_.get('passwords', [])

    def _generator_map(self, data, formatter_list):
        '''generate passwords fragment by formatting function

        :param data: data will be formatted
        :param formatter_list: formatting function
        :return: strings list
        '''
        if not data:
            return []

        result = set()
        for format_func in formatter_list:
            if not callable(format_func):
                raise TypeError('formatter is not callable')
            if not isinstance(data, (list, set, tuple)):
                data = [data]
            result.update(map(format_func, data))
        return result

    def _generate_email(self):
        '''generate passwords fragment from email

        :return: strings list
        '''
        id_string = map(lambda i: i.split('@')[0], self.email)
        return self._generator_map(id_string, built_in.general_formats)

    def _generate_name(self):
        '''generate passwords fragment from username/real name/email id string

        :return: strings list
        '''
        # real name
        result = set()
        pinyin = PinYin(PINYIN)
        pinyin.load_word()
        name_pinyin_list = map(pinyin.hanzi2pinyin, self.name)
        result.update(self._generator_map(name_pinyin_list, built_in.name_formats))

        # username
        result.update(self._generator_map(self.username, built_in.general_formats))

        # email id_string
        result.update(self._generate_email())
        return result

    def _generate_birthday(self):
        '''generate passwords fragment from birthday

        :return: strings list
        '''
        return self._generator_map(self.birthday, built_in.date_formats)

    def _generate_company(self):
        '''generate passwords fragment from company

        :return: string list
        '''
        general = self._generator_map(self.company, built_in.general_formats)
        return self._generator_map(general, built_in.company_formats)

    def _generate_qq(self):
        '''generate passwords fragment from qq number

        :return: string list
        '''
        return self._generator_map(map(str, self.qq_number), built_in.qq_formats)

    def _generate_attached_info(self):
        '''generate passwords fragment from user attached information

        :return: string list
        '''
        result = set()
        result.update(map(str, self.mobile_phone))
        result.update(self._generate_birthday())
        result.update(self._generate_qq())
        result.update(self._generate_company())
        return result

    def generate_password(self):
        '''generate passwords

        :return: list
        '''
        combination_list = filter(lambda i: i, [
            self._generate_name(),
            self._generate_attached_info(),
        ])
        passwords = set()
        for i in range(len(combination_list)):
            for data in permutations(combination_list, i + 1):
                for password in product(*data):
                    passwords.add(''.join(password))
        return passwords

    def generate_password_with_dict(self):
        '''generate passwords with wake passwords dict

        :return: string list
        '''
        person_passwords = self.generate_password()
        with open(DICT) as f:
            dict_password = f.read().splitlines()
        passwords = set()
        for password_list in permutations([person_passwords, dict_password], 2):
            for password in product(*password_list):
                passwords.add(''.join(password))

        person_passwords.update(passwords)
        return person_passwords

    def __str__(self):
        return '<Person object>'
