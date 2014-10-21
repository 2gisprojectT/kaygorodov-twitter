from helpers.base_component import BaseComponent


class ShareBar(BaseComponent):

    selectors = {
        'self': '.share__popup',
        'open_btn': '.extras__share',
        'close_btn': '.share__popupClose',
        'url_input': '.share__popupUrlInput'
    }

    paths = {
        'self': '.share__popup',
        'open_btn': '//*[@id="module-1-8"]/div[2]/div[1]',
        'close_btn': '//*[@id="module-1-14"]/div[2]/div[1]',
        'url_input': '//*[@id="module-1-14"]/div[2]/div[3]/input'
    }

    def open(self):
        self.driver.find_element_by_xpath(self.paths['open_btn']).click()

    def close(self):
        self.driver.find_element_by_css_selector(self.selectors['close_btn']).click()

    def share_link(self):
        return self.driver.find_element_by_css_selector(self.selectors['url_input']).get_attribute('value')
