# coding=utf-8
from __future__ import print_function
import re
import time
import argparse


def email(string):
    if not re.match(r'^[\w\d.-_]+@[\w\d.-]+\.[\w]{2,8}$', string):
        raise ValueError(string)
    return string


def date(date_string):
    return time.strptime(date_string, '%Y-%m-%d')


def cmd_parser():
    parser = argparse.ArgumentParser(description='User information')

    parser.add_argument('-n', '--name', dest='name', action='store',
                        help='real name of target')
    parser.add_argument('-u', '--username', dest='username', action='store',
                        help='usernames of target', nargs='*')
    parser.add_argument('-q', '--qq', dest='qq_number', action='store',
                        help='QQ numbers of target', nargs='*', type=int)
    parser.add_argument('-e', '--email', dest='email', action='store',
                        help='email addresses of target', nargs='*', type=email)
    parser.add_argument('-m', '--mobile', dest='mobile_phone', action='store',
                        help='mobile phone/phone numbers of target', nargs='*', type=int)
    parser.add_argument('-b', '--birthday', dest='birthday', action='store',
                        help='birthday of target, format: %%Y-%%m-%%d', type=date)

    parser.add_argument('--csv', dest='is_csv', action='store_true',
                        help='csv files of users list')
    parser.add_argument('-f', '--file', dest='file', action='store',
                        help='json format file\'s path of target information')
    parser.add_argument('--with-dict', dest='with_dict', action='store_true',
                        help='generate password with weak password dictionary')
    parser.add_argument('-o', '--output', dest='output_file', action='store',
                        help='output result to a json file')

    args = parser.parse_args()

    print(args)
    return args
