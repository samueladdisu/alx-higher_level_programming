#!/usr/bin/python3
"""
POST request
"""
import sys
import requests


if __name__ == "__main__":
    payload = {"email": sys.argv[2]}
    resp = requests.post(sys.argv[1], data=payload)
    print(resp.text)
