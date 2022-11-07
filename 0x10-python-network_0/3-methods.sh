#!/bin/bash
# Get content  from request
curl -s -I "$1" |grep Allow|cut -d" " -f2-
