#!/usr/bin/python3

"""
    This function takes in a subreddit name as input and retrieves
    the top ten hot articles from the subreddit.
    Parameters:
    subreddit (str): The subreddit to retrieve hot articles from
    Returns:
    None
"""

import requests


def top_ten(subreddit):
    """
    This function takes in a subreddit name as input and retrieves
    the top ten hot articles from the subreddit.
    Parameters:
    subreddit (str): The subreddit to retrieve hot articles from
    Returns:
    None
    """

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/\
      537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    }
    response = requests.get(
        "https://www.reddit.com/r/" + subreddit + "/hot.json?limit=10",
        headers=headers)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            print(post["data"]["title"])
    else:
        print(None)
