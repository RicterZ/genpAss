# coding=utf-8
from __future__ import print_function
import re
from itertools import product
from rules import built_in, combinations


__all__ = ['Person']


class Person(object):
    source_dict = {}

    def __init__(self, information=None, field_map=()):
        self.information = {} if information is None else information
        self.field_map = field_map

    @classmethod
    def generator_map(cls, data, formatter_list):
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

    def generate_source_dict(self):
        source_dict = {}
        for row in self.field_map:
            if len(row) == 3:
                field, rule, method = row
            elif len(row) == 2:
                field, rule = row
                method = None
            else:
                raise ValueError('Invalid map')

            if isinstance(field, tuple):
                field, alias = field
            else:
                alias = field

            if not rule and not method:
                returned = self.information.get(field, [])
            elif rule and not method:
                returned = self.generator_map(self.information.get(field, []), rule)
            elif method:
                if not callable(method):
                    raise TypeError('Process function is not callable')

                returned = method(self.information.get(field, []), rule)
                if not isinstance(returned, set):
                    raise TypeError('UDF returned value should be a set.')
            else:
                returned = []

            if alias in source_dict:
                source_dict[alias].update(returned)
            else:
                source_dict[alias] = returned

        for key, value in source_dict.iteritems():
            if value:
                self.source_dict[key] = value

    def combined_zip(self, dependence):
        for res in (zip(dependence.keys(), i) for i in product(*dependence.itervalues())):
            yield dict(res)

    def generate_password(self):
        '''generate passwords

        :return: list
        '''
        self.generate_source_dict()
        match_keys = re.compile('\{(%s)\}' % '|'.join(self.information.keys()))
        for rule in combinations.rules:
            dependent_keys = filter(lambda x: x if x in self.information.keys() else False, match_keys.findall(rule))
            if all(map(lambda x: x in self.source_dict.keys(), dependent_keys)):
                dependence = {i: self.source_dict[i] for i in dependent_keys}
                for i in self.combined_zip(dependence):
                    yield rule.format(**i)

    def generate_password_with_dict(self):
        '''generate passwords with wake passwords dict

        :return: string list
        '''
        pass

    def __str__(self):
        return '<Person object>'
