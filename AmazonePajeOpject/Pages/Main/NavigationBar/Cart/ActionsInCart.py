import time
from Pages.Common.BaseClass import BaseClass
from Pages.Main.SearchingResult.SearchingResult import SearchResultClas


class ActionsInCart(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.choosingItem = SearchResultClas(self.driver)

    def check_item_in_cart(self, attribute):
        atribute = attribute
        try:
            if atribute in self.driver.page_source:
                pass
            print("Element in cart")
        except:
            print("No such element in Cart")
        time.sleep(1)

    def deleting_items(self):
        try:
            for delete in self.driver.page_source:
                print("Items deleted")
                deletingFile = self.findElement.find_my_element(self.locators.deleteItems)
                deletingFile.click()
                time.sleep(1)
        except:
            print("No more item for delete")
        time.sleep(3)

    def deleting_one_item(self):
        try:
            print("Items deleted")
            deletingFile = self.findElement.find_my_element(self.locators.deleteItems)
            deletingFile.click()
            time.sleep(1)
        except:
            print("No more item for delete")
        time.sleep(3)
