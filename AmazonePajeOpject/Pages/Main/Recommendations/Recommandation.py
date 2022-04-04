import time

from Pages.Common.BaseClass import BaseClass
from Pages.Main.ProductInformation.ProductInformation import ProductInfoClass


class RecommendItemClas(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.productInfo = ProductInfoClass(driver)

    def choose_recommend_item(self):
        try:
            recommendItem = self.findElement.find_my_element(self.locators.choseReccomendItem)
            recommendItem.click()
            time.sleep(2)
        except:
            print("Recommenden element note found")

    def click_recommend_item(self):
        try:
            clickRecommendItem = self.findElement.find_my_element(self.locators.clickRecommendItem)
            clickRecommendItem.click()
        except:
            print("No item to add in Cart")

    def add_item_to_cart(self):
        try:
            self.addItemCart = self.productInfo.add_item_to_cart()

            return self.addItemCart
        except:

            return print("the item out off stock")

    def close_pop_up_window(self):
        try:
            self.closeWindow = self.productInfo.close_add_window()
            return self.closeWindow
        except:
            return print("there is no Additional window")
