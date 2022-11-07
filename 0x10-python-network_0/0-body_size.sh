#!/bin/bash
# Get content length from request
curl -sI "$1" |grep Content-Length|awk '{print $2}'
