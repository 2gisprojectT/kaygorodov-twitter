from helpers.base_component import BaseComponent


class ModalTweetBox(BaseComponent):

    ids = {
        'self': 'global-tweet-dialog',
        'open_btn': 'global-new-tweet-button',
        'input': 'tweet-box-global',
    }

    selectors = {
        'count': 'tweet-counter'
    }

    paths = {
        'send': '//*[@id="global-tweet-dialog-dialog"]/div[2]/div[4]/form/div[2]/div[2]/button'
    }

    def open(self):
        self.driver.find_element_by_id(self.ids['open_btn']).click()

    def send_tweet(self, text):
        self.driver.find_element_by_id(self.ids['input']).send_keys(text)
        self.driver.find_element_by_xpath(self.paths['send']).click()