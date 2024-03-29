#!/usr/bin/python3
"""
takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
letter must be sent in the variable q
If no argument is given, set q=""
"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) < 2:
        letter = ""
    else:
        letter = argv[1]
    payload = {'q': letter}
    url = 'http://0.0.0.0:5000/search_user'
    r = requests.post(url, data=payload)

    try:
        dic = r.json()
        if dic:
            print("[{}] {}".format(dic.get('id'), dic.get('name')))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
