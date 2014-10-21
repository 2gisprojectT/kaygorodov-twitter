#-*- coding:UTF-8 -*-
from unittest import TestCase
import unittest
from selenium import webdriver
from helpers.page import Page


class ShareLink(TestCase):

    def test_share_link(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        page = Page(driver)

        page.open("http://2gis.ru")
        query = 'rock city'
        page.search_bar.search(query)

        page.share_bar.open()
        shared_url = page.share_bar.share_link()
        page.open(shared_url)

        assert query in driver.page_source
        driver.close()

if __name__ == '__main__':
    unittest.main()
