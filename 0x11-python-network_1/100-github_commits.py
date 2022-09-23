#!/usr/bin/python3
"""
lists 10 commits (from the most recent to oldest) of the repository "rails"
by the user "rails"
"""
import requests
import sys


if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]
    r = requests.get(
        'https://api.github.com/repos/{}/{}/commits?page=1&per_page=10'
        .format(owner, repo))
    commits = r.json()
    for commit in commits:
        author = commit.get('commit').get('author').get('name')
        sha = commit.get('sha')
        print('{}: {}'.format(sha, author))
