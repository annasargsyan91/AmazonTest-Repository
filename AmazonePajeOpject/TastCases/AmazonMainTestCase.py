import unittest
from selenium import webdriver
from Pages.LoginPage.Login.LoginPage import LoginField
from Pages.LoginPage.Password.PasswordPage import PasswordField
from Pages.Main.SearchingResult.SearchingResult import SearchResultClas
from Pages.Main.NavigationBar.NavigationBar import NavBar
from Pages.Main.ProductInformation.ProductInformation import ProductInfoClass
from Common.Variables.variables import VareablesClass
from Pages.Main.NavigationBar.Cart.ActionsInCart import ActionsInCart
from Pages.Main.Recommendations.Recommandation import RecommendItemClas
from webdriver_manager.chrome import ChromeDriverManager

class LoginTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.variables = VareablesClass()
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()
        cls.driver.delete_all_cookies()
        cls.driver.implicitly_wait(10)
        cls.loginBlock = LoginField(cls.driver)
        cls.passwordPage = PasswordField(cls.driver)
        cls.searchResult = SearchResultClas(cls.driver)
        cls.productInfo = ProductInfoClass(cls.driver)
        cls.navigationBar = NavBar(cls.driver)
        cls.actionsInCart = ActionsInCart(cls.driver)
        cls.recommendItem = RecommendItemClas(cls.driver)

    def test_AmazoneTestCase(self):
        self.driver.get(self.variables.testingLink)
        self.loginBlock.fill_login_field()
        self.loginBlock.press_continue_button()
        self.passwordPage.keep_me_sign_in_field()
        self.passwordPage.fill_password_field()
        self.passwordPage.press_signIn_button()
        self.navigationBar.fill_search_field()
        self.searchResult.get_product_name()
        self.searchResult.choose_random_item()
        self.productInfo.add_item_to_cart()
        self.productInfo.close_add_window()
        self.navigationBar.click_into_cart_button()
        self.actionsInCart.check_item_in_cart(self.searchResult.getItemAttribute)
        self.actionsInCart.deleting_one_item()
        self.navigationBar.pop_up_recomndation()
        self.recommendItem.choose_recommend_item()
        self.recommendItem.click_recommend_item()
        self.recommendItem.add_item_to_cart()
        self.recommendItem.close_pop_up_window()
        self.navigationBar.pop_up_sign_out()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == "__main__":
    unittest.main()