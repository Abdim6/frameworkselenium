from msilib.schema import Class
import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginmaPage

class Test_001_Login:
    baseURL = "http://demostore.supersqa.com/"
    username = "hldyqkqahohgaeg@gmail.com"
    passeword = "gHAEjjEABoAOMmI"
    
    def test_homePageTitle(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "My account – DemoStore":
            assert True
        else:
            assert False
    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginmaPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.passeword)
        self.lp.clickLogin()   
        act_title = self.driver.title
        self.driver.close()
        if act_title == "My account – DemoStore":
            assert True
        else:
            assert False
        
    
    