# coding=utf-8
from __future__ import print_function
import re
from itertools import product
from genpass import generator
from genpass.rules import combinations, built_in
from genpass.lib.constants import SEQUENCES


__all__ = ['Person', 'BUILT_IN_FIELD_MAP']

BUILT_IN_FIELD_MAP = (
    ('qq', None),
    ('birthday', built_in.date_formats),
    ('company', built_in.company_formats, generator.generate_name),
    ('name', built_in.name_formats, generator.generate_name),
    ('username', built_in.general_formats),
    (('email', 'username'), built_in.general_formats, generator.generate_id_string),
)


class Person(object):
    source_dict = {}

    def __init__(self, information=None, field_map=()):
        self.information = {} if information is None else information
        self.field_map = field_map if field_map else BUILT_IN_FIELD_MAP

    def generate_source_dict(self):
        '''generate source dictionary `source_dict`.
        `source_dict` is a dictionary which the value contains all
        the situation of provided.
        The map of generate `source_dict` named `field_map`.
        `field_map` is tuple.

        ```
        field_map = (
            ('test', None),
            (('test1', 'test'), built_in.generate_formats),
            ('test2', built_in.generate_formats, generate.custom_function),
        )
        ```
        The first element of tuple is the field name, and if the first element
        is tuple, then the first element of the tuple is the field name from
        user information, the second element is a alias name in the `source_dict`.

        The second element of tuple is the rules for formatting and transferring
        the data which user provided, which is a sequence of lambda.

        The third element of tuple is the custom formatting function. The function
        has 2 parameters. First of the parameters is the data of user information,
        and the type is a list. The second of the parameters is the rule. The function
        returned a set of password fragment.

        A sample of custom formatting function is:

        ```
        def custom_generator(data, rule):
            return set(data)
        ```

        :return: None
        '''
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

            data = self.information.get(field, set())
            if not isinstance(data, SEQUENCES):
                data = [data]
            if not rule and not method:
                returned = data
            elif rule and not method:
                returned = generator.generator_map(data, rule)
            elif method:
                if not callable(method):
                    raise TypeError('Process function is not callable')
                returned = method(data, rule)
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
        '''A generator yield passwords by combining the password fragment.

        `dependence` is a list of field. The function will combine the values of
        each key in the `source_dict`, while the key provided by `dependence`.

        :param dependence:
        :return:
        '''
        for res in (zip(dependence.keys(), i) for i in product(*dependence.itervalues())):
            yield dict(res)

    def generate_password(self):
        '''A generator yield passwords

        :return:
        '''
        self.generate_source_dict()
        match_needed_keys = re.compile('\{(%s)\}' % '|'.join(self.source_dict.keys()))
        match_keys = re.compile('\{([a-zA-Z0-9_]+?)\}')
        for rule in combinations.rules:
            dependent_keys = match_needed_keys.findall(rule)
            all_keys = match_keys.findall(rule)
            if all(map(lambda x: x in dependent_keys, all_keys)) and dependent_keys:
                dependence = {i: self.source_dict[i] for i in dependent_keys}
                for i in self.combined_zip(dependence):
                    yield rule.format(**i)

    def generate_password_with_dict(self):
        pass

    def __str__(self):
        return '<Person object>'
