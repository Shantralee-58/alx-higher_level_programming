#!/bin/bash
# This script makes a request to a specific URL that causes the server to respond with a message
curl -sLX PUT "$1" -d "user_id=98" -H "Origin: HolbertonSchool"
