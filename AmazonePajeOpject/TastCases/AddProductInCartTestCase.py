import unittest
from selenium import webdriver
from Pages.LoginPage.Login.LoginPage import LoginField
from Pages.LoginPage.Password.PasswordPage import PasswordField
from Pages.Main.SearchingResult.SearchingResult import SearchResultClas
from Pages.Main.NavigationBar.NavigationBar import NavBar
from Pages.Main.ProductInformation.ProductInformation import ProductInfoClass
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
        cls.searchResult = SearchResultClas(cls.driver)
        cls.productInfo = ProductInfoClass(cls.driver)
        cls.navigationBar = NavBar(cls.driver)

    def test_AmazoneTestCase(self):
        self.driver.get(self.variables.testingLink)
        self.loginBlock.fill_login_field()
        self.loginBlock.press_continue_button()
        self.passwordPage.keep_me_sign_in_field()
        self.passwordPage.fill_password_field()
        self.passwordPage.press_signIn_button()
        self.navigationBar.fill_search_field()
        self.searchResult.choose_random_item()
        self.productInfo.add_item_to_cart()
        self.productInfo.close_add_window()
        self.navigationBar.pop_up_sign_out() #Todo not fork properly

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == "__main__":
    unittest.main()