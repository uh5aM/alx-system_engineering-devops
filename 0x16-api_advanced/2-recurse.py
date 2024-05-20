#!/usr/bin/python3
"""This script will return the number of subscribers associated with
a subreddit
"""
import json
import requests
from sys import argv


def get_titles(hot_list):
    """extracts the title from list of"""
    if hot_list:
        return [post['data'].get('title') for post in hot_list]
    return None


def recurse(subreddit, hot_list=[]):
    """Method get the number of users subscribed to a subreddit

    subreddit (Str) - subreddit to check

    Returns - number of users (INT) else 0 (INT) if not subreddit is found
    """
    try:
        h = {'user-agent': 'martin', 'allow_redirects': 'false'}
        if type(subreddit) is tuple:
            url = "https://www.reddit.com/r/{}/hot.json".format(subreddit[0])
            p = {'limit': 100, 'after': subreddit[1]}
            subreddit = subreddit[0]
        else:
            url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
            p = {'limit': 100}
        req = requests.get(url, headers=h, params=p)
        data = req.json().get('data', None)
        if req is None:
            return None
        elif data.get('after', None) is not None:
            sr = (subreddit, data.get('after'))
            recurse(sr, hot_list)

        hot_list += get_titles(data.get('children', None))
        return hot_list
    except Exception as e:
        return None


if __name__ == "__main__":
    pass
