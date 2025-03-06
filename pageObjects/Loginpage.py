from symtable import Class

from selenium import webdriver
from selenium.webdriver.common.by import By

class Login_page:
    txt_login_username_name="userName"
    txt_login_password_name="password"
    button_name="submit"

    def __init__(self,driver):
        self.driver=driver
    def setUserNames(self,username):
        self.driver.find_element(By.NAME,self.txt_login_username_name).clear()
        self.driver.find_element(By.NAME, self.txt_login_username_name).send_keys(username)
    def setPasswords(self,password):
        self.driver.find_element(By.NAME,self.txt_login_password_name).clear()
        self.driver.find_element(By.NAME, self.txt_login_password_name).send_keys(password)

    def ClickLoginPage(self):
        self.driver.find_element(By.NAME,self.button_name).click()

