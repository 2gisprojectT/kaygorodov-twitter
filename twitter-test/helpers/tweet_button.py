from helpers.base_component import BaseComponent
from selenium.common.exceptions import NoSuchElementException


class TweetButton(BaseComponent):

    selectors = {
        'self': '.tweet-btn.js-tweet-btn',
        'disabled': '.tweet-btn.js-tweet-btn.disabled'
    }

    paths = {
        'self': '/html/body/div[9]/div[2]/div[2]/div[4]/form/div[2]/div[2]/button'
    }

    @property
    def enabled(self):
        try:
            element = self.driver.find_element_by_xpath(self.paths['self'])
        except NoSuchElementException:
            return False
        return element.is_enabled()