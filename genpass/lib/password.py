# coding=utf-8
from __future__ import print_function
from itertools import combinations
from genpass import generator
from genpass.lib import formats
from genpass.lib.constants import SEQUENCES


__all__ = ['Password', 'BUILT_IN_FIELD_MAP']


class PasswordStructure(object):
    '''from: http://drops.wooyun.org/tips/10641
    Password structure: Prefix + Connector +  Keyword + Connector + Suffix
    '''
    _basic_values = tuple()

    def __init__(self):
        self._values = []

    @property
    def values(self):
        self._values.extend(self._basic_values)
        return self._values

    def append(self, v):
        self._values.append(v)

    def extend(self, iterable):
        self._values.extend(iterable)
        self._values = list(set(self._values))

    def __iter__(self):
        return iter(self.values)

    def __str__(self):
        return str(self.values)


class Prefix(PasswordStructure):
    pass


class Suffix(PasswordStructure):
    _basic_values = ('', '123', '0123', '2008', '2010', '2012', '!@#',
                     '..', '.', '!', '?', '~', '-=', '*', '=', )


class Keyword(PasswordStructure):
    pass


class Connector(PasswordStructure):
    _basic_values = ('', '@', '#', ',', '.', '_', '-', '&', '+', '~', '/', ';')
    # _basic_values = ('', )


# PasswordStructure Structure

# prefix: name, username, birthday, company
# suffix: name, username, birthday, company
# keywords: name, username, qq, company

BUILT_IN_FIELD_MAP = (
    ('qq', None, None, (Keyword, )),
    ('birthday', formats.date_formats, None, (Suffix, )),
    ('company', formats.company_formats, generator.generate_name, (Keyword, Suffix, )),
    ('name', formats.name_formats, generator.generate_name, (Keyword, )),
    ('username', formats.general_formats, None, (Keyword, )),
    ('email', formats.general_formats, generator.generate_id_string, (Keyword, )),
)


class Password(object):
    __cache = set()

    def __init__(self, information=None, field_map=()):
        self.information = {} if information is None else information
        self.field_map = field_map if field_map else BUILT_IN_FIELD_MAP
        self.suffix = Suffix()
        self.prefix = Prefix()
        self.keyword = Keyword()
        self.connector = Connector()

    def generate_source_dict(self):
        '''generate source dictionary `source_dict`.
        `source_dict` is a dictionary which the value contains all
        the situation of provided.
        The map of generate `source_dict` named `field_map`.
        `field_map` is tuple.

        ```
        field_map = (
            ('test', None, None, None),
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
        for row in self.field_map:
            if len(row) == 4:
                field, rule, method, types = row
            else:
                raise ValueError('Invalid map')

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

            for type_ in types:
                _ = self.__dict__[type_.__name__.lower()]
                _.extend(returned)
                self.__dict__[type_.__name__.lower()] = _

    def _equal(self, *args):
        args = list(args)
        ret = args.pop()

        if not args:
            return True

        if ret in args:
            return False
        else:
            return self._equal(*args)

    def generate_password(self):
        '''A generator yield passwords

        :return:
        '''
        self.generate_source_dict()
        for keyword in self.keyword:
            for suffix in self.suffix:
                    # for prefix in self.prefix:
                        for connector in self.connector:
                            if self._equal(keyword, suffix, connector):
                                password = keyword + connector + suffix
                                if password not in self.__cache:
                                    self.__cache.add(password)
                                    yield password

    def generate_password_with_dict(self):
        pass

    def __str__(self):
        return '<Password object>'
