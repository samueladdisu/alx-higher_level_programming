#!/usr/bin/python3
"""
Get request status
"""
import requests


if __name__ == "__main__":
    resp = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    data = resp.text
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))
