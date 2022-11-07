#!/usr/bin/python3
"""
Handle errors
"""
import sys
import requests


if __name__ == "__main__":
    resp = requests.get(sys.argv[1])
    if resp.status_code >= 400:
        print("Error code: {}".format(resp.status_code))
    else:
        print(resp.text)
