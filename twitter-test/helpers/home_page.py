from selenium.common.exceptions import NoSuchElementException


class HomePage():

    selectors = {
        'logged_in': '.logged-in',
        'logged_out': '.logged-out'
    }

    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://twitter.com'

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

    @property
    def is_logged(self):
        try:
            self.driver.find_element_by_css_selector(self.selectors['logged_in'])
        except NoSuchElementException:
            return False
        return True

    def open(self):
        self.driver.get(self.url)

    def logout(self):
        self.driver.delete_all_cookies()