#!/bin/bash
# takes in a url, sends a request to the url and displays the size of the response body
curl -sI "$1" | grep -i 'content-length:' | cut -d' ' -f2
