import openai
import tweepy
import tweepy.client
import re
from re import sub

class GPT_x:
    @staticmethod
    def generate_response(prompt):
        openai.api_key = ""
        response = openai.completions.create(
            model="gpt-3.5-turbo-instruct",  
            prompt=prompt,
            max_tokens=2000 -len(prompt) ,               #500 - len(prompt)
            # temperature=0.5
        )

        text = response.choices[0].text.strip()
        text = sub(r'["".,!:\n]','', text)
        return text
    
    @staticmethod
    def Upload_in_Twitter(tweet_text:str,media_path:str): 
        baerer_token = ""
        consumer_key = ''
        consumer_secret = ''
        access_token = ''
        access_token_secret = ''
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        client = tweepy.Client(
                    bearer_token= baerer_token,
                    consumer_key=consumer_key,
                    consumer_secret= consumer_secret,
                    access_token=access_token,
                    access_token_secret=access_token_secret,      
                )
        try:
            media_id = api.media_upload(filename=media_path).media_id_string
            client.create_tweet(text=tweet_text,media_ids=[media_id])
        except: 
            pass
            

        