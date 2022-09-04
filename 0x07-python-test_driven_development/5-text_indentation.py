#!/usr/bin/python3
"""
Text indentation function module doc
"""


def text_indentation(text):

    """
    add 2 new line after each special chars . ? and :
    Args:
        text(str): text input
    Raises:
        TypeError: if input is not string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    prev = None
    start = 0
    while text[start] == " ":
        start += 1
    text = text[start:]
    for c in text:
        if c in ['.', ':', "?"]:
            print(c)
            print()
            prev = c
        else:
            if prev in ['.', '?', ':'] and c == " ":
                pass
            else:
                print(c, end="")
                prev = "a"
