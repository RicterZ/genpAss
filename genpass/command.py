# coding: utf-8
from __future__ import print_function
from genpass.lib.cmdline import cmd_parser


class GeneratePassword(object):
    with_dict = False
    output_file = None

    def genpass(self, person):
        if self.with_dict:
            passwords = person.generate_password_with_dict()
        else:
            passwords = person.generate_password()

        if self.output_file:
            for i in passwords:
                self.output_file.write('%s\n' % i)
        else:
            for i in passwords:
                print(i)


def main():
    args, person_list = cmd_parser()
    gen = GeneratePassword()
    gen.with_dict = args.with_dict
    gen.output_file = args.output_file

    map(gen.genpass, person_list)


if __name__ == '__main__':
    main()
