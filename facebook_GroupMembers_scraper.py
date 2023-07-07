import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
# from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("https://facebook.com")
email = driver.find_element(By.ID, 'email').send_keys("email")
password = driver.find_element(By.ID, 'pass').send_keys("password")
button = driver.find_element(By.TAG_NAME, "button").click()
time.sleep(2)
driver.get("https://web.facebook.com/groups/....")
time.sleep(1)
arr_data = []
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    elements = driver.find_elements(
        By.XPATH, 
        "//span[@class='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xk50ysn xzsf02u x1yc453h']")
    for element in elements:
        link = element.find_element(By.TAG_NAME, "a")
        if link.get_attribute("href") not in arr_data:
            arr_data.append(link.get_attribute("href"))            
            dicty[link.text] = link.get_attribute("href")[53:]
