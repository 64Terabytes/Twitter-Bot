import tweepy
from twitchAPI.twitch import Twitch
import json

# API credentials (KEEP THIS HIDDEN)
TweetAuth = tweepy.OAuth1UserHandler('AD3oebPhDSgIlFbhrGdMl0Jrd', 'ccWP5nFYHlg8CGCZZhT22mplPVs32IlmpaYpQIfUh9HXwiiI61', callback='oob')
TwitchAPI = Twitch('62ysldz1a8qguhweba2k5j99iylyyw', 'fu3473eldoest10pj7sqmnviap9c7l')

# Twitter authentication
auth_url = TweetAuth.get_authorization_url()
print('Authorization URL: ' + auth_url)
verifier = input('PIN: ').strip()
TweetAuth.get_access_token(verifier)
TweetAuth.set_access_token(TweetAuth.access_token, TweetAuth.access_token_secret)
print()
# Create Twitter API object's
TweetAPI = tweepy.API(TweetAuth)

# Bot Code
triggerphrase = 'doc'
user_list = json.loads(open('users.json').read())


# for user in user_list['users']:
#     username = TwitchAPI.search_channels(query=user, first=1)['data'][0]['broadcaster_login']
#     is_live = TwitchAPI.search_channels(query=user, first=1)['data'][0]['is_live']
#     streamtitle = TwitchAPI.search_channels(query=user, first=1)['data'][0]['title']
    
#     user_all = TwitchAPI.search_channels(query=user, first=1)
    
    
#     if is_live == False:
#         if streamtitle.lower().find(triggerphrase) != -1:
#             TweetAPI.update_status(username + " is live. " + streamtitle + " at twitch.tv/" + username)









#TweetAPI.update_status("Bot Test lmao")