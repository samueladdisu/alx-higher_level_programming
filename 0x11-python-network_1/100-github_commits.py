#!/usr/bin/python3
"""
Handle errors
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/"+str(
        sys.argv[2]) + "/" + str(sys.argv[1]) + "/commits"
    resp = requests.get(url)
    data = list(resp.json())[0:10]
    try:
        for item in data:
            print("{}: {}".format(item.get(
                "sha"), item.get("commit").get("author").get("name")))
    except IndexError:
        pass
