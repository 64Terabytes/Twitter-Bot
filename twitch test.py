from tkinter.messagebox import NO, YES
from twitchAPI.twitch import Twitch
import json

# create instance of twitch API and create app authentication
TwitchAPI = Twitch('62ysldz1a8qguhweba2k5j99iylyyw', 'fu3473eldoest10pj7sqmnviap9c7l')

triggerphrase = 'doc'



user_list = json.loads(open('users.json').read())
#print(user_list['users'][0])

for user in user_list['users']:
    username = TwitchAPI.search_channels(query=user, first=1)['data'][0]['broadcaster_login']
    is_live = TwitchAPI.search_channels(query=user, first=1)['data'][0]['is_live']
    streamtitle = TwitchAPI.search_channels(query=user, first=1)['data'][0]['title']
    
    user_all = TwitchAPI.search_channels(query=user, first=1)
    
    
    if is_live == False:
        if streamtitle.lower().find(triggerphrase) != -1:
            print(username, "is live.", streamtitle,"at twitch.tv/{}".format(username))
    
    
    
    
    #print(user_all)
    #print(username, 'is live:', is_live, 'title:', streamtitle)

# get ID of user
#user_info = TwitchAPI.get_users(logins=[user])
#user_id = user_info['data'][0]['id']
    


#print(user_info)
#print(search_user)