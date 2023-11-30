#!/bin/bash

# Takes a URL as an argument, sends a POST request with specific parameters, and displays the body of the response

url=$1

# Send a POST request with email and subject parameters
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$url"
