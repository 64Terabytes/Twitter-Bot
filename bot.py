import tweepy
from twitchAPI.twitch import Twitch
import json

# Credentials (KEEP THIS HIDDEN)
TweetAuth = tweepy.OAuth1UserHandler('AD3oebPhDSgIlFbhrGdMl0Jrd', 'ccWP5nFYHlg8CGCZZhT22mplPVs32IlmpaYpQIfUh9HXwiiI61', callback='oob')
TwitchAPI = Twitch('62ysldz1a8qguhweba2k5j99iylyyw', 'fu3473eldoest10pj7sqmnviap9c7l')
TweetAuth.set_access_token('1498134814058115073-zk9BGcLnvkDYqQFqKYfwj3E1IFPXxA', '0PfhuHtBRrHoDaunUu6AuxQ2m7RCj5wimctCBbxyaNUle')

# Create Twitter API object's
TweetAPI = tweepy.API(TweetAuth)

# Bot Code
triggerphrase = 'sick'
user_list = json.loads(open('users.json').read())

# Main Script
for user in (user_list['users']):
    username = TwitchAPI.search_channels(query=user, first=1)['data'][0]['broadcaster_login']
    is_live = TwitchAPI.search_channels(query=user, first=1)['data'][0]['is_live']
    streamtitle = TwitchAPI.search_channels(query=user, first=1)['data'][0]['title']
    
    user_all = TwitchAPI.search_channels(query=user, first=1)
    
    
    if is_live == False:
        if streamtitle.lower().find(triggerphrase) != -1:
            print(username + " is live. " + streamtitle + " at twitch.tv/" + username)
#             TweetAPI.update_status(username + " is live. " + streamtitle + " at twitch.tv/" + username)









# TweetAPI.update_status("Amogus Sus")