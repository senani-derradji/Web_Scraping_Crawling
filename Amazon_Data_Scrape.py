import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

dictionary_data = {'titles': [], 'prices': [], 'images': []}
query = "pc gamer"
for pg in range(1, 101):
    
    driver.get(f'https://www.amazon.com/s?k={query.replace(" ","+")}&page={pg}&ref=sr_pg_{pg}')
    page = driver.find_element(By.XPATH, '//div[@class="s-main-slot s-result-list s-search-results sg-row"]')
    products = page.find_elements(By.XPATH, '//div[@class="sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 AdHolder sg-col s-widget-spacing-small sg-col-4-of-20"]')

    driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
    time.sleep(1.5)

    titles = page.find_elements(By.XPATH, "//h2[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-4']")
    prices = page.find_elements(By.XPATH, "//a[@class='a-size-base a-link-normal s-no-hover s-underline-text s-underline-link-text s-link-style a-text-normal']")
    images_link = page.find_elements(By.XPATH, "//img[@class='s-image']")

    for title, price, image_link in zip(titles, prices, images_link):
        dictionary_data['titles'].append(title.text)
        dictionary_data['prices'].append(price.find_element(By.CLASS_NAME, "a-price").text.strip().replace('\n', '.'))
        dictionary_data['images'].append(image_link.get_attribute('src'))
    print(dictionary_data)
driver.quit()
