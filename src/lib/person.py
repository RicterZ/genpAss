# coding=utf-8
from __future__ import print_function
import time
import sys
from itertools import product, permutations
from pinyin import PinYin
from ..rules import built_in
from ..config import PINYIN, DICT


__all__ = ['Person']


class Person(object):
    def __init__(self, dict_=None):
        if dict_ and isinstance(dict_, (dict, )):
            self.name = dict_.get('name', [])
            self.username = dict_.get('username', [])
            self.email = dict_.get('email', [])
            self.qq_number = dict_.get('qq_number', [])
            self.mobile_phone = dict_.get('mobile_phone', [])
            self.birthday = dict_.get('birthday', None)

            # TODO
            # self.passwords = dict_.get('passwords', [])

    def _generator(self, data, formatter_list):
        '''generate passwords fragment by formatting function

        :param data: data will be formatted
        :param format_list: formatting function
        :return: strings list
        '''
        result = []
        for format_func in formatter_list:
            if not callable(format_func):
                raise TypeError('formatter is not callable')
            result.extend(map(format_func, data))
        return result

    def _generate_email(self):
        '''generate passwords fragment from email

        :return: strings list
        '''
        if not self.email:
            return []
        id_string = map(lambda i: i.split('@')[0], self.email)
        return self._generator(id_string, built_in.general_formats)

    def _generate_name(self):
        '''generate passwords fragment from username/real name/email id string

        :return: strings list
        '''
        result = []
        if not any([self.username, self.email, self.name]):
            return result

        # real name
        pinyin = PinYin(PINYIN)
        pinyin.load_word()
        name_pinyin_list = map(pinyin.hanzi2pinyin, self.name)
        result.extend(self._generator(name_pinyin_list, built_in.name_formats))

        # username
        result.extend(self._generator(self.username, built_in.general_formats))

        # email id string
        result.extend(self._generate_email())
        return list(set(result))

    def _generate_birthday(self):
        '''generate passwords fragment from birthday

        :return: strings list
        '''
        result = []
        if not self.birthday:
            return result
        for format_ in built_in.date_formats:
            result.append(time.strftime(format_, self.birthday))
        return result

    def _generate_attached_info(self):
        '''generate passwords from user attached information

        :return: string list
        '''
        result = []
        result.extend(self.mobile_phone)
        result.extend(self._generate_birthday())
        result.extend(self.qq_number)
        return list(set(result))

    def generate_password(self):
        '''generate passwords

        :return:
        '''
        combination_list = filter(lambda i: i, [
            self._generate_name(),
            self._generate_attached_info(),
        ])
        passwords = []
        for i in range(len(combination_list)):
            for data in permutations(combination_list, i + 1):
                for password in product(*data):
                    passwords.append(''.join(password))
        return list(set(passwords))

    def generate_password_with_dict(self):
        '''generate passwords with wake passwords dict

        :return: string list
        '''
        person_passwords = self.generate_password()
        with open(DICT) as f:
            dict_password = f.read().splitlines()

        passwords = []
        for password_list in permutations([person_passwords, dict_password], 2):
            for password in product(*password_list):
                passwords.append(''.join(password))

        person_passwords.extend(list(set(passwords)))
        return person_passwords

    def __str__(self):
        return '<Person object>'
