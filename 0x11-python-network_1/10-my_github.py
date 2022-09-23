#!/usr/bin/python3
"""
takes GitHub credentials (username and password) and uses the GitHub API
to display id
"""
from sys import argv
from requests.auth import HTTPBasicAuth
import requests


if __name__ == '__main__':
    r = requests.get(
        'https://api.github.com/user',
        auth=HTTPBasicAuth(argv[1], argv[2])
    )
    print(r.json().get('id'))
