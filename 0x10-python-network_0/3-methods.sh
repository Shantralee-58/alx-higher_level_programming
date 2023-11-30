#!/bin/bash

# Takes a URL as an argument and displays all HTTP methods the server will accept

url=$1

# Send an OPTIONS request and display only the Allow header
curl -sI -X OPTIONS "$url" | grep -i Allow | cut -d ' ' -f 2-
