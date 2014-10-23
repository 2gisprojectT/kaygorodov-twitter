class HomePage():
    def __init__(self, driver):

        self.driver = driver
        self.url = 'http://twitter.com'
        self.is_logged = False

        self._modal_tweet_box = None
        self._signin_form = None

    @property
    def modal_tweet_box(self):
        from helpers.modal_tweet_box import ModalTweetBox

        if self._modal_tweet_box is None:
            self._modal_tweet_box = ModalTweetBox(self.driver)
        return self._modal_tweet_box

    @property
    def signin_form(self):
        from helpers.signin_form import SignInForm

        if self._signin_form is None:
            self._signin_form = SignInForm(self.driver)
        return self._signin_form

    def open(self):
        self.driver.get(self.url)