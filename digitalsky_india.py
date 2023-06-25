from selenium import webdriver
from selenium.webdriver.common.by import By
import time, csv

driver = webdriver.Chrome()

driver.get("https://digitalsky.dgca.gov.in/remote_pilots")
time.sleep(3)

table = driver.find_element(By.XPATH, "//table[@class='table table-striped']")
columns_titles = table.find_element(By.XPATH, "//tr[@class='header row-color']").find_elements(By.TAG_NAME, "th")

columns = []
for Column in columns_titles:
    columns.append(Column.text)

R_General = []

def extract_row_data(row):
    cells = row.find_elements(By.TAG_NAME, "td")
    return [cell.text for cell in cells]

for _ in range(1, 101):
    
    time.sleep(2.5)
    
    table = driver.find_element(By.XPATH, "//table[@class='table table-striped']")
    Rows = table.find_elements(By.XPATH, "//tr[@class='row-color']")
    
    R_General.extend([extract_row_data(row) for row in Rows])
    
    time.sleep(1)
    
    page = driver.find_element(By.XPATH, "//div[@class='pagination mb-10']")
    next_page_link = page.find_element(By.XPATH, '//li[@class="page-item"]/a[@aria-label="Next"]')
    next_page_link.click()

output_file = 'output.csv'

with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(columns)
    writer.writerows(R_General)

print(f"CSV file '{output_file}' has been created successfully.")
