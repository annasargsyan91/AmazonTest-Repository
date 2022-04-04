import time
from Pages.Common.BaseClass import BaseClass


class PasswordField(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)

    def keep_me_sign_in_field(self):
        KeepMeSignIn = self.findElement.find_my_element(self.locators.KeepMeSignInLocator)
        KeepMeSignIn.click()
        time.sleep(2)

    def fill_password_field(self):
        passwordField = self.findElement.find_my_element(self.locators.passwordPageLoginFieldLocator)
        passwordField.send_keys(self.vareables.defoultPassword)
        time.sleep(4)

    def press_signIn_button(self):
        signInButton = self.findElement.find_my_element(self.locators.passwordPageSignInButtonLocator)
        signInButton.click()
