#-*- coding:UTF-8 -*-
from unittest import TestCase
import unittest
from unittest_data_provider import data_provider
from selenium import webdriver
from helpers.page import Page


class SeleniumTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(10)
        cls.page = Page(cls.driver)

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

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == '__main__':
    unittest.main()
