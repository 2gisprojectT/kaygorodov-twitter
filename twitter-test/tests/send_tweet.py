#-*- coding:UTF-8 -*-
from unittest import TestCase
import unittest
from selenium import webdriver
from helpers.home_page import HomePage
from users.user import User


class SendTweetTest(TestCase):

    def test_send_tweet(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        home_page = HomePage(driver)
        home_page.open()

        # Authentication
        user = User()
        driver.find_element_by_id("signin-email").send_keys(user.username)
        driver.find_element_by_id("signin-password").send_keys(user.password)
        driver.find_element_by_xpath("(//button[@type='submit'])[2]").click()

        home_page.modal_tweet_box.open()
        tweet = 'hello tweet'
        home_page.modal_tweet_box.send_tweet(tweet)

        assert tweet in driver.page_source
        driver.close()

if __name__ == '__main__':
    unittest.main()