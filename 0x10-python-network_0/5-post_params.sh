#!/bin/bash
# sends post request to given url and displays response
curl -sX POST -d'email=test@gmail.com' -d'subject=I will always be here for PLD' "$1"
