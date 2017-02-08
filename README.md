# mining-minipro
This is WIP on a mini-project.
Currently, it just mines the last 20 statuses of Donald Trump from Twitter using Tweepy.

Dependencies:

Python3:

`sudo apt-get install python3`

Tweepy:

`pip install tweepy`

To access Twitter API, you require a consumer key, consumer secret key, API token and API token secret.
Twitter API does not allow a person to share their apps keys publicly. Thus, you'll have to generate your own keys and plug them in the code.
Getting your own keys requires you to register your own app at https://apps.twitter.com/app/new
This app is just a placeholder and it's purpose is to get these keys.
This is a tutorial for the aforementioned process:
http://stackoverflow.com/questions/1808855/getting-new-twitter-api-consumer-and-secret-keys


I'm currently working on a method that will allow a user to use my keys by submitting a request to my server with the code and my server will then communicate with the Twitter API.
