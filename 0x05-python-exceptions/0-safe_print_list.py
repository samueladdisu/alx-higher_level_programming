#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    try:
        real = 0
        for i in range(x):
            print(my_list[i], end="")
            real = real + 1
    except Exception:
        pass
    finally:
        print()
        return real
