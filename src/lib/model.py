# coding=utf-8
from __future__ import print_function
import time
from itertools import product, permutations
from lib.pinyin import PinYin
from config import PINYIN


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

    def _generate_name(self):
        if not self.name:
            return []
        result = []

        # true name
        formats = [
            lambda x: ''.join(x),
            lambda x: ' '.join(x).title().replace(' ', ''),
            lambda x: ''.join(map(lambda i: i[0], x)),
            lambda x: ''.join(map(lambda i: i[0], x)).title(),
            lambda x: ''.join(map(lambda i: i[0], x)).upper(),
            lambda x: '%s%s' % (x[0].title(), ''.join(map(lambda i: i[0], x[1:]))),
            lambda x: '%s%s' % (x[0], ''.join(map(lambda i: i[0], x[1:]))),
            lambda x: '%s%s' % (x[0], ''.join(map(lambda i: i[0].upper(), x[1:]))),
            lambda x: ('%s%s' % (x[0], ''.join(map(lambda i: i[0], x[1:])))).upper(),
        ]
        pinyin = PinYin(PINYIN)
        pinyin.load_word()
        name_pinyin_list = map(pinyin.hanzi2pinyin, self.name)
        for format_ in formats:
            for name_pinyin in name_pinyin_list:
                result.append(format_(name_pinyin))

        # username
        formats = [
            lambda x: x.title(),
            lambda x: x.upper(),
            lambda x: x,
        ]
        for format_ in formats:
            result.extend(map(format_, self.username))
        result.extend(self._generate_email())

        return list(set(result))

    def _generate_email(self):
        if not self.email:
            return []
        result = []
        id_string = map(lambda i: i.split('@')[0], self.email)
        formats = [
            lambda x: x.title(),
            lambda x: x.upper(),
            lambda x: x,
        ]
        for format_ in formats:
            result.extend(map(format_, id_string))

        return list(set(result))

    def _generate_birthday(self):
        if not self.birthday:
            return []
        result = []
        formats = [
            '%Y',
            '%y',
            '%Y%m%d',
            '%y%m%d',
            '%-m%-d',
            '%y%-m%-d',
            '%Y%-m%-d',
        ]
        for format_ in formats:
            result.append(time.strftime(format_, self.birthday))
        return list(set(result))

    def generate_password(self):
        combination_list = filter(lambda i: i, [
            self._generate_name(),
            self._generate_birthday(),
        ])
        for i in range(len(combination_list)):
            for data in permutations(combination_list, i + 1):
                for password in product(*data):
                    print(''.join(password))

    def __unicode__(self):
        return '<Person: %s>' % str(self.name)
