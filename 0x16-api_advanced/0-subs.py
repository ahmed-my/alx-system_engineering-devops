#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""
import requests
def number_of_subscribers(subreddit):
    """returns the total number of subscribers for a given subreddit."""

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        subreddit_info = response.json().get('data', {})
        subscribers_count = subreddit_info.get('subscribers', 0)
        return subscribers_count
    elif response.status_code == 302:
        return 0
    else:
        return 0
