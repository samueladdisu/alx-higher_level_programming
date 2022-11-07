#!/usr/bin/python3
"""
Fetch Header Data
"""
import sys
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as resp:
        data = dict(resp.headers)
        print(data.get('X-Request-Id'))
