# coding=utf-8
from __future__ import print_function
import re
import time
import argparse
import csv
import itertools
import generator
from rules import built_in
from lib.person import Person


def email(string):
    if not re.match(r'^[\w\d.-_]+@[\w\d.-]+\.[\w]{2,8}$', string):
        raise ValueError(string)
    return string


def date(date_string):
    if not date_string:
        return None
    return time.strptime(date_string, '%Y-%m-%d')


def cmd_parser():
    parser = argparse.ArgumentParser(description='User information')

    parser.add_argument('-n', '--name', dest='name', action='store',
                        help='real name of target', nargs='*', default=[])
    parser.add_argument('-u', '--username', dest='username', action='store',
                        help='usernames of target, English only', nargs='*', default=[])
    parser.add_argument('-q', '--qq', dest='qq', action='store',
                        help='QQ numbers of target', nargs='*', type=int, default=[])
    parser.add_argument('-e', '--email', dest='email', action='store',
                        help='email addresses of target', nargs='*', type=email, default=[])
    parser.add_argument('-m', '--mobile', dest='mobile_phone', action='store',
                        help='mobile phone/phone numbers of target', nargs='*', type=int, default=[])
    parser.add_argument('-b', '--birthday', dest='birthday', action='store',
                        help='birthday of target, format: %%Y-%%m-%%d', type=date, default=None)
    parser.add_argument('-c', '--company', dest='company', action='store',
                        help='company(english only)/website domain of target', type=str)

    parser.add_argument('--csv', dest='csv', action='store', type=argparse.FileType('r'),
                        help='csv files of users list')
    parser.add_argument('--with-dict', dest='with_dict', action='store_true',
                        help='generate passwords with weak password dictionary')
    parser.add_argument('-o', '--output', dest='output_file', action='store',
                        help='output result to a json file', type=argparse.FileType('w'))

    args = parser.parse_args()
    if not any(args.__dict__.values()):
        parser.print_help()
        raise SystemExit

    field_map = (
        ('qq', None),
        ('birthday', built_in.date_formats),
        ('company', built_in.general_formats),
        ('name', built_in.name_formats, generator.generate_name),
        (('username', 'name'), built_in.general_formats),
        (('email', 'name'), built_in.general_formats),
    )

    info_list = ['-n', '-e', '-b', '-u', '-m', '-q', '-c']

    person_list = []
    if not args.csv:
        person_list.append(Person(information=args.__dict__, field_map=field_map))
    else:
        for line in itertools.islice(csv.reader(args.csv), 1, None):
            if any(line):
                # TODO: validate the columns
                if len(line) < len(info_list):
                    raise Exception('Columns of csv file is not invalid')
                arg_string = ''
                for i, arg in enumerate(info_list):
                    if line[i]:
                        arg_string += '{0} {1} '.format(arg, line[i])
                args_csv = parser.parse_args(arg_string.split())
                person_list.append(Person(information=args_csv.__dict__, field_map=field_map))
    return (args, person_list)
