#!/bin/bash
# sends a request and prints out the status code
curl -o /dev/null -w '%{http_code}' -sIL "$1"
