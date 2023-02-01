#!/usr/bin/python3

"""
    This function retrieves the title of all hot articles from a subreddit.
    Parameters:
    subreddit (str): The subreddit to retrieve hot articles from.
    after (str, optional): The 'after' parameter used for pagination of
    Reddit API results.
    hot_list (list, optional): A list to store the titles of the hot articles.
    Returns:
    list: A list of the titles of the hot articles from the subreddit.
    None: If the status code is not 200.
"""
import requests


def recurse(subreddit, after=None, hot_list=[]):
    """
    This function retrieves the title of all hot articles from a subreddit.
    Parameters:
    subreddit (str): The subreddit to retrieve hot articles from.
    after (str, optional): The 'after' parameter used for pagination of
    Reddit API results.
    hot_list (list, optional): A list to store the titles of the hot articles.
    Returns:
    list: A list of the titles of the hot articles from the subreddit.
    None: If the status code is not 200.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/\
          537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    }
    params = {
        'limit': 100
    }
    if after:
        params['after'] = after

    response = requests.get(
        "https://www.reddit.com/r/" + subreddit + "/hot.json", headers=headers,
        params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            hot_list.append(post["data"]["title"])

        after = data["data"]["after"]
        if after:
            return recurse(subreddit, after, hot_list)
        else:
            return hot_list
    else:
        return None
