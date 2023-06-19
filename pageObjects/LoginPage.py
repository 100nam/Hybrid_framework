import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By


# pageobject class we have created for login page
class LoginPage:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[text()='Log in']"
    button_logout_linktext = "Logout"

    # it is a python constructor it will auto call when object creation
    def __init__(self, driver):
        self.driver = driver

    # action methods:
    # self keyword:  it is a "instance of the class" with this we can access the methods of the class
    # def setUserName is a userdefined name you will pass any of the name here
    def setUserName(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        time.sleep(5)
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)  # (username) as a parameter

    def setPassword(self, password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        time.sleep(5)
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

    def loginbutton(self):  # here we don't need to pass any arguments because it's just a click action
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def logoutbutton(self):
        self.driver.find_element_by_link_text(self.button_logout_linktext).click()

