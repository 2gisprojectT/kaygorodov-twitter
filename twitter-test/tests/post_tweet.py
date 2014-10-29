#-*- coding:UTF-8 -*-
import sys
from unittest import TestCase
import unittest
from selenium import webdriver
from unittest_data_provider import data_provider
from helpers.home_page import HomePage
from config.user import User
from config import config


@config.on_platforms(config.browsers)
class PostTweet(TestCase):
    def setUp(self):
        self.desired_capabilities['name'] = self.id()
        self.desired_capabilities['public'] = 'share'
        self.desired_capabilities['build'] = '1.0'
        sauce_url = "http://%s:%s@ondemand.saucelabs.com:80/wd/hub"
        self.driver = webdriver.Remote(
            desired_capabilities=self.desired_capabilities,
            command_executor=sauce_url % (config.USERNAME, config.ACCESS_KEY)
        )
        self.driver.implicitly_wait(10)
        self.home_page = HomePage(self.driver)
        self.home_page.open()

        self.user = User()
        self.home_page.signin_form.login(self.user.username, self.user.password)
        assert self.home_page.is_logged

    def tearDown(self):
        print("Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id)
        try:
            if sys.exc_info() == (None, None, None):
                config.sauce.jobs.update_job(self.driver.session_id, passed=True)
            else:
                config.sauce.jobs.update_job(self.driver.session_id, passed=False)
        finally:
            self.driver.quit()

    valid_tweets = lambda: (
        ('hello tweet',),
        ('x',),
        ('a'*139,),
        ('b'*140,)
    )

    @data_provider(valid_tweets)
    def test_post_tweet_positive(self, tweet):
        self.home_page.modal_tweet_box.open()
        self.home_page.modal_tweet_box.enter_tweet(tweet)
        self.home_page.modal_tweet_box.post_tweet()
        assert tweet in self.driver.page_source

    def test_post_tweet_negative(self):
        self.home_page.modal_tweet_box.open()
        tweet = 'c'*141
        self.home_page.modal_tweet_box.enter_tweet(tweet)
        self.assertFalse(self.home_page.modal_tweet_box.tweet_button.enabled)


if __name__ == '__main__':
    unittest.main()