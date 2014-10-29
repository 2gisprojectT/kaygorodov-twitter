#-*- coding:UTF-8 -*-
import sys
from unittest import TestCase
import unittest
from selenium import webdriver
from helpers.home_page import HomePage
from config.user import User
from config import config


@config.on_platforms(config.browsers)
class Login(TestCase):
    def setUp(self):
        self.desired_capabilities['name'] = self.id()
        self.desired_capabilities['public'] = 'public'
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

    def tearDown(self):
        print("Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id)
        try:
            if sys.exc_info() == (None, None, None):
                config.sauce.jobs.update_job(self.driver.session_id, passed=True)
            else:
                config.sauce.jobs.update_job(self.driver.session_id, passed=False)
        finally:
            self.driver.quit()

    def test_login_username(self):
        self.home_page.signin_form.login(self.user.username, self.user.password)
        assert self.home_page.is_logged

    def test_login_email(self):
        self.home_page.signin_form.login(self.user.email, self.user.password)
        assert self.home_page.is_logged

    def test_login_phone(self):
        self.home_page.signin_form.login(self.user.phone, self.user.password)
        assert self.home_page.is_logged

if __name__ == '__main__':
    unittest.main()