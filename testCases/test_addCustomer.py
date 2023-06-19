import pytest
import time
import string
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.read_properties import ReadConfig
from utilities.customLogger import LogGen


class Test_003_AddCustomer:
    baseurl = ReadConfig.getApplicationurl()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("********Test_003_AddCustomer*******")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.loginbutton()
        self.logger.info("************ Login Successful ************")

        self.logger.info("******************Starting Add Customer Test*************************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.ClickonCustomerMenu()
        self.addcust.ClickonCustomerMenuItem()

        self.addcust.AddNewButton()
        self.logger.info("*************Providing Customer ***********************")

        self.email = random_generator() + "@gmail.com"
        time.sleep(5)
        self.addcust.SetEmail(self.email)
        self.addcust.SetPassword("test123")
        self.addcust.SetFirstName("Shivani")
        self.addcust.SetLastName("Yadav")
        self.addcust.SetGender("Female")
        self.addcust.SetDob("01/12/1969")
        self.addcust.SetCompanyName(" Bits-quad software pvt limited ")
        time.sleep(5)
        self.addcust.Checkbox()
        self.addcust.NewsLetter()
        time.sleep(3)
        self.addcust.NewsLetterValue()
        self.addcust.SetCustomerRoles()
        self.addcust.SetCustomerRolesValue("Guests")
        time.sleep(8)
        self.addcust.SetManageOfVendor("Vendor 1")
        time.sleep(5)
        self.addcust.SetAdminContent("This is for testing the testing is your world.....")
        time.sleep(5)
        self.addcust.ClickSaveButton()
        time.sleep(10)

        self.logger.info("***********Saving customer info************")
        self.logger.info("**************Add Customer validation started ********************************")

        self.msg = self.driver.find_element(By.TAG_NAME, 'body').text
        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("************ Add customer Test Passed ***************")

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")
            self.logger.error("***********Add customer Test Failed*******************************")
            assert True == False

        self.driver.close()
        self.logger.info("*********** Ending Home Page Title Test ********************")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
