import tweepy

# Keys (KEEP THIS HIDDEN!)
TweetAuth = tweepy.OAuth1UserHandler('AD3oebPhDSgIlFbhrGdMl0Jrd', 'ccWP5nFYHlg8CGCZZhT22mplPVs32IlmpaYpQIfUh9HXwiiI61', callback='oob')

# Twitter authentication
auth_url = TweetAuth.get_authorization_url()
print('Authorization URL: ' + auth_url)
verifier = input('PIN: ').strip()
TweetAuth.get_access_token(verifier)
TweetAuth.set_access_token(TweetAuth.access_token, TweetAuth.access_token_secret)
print('ACCESS TOKEN: ' + TweetAuth.access_token, "SECRET: " + TweetAuth.access_token_secret)