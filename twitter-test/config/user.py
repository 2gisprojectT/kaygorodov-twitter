import os

USERNAME = os.environ.get('TWITTER_USERNAME')
PASSWORD = os.environ.get('TWITTER_PASSWORD')
EMAIL = os.environ.get('TWITTER_EMAIL')
PHONE = os.environ.get('TWITTER_PHONE')


class User:
    def __init__(self):
        self.username = USERNAME
        self.password = PASSWORD
        self.email = EMAIL
        self.phone = PHONE
