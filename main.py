from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

IG_USERNAME = os.getenv('IG_USERNAME')
IG_PASSWORD = os.getenv('IG_PASSWORD')
WEBDRIVER_PATH = os.getenv('WEBDRIVER_PATH')

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

print('Usuario de instagram: ')
account_to_scrape = str(input())

driver = webdriver.Chrome(WEBDRIVER_PATH, chrome_options=options)

driver.set_window_position(5,0)
driver.maximize_window()
time.sleep(1)

driver.get('https://instagram.com')

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')))\
    .send_keys(IG_USERNAME)

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')))\
    .send_keys(IG_PASSWORD)
    
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.sqdOP.L3NKy.y3zKF')))\
    .click()

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/button')))\

driver.get('https://instagram.com/%s' % account_to_scrape) 

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.-nal3')))\
    .click()

time.sleep(1)

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.isgrP')))\

followers_list = driver.find_element_by_css_selector('div.isgrP')


SCROLL_PAUSE_TIME = 0.5

last_height = driver.execute_script("return arguments[0].scrollHeight", followers_list)

while True:
    driver.execute_script("arguments[0].scrollBy(0,arguments[0].scrollHeight)", followers_list) 

    time.sleep(SCROLL_PAUSE_TIME)

    new_height = driver.execute_script("return arguments[0].scrollHeight", followers_list)
    if new_height == last_height:
        break
    last_height = new_height


text = followers_list.text

def fnMap(item):
    return item.split("\n")[0]

arr = map(fnMap, text.split("Eliminar\n"))
print(list(arr))