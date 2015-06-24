# coding: utf-8
from lib.cmdline import cmd_parser


def main():
    data = cmd_parser()
    data.generate_password()


if __name__ == '__main__':
    main()
