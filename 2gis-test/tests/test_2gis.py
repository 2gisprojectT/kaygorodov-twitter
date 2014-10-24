#-*- coding:UTF-8 -*-
import os
import sys
import new
import unittest
from selenium import webdriver
from sauceclient import SauceClient
from unittest_data_provider import data_provider
from helpers.page import Page

# it's best to remove the hardcoded defaults and always get these values
# from environment variables
USERNAME = os.environ.get('SAUCE_USERNAME', "terracott")
ACCESS_KEY = os.environ.get('SAUCE_ACCESS_KEY', "0b7c1550-7807-48f4-ad20-9a8be45b57bb")
sauce = SauceClient(USERNAME, ACCESS_KEY)

browsers = [{"platform": "Mac OS X 10.9",
             "browserName": "chrome",
             "version": "31"},
            {"platform": "Windows 8.1",
             "browserName": "internet explorer",
             "version": "11"}]


def on_platforms(platforms):
    def decorator(base_class):
        module = sys.modules[base_class.__module__].__dict__
        for i, platform in enumerate(platforms):
            d = dict(base_class.__dict__)
            d['desired_capabilities'] = platform
            name = "%s_%s" % (base_class.__name__, i + 1)
            module[name] = new.classobj(name, (base_class,), d)
    return decorator


@on_platforms(browsers)
class SauceSampleTest(unittest.TestCase):
    def setUp(self):
        self.desired_capabilities['name'] = self.id()

        sauce_url = "http://%s:%s@ondemand.saucelabs.com:80/wd/hub"
        self.driver = webdriver.Remote(
            desired_capabilities=self.desired_capabilities,
            command_executor=sauce_url % (USERNAME, ACCESS_KEY)
        )
        self.page = Page(self.driver)
        self.driver.implicitly_wait(30)

    queries = lambda: (
        (u'Кафе', True),
        ('cafe', True),
        (u'НГТУ', True),
        ('ha8a8shd', False)
    )

    @data_provider(queries)
    def test_search(self, query, is_found):
        self.page.open("http://2gis.ru/")
        self.page.search_bar.search(query)
        if is_found:
            self.assertEquals(is_found, bool(self.page.search_result.count))
        else:
            self.assertEquals(is_found, self.page.search_result.found())

    def tearDown(self):
        print("Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id)
        try:
            if sys.exc_info() == (None, None, None):
                sauce.jobs.update_job(self.driver.session_id, passed=True)
            else:
                sauce.jobs.update_job(self.driver.session_id, passed=False)
        finally:
            self.driver.quit()
