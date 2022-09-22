#!/bin/bash
# sends request to a given url and only displays response if status code is 200
curl -sL "$1"
