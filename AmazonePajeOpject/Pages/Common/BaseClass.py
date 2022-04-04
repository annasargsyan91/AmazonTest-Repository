from Locators.Locators import Locators
from Common.Variables.variables import VareablesClass
from Common.CustomFind.FindElement import CustomFindElement


class BaseClass():
    def __init__(self, driver):
        self.locators = Locators()
        self.driver = driver
        self.vareables = VareablesClass()
        self.findElement = CustomFindElement(self.driver)