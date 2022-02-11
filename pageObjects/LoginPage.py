"Ce fichier a pour objectif de pourvoir localiser les objects connexion & une classe qui permetra d'éffectuer la connexion"
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginmaPage:
    textbox_username_id = "username"
    textbox_password_id = "password"
    button_login_xpath = '//*[@id="customer_login"]/div[1]/form/p[3]/button'
    link_logout_xpath = '//*[@id="post-9"]/div/div/nav/ul/li[6]/a'
    
    def __init__(self, driver):
        self.driver = driver
    
    def setUsername(self, username):
        self.driver.find_element(By.ID,self.textbox_username_id).clear
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)
        
    def setPassword(self, password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)
        
    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()
        
    def clickLogout(self):
        self.driver.find_element(By.XPATH,self.link_logout_xpath).click()
        
        
        
        
