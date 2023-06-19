import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.read_properties import ReadConfig
from utilities.customLogger import LogGen


class Test_004_SearchCustomerByName:
    baseurl = ReadConfig.getApplicationurl()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):
        self.logger.info("=================SearchCustomerByName_005=========================")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.loginbutton()
        self.logger.info("************ Login Successful ************")

        self.logger.info("==================Starting Search Customer By Name==========================")
        self.addcust = AddCustomer(self.driver)
        self.addcust.ClickonCustomerMenu()
        self.addcust.ClickonCustomerMenuItem()

        self.logger.info("====================searching customer by emailid======================================")
        searchcust = SearchCustomer(self.driver)
        searchcust.SetFirstName("Victoria")
        searchcust.SetLastName("Terces")
        time.sleep(8)
        searchcust.ClickSearch()
        status = searchcust.SearchCustomerByName("Victoria Terces")
        assert True == status

        self.logger.info("==================Search Customer By Name005 Finished=====================")
        self.driver.close()
