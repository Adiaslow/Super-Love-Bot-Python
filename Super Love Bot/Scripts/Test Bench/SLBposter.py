from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class InstaBot:
    def __init__(self, username, pw):
        # open web driver
        self.driver = webdriver.Chrome("/Users/Adam/Downloads/chromedriver")
        sleep(2)
        # login
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        # username login
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')\
            .send_keys(username)
        # password login
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')\
            .send_keys(pw)
        # login click
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div')\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')\
            .click()
        sleep(2)
            

InstaBot('superlovebot','Peace005!')