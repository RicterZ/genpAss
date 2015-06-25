# coding: utf-8
from __future__ import print_function
from lib.cmdline import cmd_parser, parse_input
from lib.person import Person
import time


def main():
    args = cmd_parser()
    person = Person()
    if args.file:
        raise NotImplementedError
    else:
        person.name = parse_input(args.name)
        person.username = parse_input(args.username)
        person.qq_number = parse_input(args.qq_number, 'int')
        person.email = parse_input(args.email, 'email')
        person.mobile_phone = parse_input(args.mobile_phone, 'int')

    try:
        person.birthday = time.strptime(args.birthday, '%Y-%m-%d')
    except (ValueError, TypeError):
        person.birthday = None

    if args.with_dict:
        passwords = person.generate_password_with_dict()
    else:
        passwords = person.generate_password()

    for password in passwords:
        print(password)


if __name__ == '__main__':
    main()
