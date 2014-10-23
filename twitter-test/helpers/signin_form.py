from helpers.base_component import BaseComponent


class SignInForm(BaseComponent):

    ids = {
        'self': '',
        'login': 'signin-email',
        'password': 'signin-password',
    }

    paths = {
        'submit': "(//button[@type='submit'])[2]"
    }

    def login(self, username, password):
        self.driver.find_element_by_id(self.ids['login']).send_keys(username)
        self.driver.find_element_by_id(self.ids['password']).send_keys(password)
        self.driver.find_element_by_xpath(self.paths['submit']).click()