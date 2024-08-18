import tweepy
import random
import time

# Twitter API credentials for API v2
API_KEY = "my_api_key"
API_SECRET_KEY = "api_secret"
BEARER_TOKEN = "my_bearer_token"
ACCESS_TOKEN = "access_token" #original creado el 10 de marzo de 2018 xd
ACCESS_TOKEN_SECRET = "access_secret" #x2

# Authenticate using OAuth 2.0 Bearer Token
client = tweepy.Client(bearer_token=BEARER_TOKEN, 
                       consumer_key=API_KEY, 
                       consumer_secret=API_SECRET_KEY, 
                       access_token=ACCESS_TOKEN, 
                       access_token_secret=ACCESS_TOKEN_SECRET)

def tweet_random_line(file_path):
    print("Attempting to tweet...")
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    if not lines:
        print("The file is empty!")
        return

    random_line = random.choice(lines).strip()

    try:
        # Post the tweet using API v2
        response = client.create_tweet(text=random_line)
        print(f'Tweeted: {random_line}')
        print(f'Tweet ID: {response.data["id"]}')
    except tweepy.TweepyException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = 'data/lyricsgreenday.txt'

    while True:
        tweet_random_line(file_path)
        time.sleep(3600)  # Shorter sleep duration for testing
