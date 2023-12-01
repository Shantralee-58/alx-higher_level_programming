#!/bin/bash
# Sends a JSON POST request to a URL with the contents of a file

url="$1"
json_file="$2"

# Check if the file exists and is a valid JSON
if [ -f "$json_file" ] && jq . "$json_file" > /dev/null 2>&1; then
    curl -sX POST -H "Content-Type: application/json" -d @"$json_file" "$url"
else
    echo "Not a valid JSON"
fi
