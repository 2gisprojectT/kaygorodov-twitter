#-*- coding:UTF-8 -*-
from unittest import TestCase
import unittest
from selenium import webdriver
from helpers.page import Page


class SearchRoutes(TestCase):

    def test_search_routes(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        page = Page(driver)

        page.open("http://2gis.ru")
        page.search_bar.open_routes_tab()
        page.search_bar.search_routes(u'пл.Кирова', u'Метро Студенческая')
        self.assertTrue(page.routes_result.found())
        driver.close()

if __name__ == '__main__':
    unittest.main()
