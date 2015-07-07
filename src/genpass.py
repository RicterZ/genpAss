# coding: utf-8
from __future__ import print_function
from .lib.cmdline import cmd_parser


def main():
    args, person = cmd_parser()
    if args.with_dict:
        passwords = person.generate_password_with_dict()
    else:
        passwords = person.generate_password()

    if args.output_file:
        for i in passwords:
            args.output_file.write('%s\n' % i)
    else:
        for i in passwords:
            print(i)


if __name__ == '__main__':
    main()
