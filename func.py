#!/usr/bin/env python
# coding: utf-8

# # Funções

# ## Importing libs

import os
import tweepy

# ## Auth

def create_api():
    consumer_key = os.getenv('CONSUMER_TOKEN')
    consumer_secret = os.getenv('CONSUMER_TOKEN_SECRET')
    access_token = os.getenv('ACCESS_TOKEN')
    access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    
    api = tweepy.API(auth)
    return api

def tweet(message):
    api = create_api()
    api.update_status(message)
    print("Tweeted:", message)

if __name__ == "__main__":
    tweet("Hello from GitHub Actions!")




