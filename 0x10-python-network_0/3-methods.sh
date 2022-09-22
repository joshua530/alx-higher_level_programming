#!/bin/bash
# fetches all methods a given url can accept
curl -sI "$1" | grep -i "Allow:" | cut -f2 -d' '
