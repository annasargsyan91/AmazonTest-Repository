from selenium.webdriver.common.by import By


class Locators():
    # Login page locator
    loginPageLoginFieldLocator = (By.ID, "ap_email")
    loginPageContinueButtonLocator = (By.ID, "continue")

    # Keep me sign in
    KeepMeSignInLocator = (By.NAME, "rememberMe")

    # Password page locator
    passwordPageLoginFieldLocator = (By.ID, "ap_password")
    passwordPageSignInButtonLocator = (By.ID, "signInSubmit")

    # Account page search field locator
    searchFieldAccountPage = (By.ID, "twotabsearchtextbox")

    # Choosing item
    choosingItemAccountPage = (By.XPATH, "(//img[@class = 's-image'])[1]")
    addToCartItemPage = (By.ID, "add-to-cart-button")

    # close additional window
    closeAddInfoItemPage = (By.ID, "attach-popover-lgtbox")

    # Cart page
    goToCartAccountPage = (By.ID, "nav-cart-count")

    # Deletin Item fron Cart
    deleteItems = (By.XPATH, "//input[@value = 'Delete']")

    #Pop Up
    popUp = (By.ID,"nav-link-accountList")
    signOut = (By.ID, "nav-item-signout")
    recommendations = (By.LINK_TEXT, "Recommendations")

    #Recommandation Item
    choseReccomendItem = (By.ID, "p13n-asin-index-2")
    clickRecommendItem = (By.XPATH, "//div[@class = 'a-column a-span3']")


