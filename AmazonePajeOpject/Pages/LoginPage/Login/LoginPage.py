import time
from Pages.Common.BaseClass import BaseClass


class LoginField(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)

    def fill_login_field(self):
        loginField = self.findElement.find_my_element(self.locators.loginPageLoginFieldLocator)
        loginField.send_keys(self.vareables.defoultLogin)
        time.sleep(4)

    def press_continue_button(self):
        continueButton = self.findElement.find_my_element(self.locators.loginPageContinueButtonLocator)
        continueButton.click()
        time.sleep(2)
