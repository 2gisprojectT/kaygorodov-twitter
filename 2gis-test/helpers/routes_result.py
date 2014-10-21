from helpers.base_component import BaseComponent


class RoutesResult(BaseComponent):

    selectors = {
        'self': '.routeResults'
    }

    def found(self):
        return self.driver.find_element_by_css_selector(self.selectors['self']).is_displayed()