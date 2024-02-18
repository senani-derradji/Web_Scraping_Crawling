import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def create_dictionary_from_csv(csv_file_path):
    data_dict = {}
    try:
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                try:
                    fields = line.strip().split(',')
                    key = str(fields[6])
                    value = str(fields[5]).replace("-", "")
                    data_dict[key] = value
                except IndexError:
                    print(f"Error: Expected 12 fields in line {line_number}, saw {len(fields)}")
                    continue
    except FileNotFoundError:
        print(f"Error: File '{csv_file_path}' not found")
    return data_dict
def login_and_capture_screenshot(username, password):
    login_url = "https://progres.mesrs.dz/webfve/login.xhtml"
    target_url = "https://progres.mesrs.dz/webfve/pages/index.xhtml"

    driver = webdriver.Chrome()

    try:
        driver.get(login_url)
        username_field = driver.find_element(By.ID, "loginFrm:j_username")
        password_field = driver.find_element(By.ID, "loginFrm:j_password")
        username_field.send_keys(username)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
        driver.implicitly_wait(5)
        driver.get(target_url)
        nomphoto_view_element = driver.find_element(By.ID, 'j_idt32:nomphotoView')
        img_link = nomphoto_view_element.get_attribute("src")
        name_person = driver.find_element(By.CLASS_NAME, "welcome").text
        img_filename = f"ST Batna2 Bac 2020/{name_person}.png"
        driver.get(img_link)
        driver.save_screenshot(img_filename)
        print(f"Screenshot saved as: {img_filename}")
        driver.implicitly_wait(3)
        driver.get("https://progres.mesrs.dz/webfve/logout")
    except Exception as e:
        print("Error:", e)

csv_file_path = '2020.csv'
data_dict = create_dictionary_from_csv(csv_file_path)

for username, password in data_dict.items():
    login_and_capture_screenshot(username, password)