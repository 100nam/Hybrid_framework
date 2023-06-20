import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.read_properties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseurl = ReadConfig.getApplicationurl()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()  # loggen :- method , LogGen: class

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("****************Test_001_Login*********************")
        self.logger.info("**************** verifying home page title *********************")

        self.driver = setup
        self.driver.get(self.baseurl)  # this two lines will launch our application
        time.sleep(5)
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("**************Home Page title is passed *********************")
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("**************** home page title is failed *********************")

            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("**************** verifying Login test *********************")

        self.driver = setup
        self.driver.get(self.baseurl)  # this two lines will launch our application #object name=lp,LoginPage= classname
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.loginbutton()
        # after login title change ho rha h uska validation kr rhe h yha pr
        actual_title = self.driver.title
        if actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("****************Test case is passed *********************")


        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("**************** Test case is failed *********************")
            self.logger.error("**************** Test case is failed *********************")

            assert False
