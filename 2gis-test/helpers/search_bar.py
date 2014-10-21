from helpers.base_component import BaseComponent


class SearchBar(BaseComponent):

    selectors = {
        'self': '.online__searchBar',
        'tab_ref_book': '.searchBar__tab .searchBar__refbookTab',
        'input': '.searchBar__form .searchBar__textfield._refbook .suggest__input',
        'submit_ref': '.searchBar__submit._refbook',
        'tab_routes': '.searchBar__tab .searchBar__rsTab',
        'where from': '.searchBar__textfield._from',
        'where to': '.searchBar__textfield._to',
        'submit_rs': '.searchBar__submit._rs'
    }

    paths = {
        'self': '.online__searchBar',
        'tab_ref_book': '//*[@id="module-1-1"]/div[1]/div[1]',
        'tab_routes': '//*[@id="module-1-1"]/div[1]/div[2]',
        'where from': '//*[@id="module-1-1-2"]/div/input',
        'where to': '//*[@id="module-1-1-3"]/div/input',
    }

    def open_ref_book_tab(self):
        self.driver.find_element_by_xpath(self.paths['tab_ref_book']).click()

    def open_routes_tab(self):
        self.driver.find_element_by_xpath(self.paths['tab_routes']).click()

    def search(self, query):
        self.driver.find_element_by_css_selector(self.selectors['input']).send_keys(query)
        self.driver.find_element_by_css_selector(self.selectors['submit_ref']).submit()

    def search_routes(self, where_from, to):
        self.driver.find_element_by_xpath(self.paths['where from']).send_keys(where_from)
        self.driver.find_element_by_xpath(self.paths['where to']).send_keys(to)
        self.driver.find_element_by_css_selector(self.selectors['submit_rs']).submit()