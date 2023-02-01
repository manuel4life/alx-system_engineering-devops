#!/usr/bin/python3
import requests

def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit. If not a valid subreddit, prints None."""
    headers = {'User-Agent': 'My Reddit API Client'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        for post in posts:
            title = post.get('data', {}).get('title', '')
            print(title)
    else:
        print(None)
