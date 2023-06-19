from selenium.webdriver.common.by import By


class SearchCustomer:
    # add customer page
    email_xpath = "//input[@name='SearchEmail']"
    first_name_xpath = "//input[@name='SearchFirstName']"
    last_name_xpath = "//input[@name='SearchLastName']"
    search_button_xpath = "//button[@id='search-customers']"
    tab_search_results_xpath = "//table[@role='grid']"
    table_xpath = "//table[@id='customers-grid']"
    table_rows_xpath = "//table[@id='customers-grid']//tbody//tr"
    table_columns_xpath = "//table[@id='customers-grid']//tbody//tr"

    def __init__(self, driver):
        self.driver = driver

    def SetEmail(self, email):
        self.driver.find_element(By.XPATH, self.email_xpath).clear()
        self.driver.find_element(By.XPATH, self.email_xpath).send_keys(email)

    def SetFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.email_xpath).clear()
        self.driver.find_element(By.XPATH, self.first_name_xpath).send_keys(fname)

    def SetLastName(self, lname):
        self.driver.find_element(By.XPATH, self.email_xpath).clear()
        self.driver.find_element(By.XPATH, self.last_name_xpath).send_keys(lname)

    def ClickSearch(self):
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()

    def getNoofRows(self):
        return len(self.driver.find_element(By.XPATH, self.table_rows_xpath))

    def getNoofColumn(self):
        return len(self.driver.find_element(By.XPATH, self.table_columns_xpath))

    def SearchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoofRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            emailid = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def SearchCustomerByName(self, Name):
        flag = False
        for r in range(1, self.getNoofRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            name = table.find_element(By.XPATH, "//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag
