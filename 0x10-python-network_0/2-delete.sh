#!/bin/bash
# Sends a DELETE request to a URL and displays the body of the response

url=$1

# Send DELETE request and display complete response
response=$(curl -X DELETE -s -w "\n%{http_code}\n" "$url")
body=$(echo "$response" | head -n -1)
status_code=$(echo "$response" | tail -n 1)

# Display complete response
echo "Complete Response:"
echo "$body"

# Display body only for a 200 status code
if [ "$status_code" -eq 200 ]; then
    echo "Body:"
    echo "$body"
else
    echo "Error: HTTP $status_code"
fi
