#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept
curl -i -L -X OPTIONS "$1"
