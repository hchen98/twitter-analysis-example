import tweepy
  
# assign the values accordingly
consumer_key = "<your key here>"
consumer_secret = "<your key here>"
access_token = "<your key here>"
access_token_secret = "<your key here>"
  
# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  
# set access to user's access key and access secret 
auth.set_access_token(access_token, access_token_secret)
  
# calling the api 
api = tweepy.API(auth)
  
# the ID of the user
id = input("Please input the user Twitter account: ")
  
# fetching the user
user = api.get_user(id)

following_count = str(user.favourites_count)
  
print(f"The number of liked post of the user are : {following_count}")