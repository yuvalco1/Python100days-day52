from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import threading
from time import sleep
import os

from dotenv import load_dotenv

class InstaFollower:
    def __init__(self):
        # .env file contains api keys in the format of API_KEY="xxxxxx", get it using os.environ['API_KEY']; before that pip install python-dotenv
        load_dotenv()  # take environment variables from .env.

        # self.PROMISED_UP = 10
        # self.PROMISED_DOWN = 100
        self.my_email = os.environ['MY_EMAIL']
        self.my_password = os.environ['INSTA_PASS']

        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def login(self):
        url = "https://www.instagram.com/"
        self.driver.get(url)
        sleep(2)
        email_input = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
        email_input.send_keys(self.my_email)
        password_input = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
        password_input.send_keys(self.my_password)
        login_button = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]')
        login_button.click()
        sleep(5)
        not_save_login_info = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')
        not_save_login_info.click()
        sleep(1)
        turn_off_notifications = self.driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        turn_off_notifications.click()
        sleep(1)
        # Hint from instructor to find button with text - button = driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Click me')]")


    def find_followers(self):
        sleep(2)
        profile_btn = self.driver.find_element(By.XPATH,value="//span[contains(text(), 'Profile')]")
        profile_btn.click()
        sleep(2)
        follwing_btn = self.driver.find_element(By.XPATH,value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a')
        follwing_btn.click()
        sleep(2)
        first_following = self.driver.find_element(By.XPATH,value="//span[contains(text(), 'danaxcohen')]")
        first_following.click()
        sleep(2)
        first_following_following = self.driver.find_element(By.XPATH,value='/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a')
        first_following_following.click()
        sleep(3)


    def follow(self):
        i=0
        following_btns = self.driver.find_elements(By.CSS_SELECTOR,value='button')
        print(len(following_btns))
        for btn in following_btns:
            print(btn.text)
            sleep(1)
            if btn.text == 'Follow':
                btn.click()
                sleep(2)
                i+=1
                if i==5:
                    break


