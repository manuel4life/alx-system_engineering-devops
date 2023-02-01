#!/usr/bin/python3

"""
    This function retrieves the number of subscribers of a given subreddit.
    Parameters:
    subreddit (str): The subreddit to retrieve the number of subscribers for
    Returns:
    int: The number of subscribers of the subreddit. If the subreddit does not
    exist or there is a problem with the request, returns 0.
"""
import requests


def number_of_subscribers(subreddit):
    """
    This function retrieves the number of subscribers of a given subreddit.
    Parameters:
    subreddit (str): The subreddit to retrieve the number of subscribers for
    Returns:
    int: The number of subscribers of the subreddit. If the subreddit does not
    exist or there is a problem with the request, returns 0.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/\
          537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
    }
    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        return 0
