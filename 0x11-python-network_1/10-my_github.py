#!/usr/bin/python3
"""
get api
"""
import sys
import requests


if __name__ == "__main__":
    headers = {'Authorization': 'token '
               + sys.argv[2]}
    resp = requests.get("https://api.github.com/user", headers=headers)
    try:
        print(resp.json().get('id'))
    except Exception:
        pass
