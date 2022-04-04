from Pages.Common.BaseClass import BaseClass


class SearchResultClas(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.getItemAttribute = "itemAttribute"

    def choose_random_item(self):
        chooseItem = self.findElement.find_my_element(self.locators.choosingItemAccountPage)
        chooseItem.click()

    def get_product_name(self):
        self.getItemAttribute = self.findElement.find_my_element(self.locators.choosingItemAccountPage).get_attribute("alt")
        print(str(self.getItemAttribute))
        return self.getItemAttribute
