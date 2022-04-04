import unittest
from selenium import webdriver
from Pages.LoginPage.Login.LoginPage import LoginField
from Pages.LoginPage.Password.PasswordPage import PasswordField
from Pages.Main.NavigationBar.NavigationBar import NavBar
from Common.Variables.variables import VareablesClass


class LoginTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.variables = VareablesClass()
        cls.driver = webdriver.Chrome(cls.variables.generatePath())
        cls.driver.maximize_window()
        cls.driver.delete_all_cookies()
        cls.driver.implicitly_wait(10)
        cls.loginBlock = LoginField(cls.driver)
        cls.passwordPage = PasswordField(cls.driver)
        cls.navigationBar = NavBar(cls.driver)

    def test_AmazoneTestCase(self):
        self.driver.get(self.variables.testingLink)
        self.loginBlock.fill_login_field()
        self.loginBlock.press_continue_button()
        self.passwordPage.keep_me_sign_in_field()
        self.passwordPage.fill_password_field()
        self.passwordPage.press_signIn_button()
        self.navigationBar.pop_up_sign_out()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == "__main__":
    unittest.main()
