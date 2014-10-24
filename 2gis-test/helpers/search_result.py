from helpers.base_component import BaseComponent


class SearchResult(BaseComponent):

    selectors = {
        'self': '.searchResults__list',
        'count': '//*[@id="module-1-9-1-1"]/nav/div[2]/div[2]',
        'not_found': '.noResults ._error_catalogNotFound'
    }

    paths = {
        'not_found': '//*[@id="module-1-9-1-2"]/header'
    }

    @property
    def count(self):
        return int(self.driver.find_element_by_xpath(self.selectors['count']).text)

    def found(self):
        if self.driver.find_element_by_xpath(self.paths['not_found']).is_displayed():
            return False
        else:
            return True