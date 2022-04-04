import time
from Pages.Common.BaseClass import BaseClass
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class NavBar(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.action = ActionChains(driver)

    def fill_search_field(self):
        searchField = self.findElement.find_my_element(self.locators.searchFieldAccountPage)
        searchField.clear()
        searchField.send_keys(self.vareables.searchingItem)
        time.sleep(2)
        searchField.send_keys(Keys.ENTER)

    def click_into_cart_button(self):
        goToTheCart = self.findElement.find_my_element(self.locators.goToCartAccountPage)
        goToTheCart.click()
        time.sleep(2)

    def pop_up_sign_out(self):
        popUpWindow = self.findElement.find_my_element(self.locators.popUp)
        self.action.move_to_element(popUpWindow).perform()
        try:
            signOutButton = self.findElement.find_my_element(self.locators.signOut)
            time.sleep(2)
            self.action.move_to_element(signOutButton).click().perform()
            time.sleep(2)
        except:
            print("There is no button Sign Out")

    def pop_up_recomndation(self):
        popUpWindow = self.findElement.find_my_element(self.locators.popUp)
        self.action.move_to_element(popUpWindow).perform()
        try:
            recommendationsButton = self.findElement.find_my_element(self.locators.recommendations)
            time.sleep(2)
            self.action.move_to_element(recommendationsButton).click().perform()
            time.sleep(2)
        except:
            print("There is no button Sign Out")