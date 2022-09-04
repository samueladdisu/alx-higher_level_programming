#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):

    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as ex:
        stderr.write("Exception: ")
        stderr.write(ex.args[0])
        stderr.write("\n")
        return False
