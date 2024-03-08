#!/usr/bin/python3
"""
Script to query a list of all hot posts on a given Reddit subreddit.
"""
import requests

def recurse(subreddit, hot_list=[], after=None):
    """Recursively fetches titles of hot articles for a given subreddit."""
    base_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

    params = {"limit": 100, "after": after}

    try:
        response = requests.get(base_url, headers=headers, params=params, timeout=5)
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

    if 'data' in data and 'children' in data['data']:
        children = data['data']['children']
        if not children:
            return hot_list
        else:
            titles = [child['data']['title'] for child in children]
            hot_list.extend(titles)
            next_after = data['data']['after']
            return recurse(subreddit, hot_list, after=next_after)
    else:
        print(f"Invalid subreddit: {subreddit}")
        return None
