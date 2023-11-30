#!/bin/bash
# Sends a GET request to a URL and displays the body of the response

url=$1

# Send GET request and only display body for 200 status code
curl -sL -w "%{http_code}" "$url" -o /dev/null | {
    read -r status
    if [ "$status" -eq 200 ]; then
        curl -s "$url"
    fi
}
