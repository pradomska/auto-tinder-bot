from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from time import sleep
import random

MY_EMAIL = "example@gmail.pl"
MY_PASSWORD = "*********"

chrome_driver_path = "C:/Development/chromedriver.exe"

driver = webdriver.Chrome(service=Service(chrome_driver_path), options=webdriver.ChromeOptions())
driver.maximize_window()

url = "https://tinder.com"
driver.get(url)

sleep(3)
login_button = driver.find_element(By.XPATH, '//*[@id="s-407411262"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_button.click()
sleep(3)
fb_login = driver.find_element(By.XPATH, '//*[@id="s-2135792338"]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button')
fb_login.click()
sleep(3)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)
sleep(3)
fb_username = driver.find_element(By.XPATH, '//*[@id="email"]')
fb_username.send_keys(MY_EMAIL)
fb_passwd = driver.find_element(By.XPATH, '//*[@id="pass"]')
fb_passwd.send_keys(MY_PASSWORD)
fb_passwd.send_keys(Keys.ENTER)
sleep(5)
driver.switch_to.window(base_window)
print(driver.title)
sleep(5)

try:
    allow_location_button = driver.find_element(By.XPATH, '//*[@id="s-2135792338"]/main/div/div/div/div[3]/button[1]')
    allow_location_button.click()
    sleep(2)
except NoSuchElementException:
    print("No button, skipped...")

try:
    notifications_button = driver.find_element(By.XPATH, '//*[@id="s-2135792338"]/main/div/div/div/div[3]/button[1]')
    notifications_button.click()
    sleep(2)
except NoSuchElementException:
    print("No button, skipped...")

try:
    cookies = driver.find_element(By.XPATH, '//*[@id="s-407411262"]/div/div[2]/div/div/div[1]/div[1]/button')
    cookies.click()
    sleep(2)
except NoSuchElementException:
    print("No button, skipped...")

for n in range(100):
    sleep(2)
    try:
        print("swipe")
        path_list = ['//*[@id="s-407411262"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button',
                     '//*[@id="s-407411262"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[2]/button']

        like_button = driver.find_element(By.XPATH, random.choice(path_list))
        like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            sleep(2)

driver.quit()
