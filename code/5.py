from twitterscraper import query_tweets

user = input("Please input a Twitter username: ")

r = query_tweets(user, limit=None)
len_r = len(r)

print(f"The number of tweets from {user} is: {len_r}")

