from unittest import TestCase
import unittest
from selenium import webdriver
from TestUser import TestUser


class TestPostTweet(TestCase):

    def test_post_tweet(self):
        # Test environment
        driver = webdriver.Firefox()
        user = TestUser()
        driver.get("https://twitter.com/")

        # Authentication
        driver.find_element_by_id("signin-email").send_keys(user.username)
        driver.find_element_by_id("signin-password").send_keys(user.password)
        driver.find_element_by_xpath("(//button[@type='submit'])[2]").click()

        # Post new tweet
        tweet = "Hello twitter"
        driver.find_element_by_id("global-new-tweet-button").click()
        driver.find_element_by_id("tweet-box-global").send_keys(tweet)
        driver.find_element_by_xpath("//*[@id='global-tweet-dialog-dialog']"
                                     "/div[2]/div[4]/form/div[2]/div[2]/button").click()
        assert tweet in driver.page_source

        # Finish
        driver.close()

if __name__ == '__main__':
    unittest.main()