import time
from Pages.Common.BaseClass import BaseClass


class ProductInfoClass(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)

    def add_item_to_cart(self):
        addItem = self.findElement.find_my_element(self.locators.addToCartItemPage)
        addItem.click()
        time.sleep(2)

    def close_add_window(self):
        try:
            closeAddInfo = self.findElement.find_my_element(self.locators.closeAddInfoItemPage)
            closeAddInfo.click()
        except:
            print("There is no additional window")
        time.sleep(1)
