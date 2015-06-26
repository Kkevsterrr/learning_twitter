#!/usr/bin/env python

def module_exists(module_name):
    '''function to check if an import exists'''
    try:
        __import__(module_name)
    except ImportError:
        return False
    else:
        return True

def main():
    nicePrint = PrettyPrinter(indent=2, width=70)
    #^object that prints complicated data in a readable way

    api = twitter.Api(consumer_key = 'zg9yQTGTT2oizk3XLMHGLzfpJ',
                      consumer_secret = 'nmiwqRpWDX0oxTCUTro8sPeUVUXIZHW9O1VZcTb0mLyfHw51sc',
                      access_token_key = '700001043-oxm3LZ72y4WmWGRqY66QjV0SzZoHGy5OGgwic26M',
                      access_token_secret = 'hGJZWTb5bjGFSiuIQrff5UajKdlyXcp7Lyun5SJzq05Su')

    #^Using twitter library we verify the app through the REST API with these keys

    user_info_dict = api.VerifyCredentials().AsDict()
    #^Gets my info as a dictonary

    nicePrint.pprint(user_info_dict)
    #^isplay user info

    print '\n'
    current_tweets = api.GetHomeTimeline()
    nicePrint.pprint([s.AsDict() for s in current_tweets])
    #^gets all current tweets in timeline(home page), and prints it all out in dicts 



if __name__ == "__main__":
    #^This should be the first thing that is checked in the program

    #docs and stuff https://github.com/bear/python-twitter

    import collections
    import re
    from pprint import PrettyPrinter
    #^default imports that should come with python

    if not module_exists('twitter'):

        #PROMPT THE USER TO AUTO DOWNLOAD THE RIGHT PACKAGE
        print "You do not have the twitter-python module required to run this program."

        answer = raw_input("May I install it for you (Y/N)")
        while answer.lower() != 'y' or answer.lower() != 'n':#correct 'Y','N','YES','NO'
            print "I don't undestand"
            answer = raw_input("May I install it for you (Y/N)")

        if answer[0].lower() == 'y':
            print "Installing Package"
            if module_exists(pip):
                import pip
                pip.main('install','python-twitter')
            else:
                print "Pip is not installed, install pip to download packages"

    if module_exists('twitter'):
        import twitter
        main()






