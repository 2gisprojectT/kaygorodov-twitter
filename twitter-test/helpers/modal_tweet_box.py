from helpers.base_component import BaseComponent


class ModalTweetBox(BaseComponent):

    ids = {
        'self': 'global-tweet-dialog',
        'open_btn': 'global-new-tweet-button',
        'input': 'tweet-box-global',
    }

    selectors = {
        'send_btn': '.tweet-btn.js-tweet-btn',
        'count': '.tweet-counter'
    }

    paths = {
        'send_btn': '//*[@id="global-tweet-dialog-dialog"]/div[2]/div[4]/form/div[2]/div[2]/button',
        'text': '//*[@id="tweet-box-global"]/div'
    }

    def __init__(self, driver):
        super(ModalTweetBox, self).__init__(driver)
        self.driver = driver
        self._tweet_button = None

    @property
    def tweet_button(self):
        from helpers.tweet_button import TweetButton

        if self._tweet_button is None:
            self._tweet_button = TweetButton(self.driver)
        return self._tweet_button

    def open(self):
        self.driver.find_element_by_id(self.ids['open_btn']).click()

    def enter_tweet(self, text):
        self.driver.find_element_by_id(self.ids['input']).send_keys(text)

    def post_tweet(self):
        self.driver.find_element_by_xpath(self.paths['send_btn']).click()