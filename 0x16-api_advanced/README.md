0x16-Advanced API

In this project, we have three different functions that use the Reddit API to retrieve and analyze data about hot posts on Reddit.
Function

 1: top_ten(subreddit)
This function takes a subreddit as an input and returns the titles of the first 10 hot posts on that subreddit. If the subreddit is not valid, the function returns None.
Function

 2: recurse(subreddit, hot_list=[])
This function takes a subreddit as input and returns a list of all the hot post titles on that subreddit. The function uses recursion to retrieve all the hot posts from multiple pages of the Reddit API. If no posts are found for the given subreddit or the subreddit is not valid, the function returns None.
Function 

3: count_words(subreddit, word_list)
This function takes a subreddit and a list of keywords as inputs. The function then retrieves all the hot posts on the subreddit and counts the number of times each keyword appears in the titles of the posts. The function then returns the count of each keyword in descending order, with the keywords that appear the most first. If a keyword appears multiple times, the count is the sum of all its appearances. If no posts match or the subreddit is invalid, the function returns nothing.

All the functions in this project use the Reddit API to retrieve data and can be run using Python.
