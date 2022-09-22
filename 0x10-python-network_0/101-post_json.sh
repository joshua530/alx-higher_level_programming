#!/bin/bash
# sends a json post request $1 = url $2 = file containing json
curl -sX POST -H "Content-Type: application/json" -d "@$2" "$1"
