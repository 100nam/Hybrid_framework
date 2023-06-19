import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AddCustomer:
    customer_menu_xpath = "//i[contains(@class,'fa-user')]/following-sibling::p"
    time.sleep(5)
    customer_menu_item_xpath = "//a[@href='/Admin/Customer/List']"
    add_new_button_xpath = "//a[@class='btn btn-primary']"
    email_xpath = "//input[@name='Email']"
    password_xpath = "//input[@name='Password']"
    first_name_xpath = "//input[@name='FirstName']"
    last_name_xpath = "//input[@id='LastName']"
    female_gender_xpath = "//input[@value='F']"
    male_gender_xpath = "//input[@value='M']"
    date_picker_xpath = "//input[@name='DateOfBirth']"
    company_name_xpath = "//input[@name='Company']"
    is_tax_exempt_xpath = "//input[@type='checkbox']"
    newsletter_xpath = "//input[contains(@aria-owns,'NewsletterSubscription')]"
    newsletter_value_xpath = "//li[text()='Your store name']"
    time.sleep(4)
    customer_roles_xpath = "//input[contains(@aria-owns,'SelectedCustomerRoleIds')]"
    time.sleep(6)
    list_item_administrator_xpath = "//li[contains(text(),'Administrators')]"
    list_item_forum_moderator = "//li[contains(text(),'Forum Moderators')]"
    list_item_register_xpath = "//li[contains(text(),'Registered')]"
    list_item_vendor_xpath = "//li[contains(text(),'Vendors')]"
    list_item_guest_xpath = "//li[contains(text(),'Guests')]"
    time.sleep(5)
    manage_of_vendor = "//*[@id='VendorId']"
    admin_comment = "//textarea[@name='AdminComment']"
    button_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def ClickonCustomerMenu(self):
        self.driver.find_element(By.XPATH, self.customer_menu_xpath).click()

    def ClickonCustomerMenuItem(self):
        self.driver.find_element(By.XPATH, self.customer_menu_item_xpath).click()

    def AddNewButton(self):
        self.driver.find_element(By.XPATH, self.add_new_button_xpath).click()

    def SetEmail(self, email):
        self.driver.find_element(By.XPATH, self.email_xpath).send_keys(email)

    def SetPassword(self, password):
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def SetCustomerRolesClick(self):
        self.driver.find_element(By.XPATH, )

    def SetCustomerRoles(self):
        self.driver.find_element(By.XPATH, self.customer_roles_xpath).click()

    def SetCustomerRolesValue(self,role):
        if role == "Registered":
            self.Listitem = self.driver.find_element(By.XPATH, self.list_item_register_xpath)

        elif role == "Administrators":
            self.Listitem = self.driver.find_element(By.XPATH, self.list_item_administrator_xpath)

        elif role == "Guests":
            time.sleep(5)
            #self.driver.find_element(By.XPATH, "//*[@id = 'SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.Listitem = self.driver.find_element(By.XPATH, self.list_item_guest_xpath)

        elif role == "Registered":
            self.Listitem = self.driver.find_element(By.XPATH, self.list_item_register_xpath)

        elif role == "Vendors":
            self.Listitem = self.driver.find_element(By.XPATH, self.list_item_vendor_xpath)

        elif role == "Forum Moderators":
            self.Listitem = self.driver.find_element(By.XPATH, self.list_item_forum_moderator)

        else:
            self.Listitem = self.driver.find_element(By.XPATH, self.list_item_guest_xpath)
            time.sleep(5)
            # self.Listitem.click()
            self.driver.execute_script("arguments[0].click();", self.Listitem)

    def SetManageOfVendor(self, value):
        drop = Select(self.driver.find_element(By.XPATH, self.manage_of_vendor))
        drop.select_by_visible_text(value)

    def SetGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.XPATH, self.male_gender_xpath).click()
        elif gender == 'Female':
            self.driver.find_element(By.XPATH, self.female_gender_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.male_gender_xpath).click()

    def SetFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.first_name_xpath).send_keys(fname)

    def SetLastName(self, lname):
        self.driver.find_element(By.XPATH, self.last_name_xpath).send_keys(lname)

    def SetDob(self, dob):
        self.driver.find_element(By.XPATH, self.date_picker_xpath).send_keys(dob)

    def SetCompanyName(self, companyname):
        self.driver.find_element(By.XPATH, self.company_name_xpath).send_keys(companyname)
        time.sleep(5)

    def Checkbox(self):
        self.driver.find_element(By.XPATH, self.is_tax_exempt_xpath).click()

    def NewsLetter(self):
        self.driver.find_element(By.XPATH, self.newsletter_xpath).click()

    def NewsLetterValue(self):
        self.driver.find_element(By.XPATH, self.newsletter_value_xpath).click()
        time.sleep(5)

    def SetAdminContent(self, content):
        self.driver.find_element(By.XPATH, self.admin_comment).send_keys(content)

    def ClickSaveButton(self):
        self.driver.find_element(By.XPATH, self.button_xpath).click()
