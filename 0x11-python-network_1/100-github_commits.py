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
        'https://api.github.com/repos/{}/{}/commits'.format(repo, owner))
    commits = r.json()
    for commit in commits[:10]:
        author = commit.get('commit').get('author').get('name')
        sha = commit.get('sha')
        print('{}: {}'.format(sha, author))
