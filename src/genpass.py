# coding: utf-8
from __future__ import print_function
from .lib.cmdline import cmd_parser
import os
import sys
import json


def main():
    args = cmd_parser()
    sys.exit(0)
    if args.file:
        if not os.path.exists(args.file):
            print('File not Exist')
            sys.exit(0)
        with open(args.file) as f:
            data = f.read()
        person = Person(json.loads(data))
    else:
        person = Person()
        person.name = parse_input(args.name)
        person.username = parse_input(args.username)
        person.qq_number = parse_input(args.qq_number, 'int')
        person.email = parse_input(args.email, 'email')
        person.mobile_phone = parse_input(args.mobile_phone, 'int')


    if args.with_dict:
        passwords = person.generate_password_with_dict()
    else:
        passwords = person.generate_password()

    for password in passwords:
        print(password)


if __name__ == '__main__':
    main()
