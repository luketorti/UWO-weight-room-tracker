import tweepy as tw
import pandas as pd
import requests

# API keys ----------> * Add your keys here *
consumerKey = ""
consumerSecret = ""
bearerToken = ""
accessToken = ""
accessSecret = ""

# set user id of @WesternWeightRm
userID = "297549322"

# sets up client
client = tw.Client(bearer_token=bearerToken,
consumer_key=consumerKey,
consumer_secret=consumerSecret, 
access_token=accessToken, 
access_token_secret=accessSecret, 
return_type = requests.Response,
wait_on_rate_limit=True)

# pulls tweets
tweets = client.get_users_tweets(id = userID,
exclude = "retweets",
max_results = 10,
tweet_fields = ["created_at"])

# sends tweets to data frame
tweets_dict = tweets.json()
tweets_data = tweets_dict['data']
df = pd.json_normalize(tweets_data)

# takes latest tweet from the data frame (1st row)
firstRow = df.iloc[0].tolist()
firstRowInfo = firstRow[2]

# cuts out other fitness centre capacities from the string, leaves only weight room
onlyWeightRoomInfo = firstRowInfo[0:8]      # originally 6, but reformatting of tweets forced a change (must be edited if tweet format changes)

# cuts out extras in string, leaving only numerical value
occupancy1 = onlyWeightRoomInfo.replace("WR", "")
occupancy2 = occupancy1.replace("CM", "")
occupancy3 = occupancy2.replace(":", "")
finalOccupancy = occupancy3.replace("-", "")
