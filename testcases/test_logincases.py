from selenium import webdriver

import pytest

from pageObjects.Loginpage import Login_page

from utilities.readConfigData import ReadConfig
from utilities import customLogger
from utilities import readUtilis

class Test_Login_01:
    base_Url = ReadConfig.getcommonData("commonData", "base_Url")
  # hardcoded values we should not user in automation
    username =ReadConfig.getcommonData("commonData","username")
    Password = ReadConfig.getcommonData("commonData","Password")
    logger=customLogger.get_logger("login page")
    path=".\\Testdata\\loginData.xlsx"

    @pytest.mark.sanity
    @pytest.mark.smoke
    def test_home_page_validation(self,setup):

        self.logger.info("********** verifiy home page**************")
        self.driver=setup
        self.driver.get(self.base_Url)
        title=self.driver.title
        self.logger.info("**********getting tile*****"+ title)
        if title=="Welcome: Mercury Tours":
            self.driver.save_screenshot(".\\Screenshots\\home_page.png")
            self.logger.info("******** successfull title********")
            assert True
        else:
            self.logger.info("********failed test cases*********")
            self.driver.save_screenshot(".\\Screenshots\\home_page_failed1.png")
            assert False
        self.driver.close()
    @pytest.mark.regression
    def test_login_page_validation(self,setup):
        self.logger.info("*******verfiy login page**********")
        self.driver=setup
        self.driver.get(self.base_Url)
        self.lp=Login_page(self.driver)
        self.lp.setUserNames(self.username)
        self.lp.setPasswords(self.Password)
        self.lp.ClickLoginPage()
        title=self.driver.title
        self.logger.info("***********getting login page title********")
        if title=="Login: Mercury Tours":
            self.logger.info("*********successfull login page title*********")
            self.driver.save_screenshot(".\\Screenshots\\login_page.png")
            assert True
        else:
            self.logger.info("*************failed login page title**************")
            self.driver.save_screenshot(".\\Screenshots\\login_page_failed1.png")
            assert False
        self.driver.close()
    @pytest.mark.smoke
    def test_Excel_page_validation(self, setup):
        row_count = readUtilis.getRowCount(self.path, "Sheet1")  # row_count is an integer
        list_status = []

        for r in range(2, row_count + 1):  # Use row_count instead of row
            username = readUtilis.readData(self.path, "Sheet1", r, 1)  # Corrected call
            password = readUtilis.readData(self.path, "Sheet1", r, 2)  # Corrected call
            result = readUtilis.readData(self.path, "Sheet1", r, 3)  # Corrected call

            self.logger.info("******* Verifying login page **********")
            self.driver = setup
            self.driver.get(self.base_Url)
            self.lp = Login_page(self.driver)
            self.lp.setUserNames(username)
            self.lp.setPasswords(password)
            self.lp.ClickLoginPage()

            title = self.driver.title
            self.logger.info("*********** Getting login page title ********")

            if title == "Login: Mercury Tours":
                if result == "pass":
                    self.logger.info("********* Successfully logged in *********")
                    self.driver.save_screenshot(".\\Screenshots\\login_page.png")
                    list_status.append("pass")
                elif result == "fail":
                    self.logger.info("************* Failed login **************")
                    self.driver.save_screenshot(".\\Screenshots\\login_page_failed1.png")
                    list_status.append("fail")



            elif title!="Login: Mercury Tours":
                if result=="pass":
                    self.logger.info("*********successfull login page title*********")
                    self.driver.save_screenshot(".\\Screenshots\\login_page.png")
                    list_status.append("pass")
                elif result=="fail":
                    self.logger.info("*************failed login page title**************")
                    self.driver.save_screenshot(".\\Screenshots\\login_page_failed1.png")
                    list_status.append("fail")

            if "fail" not in list_status:
                self.logger.info("login is pass")
                assert True
            else:
                self.logger.info("login is fail")
                assert False






