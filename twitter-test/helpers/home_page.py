class HomePage():
    def __init__(self, driver):

        self.driver = driver
        self.url = 'http://twitter.com'

        self._modal_tweet_box = None

    @property
    def modal_tweet_box(self):
        from helpers.modal_tweet_box import ModalTweetBox

        if self._modal_tweet_box is None:
            self._modal_tweet_box = ModalTweetBox(self.driver)
        return self._modal_tweet_box

    def open(self):
        self.driver.get(self.url)