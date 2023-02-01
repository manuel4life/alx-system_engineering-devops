#!/usr/bin/python3
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    """
import requests
    
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If an invalid subreddit is given, returns 0.
    """
def number_of_subscribers(subreddit):
    # Set custom User-Agent header to avoid errors related to too many requests
    headers = {'User-Agent': 'My Reddit API Client'}
    
    # Construct the API URL for the given subreddit
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    
    # Make a GET request to the Reddit API, with redirects disabled
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # If the request is successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        
        # Get the number of subscribers from the JSON data
        subscribers = data.get('data', {}).get('subscribers', 0)
        return subscribers
    else:
        return 0

