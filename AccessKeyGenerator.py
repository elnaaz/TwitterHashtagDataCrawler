import tweepy, webbrowser


#we need an access key / secret to use Twitter API
#generate this here
class AccessKeyGenerator:
    CONSUMER_KEY = 'xxx'
    CONSUMER_SECRET = 'xxx'

    def getAccessKeyAndSecret(self):
        auth = tweepy.OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
        auth_url = auth.get_authorization_url()
        webbrowser.open(auth_url)
        #you can get this code from URL
        verifier = raw_input('PIN: ').strip()
        auth.get_access_token(verifier)
        print("ACCESS_KEY = '%s'" % auth.access_token.key)
        print("ACCESS_SECRET = '%s'" % auth.access_token.secret)
