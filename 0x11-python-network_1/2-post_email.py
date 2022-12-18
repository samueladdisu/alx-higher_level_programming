#!/usr/bin/python3
"""
Send mail with POST Request
"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as resp:
        data = resp.read()
        print(data.decode("utf-8"))