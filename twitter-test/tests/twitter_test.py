#-*- coding:UTF-8 -*-
from unittest import TestCase
import unittest
from selenium import webdriver
from helpers.home_page import HomePage
from users.user import User


class TwitterTest(TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.home_page = HomePage(self.driver)
        self.home_page.open()

        user = User()
        self.home_page.signin_form.login(user.username, user.password)

    def test_send_tweet(self):

        self.home_page.modal_tweet_box.open()
        tweet = 'hello twitter'
        self.home_page.modal_tweet_box.send_tweet(tweet)
        assert tweet in self.driver.page_source

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()