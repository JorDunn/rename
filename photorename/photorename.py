#!/usr/bin/env python3

"""pyrename 1.0.9
Copyright (c) 2016-2018, Jordan Dunn.

Usage:
    photorename [--md5 | --sha224 | --sha512] -i <input_file> -o <output_dir>
    photorename [-h | --help]

Options:
    -a --all            Rename all files in the current directory
    -i --input_file     Set the file to be renamed
    -o --ouput_path     The path to output the file to
    -v --verbose        Increase output verbosity
    -h --help           Display this message
    --md5               Use md5 to generate the file name
    --sha224            Use sha224 to generate the file name
    --sha512            Use sha512 to generate the file name
"""

import os
import os.path
import sys
from hashlib import md5, sha224, sha512
from docopt import docopt

args = docopt(__doc__, version='photorename v1.0.9')


def verbose(args, string):
    if args.verbose:
        print(string)


def get_md5_string(input_file):
    m = md5()
    m.update(input_file)
    md5string = str(m.hexdigest())
    return md5string


def get_sha224_string(input_file):
    s = sha224()
    s.update(input_file)
    sha224string = str(s.hexdigest())
    return sha224string


def get_sha512_string(input_file):
    s = sha512()
    s.update(input_file)
    sha512string = str(s.hexdigest())
    return sha512string


def rename():
    try:
        verbose(args, "Input File: " + os.path.realpath(args.input_file))
        in_f = os.path.realpath(args.input_file)
    except TypeError:
        print("You must specify an input file.")
        sys.exit(1)
    _, f_ext = os.path.splitext(in_f)
    if args.output_path:
        output_path = "{0}//".format(os.path.realpath(args.output_path))
    else:
        output_path = "{0}//".format(os.getcwd())
    if args.md5:
        out_f = "{0}\\{1}{2}".format(output_path, get_md5_string(
            args.input_file.encode('utf-8')), f_ext)
    elif args.sha224:
        out_f = "{0}\\{1}{2}".format(output_path, get_sha224_string(
            args.input_file.encode('utf-8')), f_ext)
    elif args.sha512:
        out_f = "{0}\\{1}{2}".format(output_path, get_sha512_string(
            args.input_file.encode('utf-8')), f_ext)
    try:
        verbose(args, "Output File: " + out_f)
        os.rename(in_f, out_f)
    except IOError as error:
        print(error)
        sys.exit(1)


if __name__ == '__main__':
    print(__doc__)
