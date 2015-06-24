# coding=utf-8
from __future__ import print_function
from optparse import OptionParser
from lib.model import Person
import re
import time


def parse_input(string, type_='str'):
    if not string:
        return ''
    data = map(lambda s: s.strip(), string.split(','))
    if type_ == 'int':
        data = map(int, filter(lambda i: i.isdigit(), data))
    elif type_ == 'email':
        data = filter(lambda i: re.match(r'^[\w\d.-_]+@[\w\d.-]+\.[\w]{2,8}$', i), data)
    return list(set(data))


def cmd_parser():
    parser = OptionParser()
    parser.add_option('-n', '--name', dest='name', action='store',
                      help='true name of target, split by ","')
    parser.add_option('-u', '--username', dest='username', action='store',
                      help='username of target, split by ","')
    parser.add_option('-b', '--birthday', dest='birthday', action='store',
                      help='birthday of target, format: %Y-%m-%d')
    parser.add_option('-q', '--qq', dest='qq_number', action='store',
                      help='QQ number of target, split by ","')
    parser.add_option('-e', '--email', dest='email', action='store',
                      help='email of target, split by ","')
    parser.add_option('-f', '--file', dest='file', action='store',
                      help='json format file\'s path of target information')

    args, _ = parser.parse_args()
    person = Person()

    if args.file:
        raise NotImplementedError
    else:
        person.name = parse_input(args.name)
        person.username = parse_input(args.username)
        person.qq_number = parse_input(args.qq_number, 'int')
        person.email = parse_input(args.email, 'email')

    try:
        person.birthday = time.strptime(args.birthday, '%Y-%m-%d')
    except (ValueError, TypeError):
        person.birthday = None

    return person
