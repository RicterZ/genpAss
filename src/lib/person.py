# coding=utf-8
from __future__ import print_function
import time
from itertools import product, permutations
from pinyin import PinYin
from ..rules import build_in
from ..config import PINYIN, DICT


class Person(object):
    name = []
    username = []
    email = []
    qq_number = []
    birthday = None

    def __init__(self, dict_=None):
        if dict_ and isinstance(dict_, (dict, )):
            self.name = dict_.get('name', [])
            self.username = dict_.get('username', [])
            self.email = dict_.get('email', [])
            self.qq_number = dict_.get('qq_number', [])
            self.birthday = dict_.get('birthday', None)

    @property
    def is_null(self):
        return not any([self.name, self.username, self.email,
                        self.qq_number, self.birthday])

    def _format(self, data, format_list):
        result = []
        for format_ in format_list:
            result.extend(map(format_, data))
        return list(set(result))

    def _generate_name(self):
        if not self.name and not self.email:
            return []
        result = []

        # true name
        pinyin = PinYin(PINYIN)
        pinyin.load_word()
        name_pinyin_list = map(pinyin.hanzi2pinyin, self.name)
        result.extend(self._format(name_pinyin_list, build_in.name_formats))
        result.extend(self._format(self.username, build_in.general_formats))
        result.extend(self._generate_email())
        return list(set(result))

    def _generate_email(self):
        if not self.email:
            return []
        id_string = map(lambda i: i.split('@')[0], self.email)
        return self._format(id_string, build_in.general_formats)

    def _generate_birthday(self):
        if not self.birthday:
            return []
        result = []
        for format_ in build_in.date_formats:
            result.append(time.strftime(format_, self.birthday))
        return list(set(result))

    def generate_password(self):
        combination_list = filter(lambda i: i, [
            self._generate_name(),
            self._generate_birthday(),
        ])
        passwords = []
        for i in range(len(combination_list)):
            for data in permutations(combination_list, i + 1):
                for password in product(*data):
                    passwords.append(''.join(password))
        return list(set(passwords))

    def generate_password_with_dict(self):
        person_passwords = self.generate_password()
        with open(DICT) as f:
            dict_password = f.read().splitlines()
        passwords = []
        for password_list in permutations([person_passwords, dict_password], 2):
            for password in product(*password_list):
                passwords.append(''.join(password))
        person_passwords.extend(list(set(passwords)))
        return person_passwords

    def __unicode__(self):
        return '<Person: %s>' % str(self.name)
