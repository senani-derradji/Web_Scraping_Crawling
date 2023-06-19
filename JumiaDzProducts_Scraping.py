import requests, sys
from bs4 import BeautifulSoup

PageNum, dictionary_products, Query = 0, {}, sys.argv[1]

while PageNum >=  0:
  url = f"https://www.jumia.dz/catalog/?q={Query.replace(' ', '+')}&page={PageNum}#catalog-listing"
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')
  all_products_of_one_page = soup.find_all('article', 
                                           class_="prd _fb col c-prd")

  if all_products_of_one_page:
    for product in all_products_of_one_page:
      info = product.find('a', class_="core").find('div', class_="info")
      link = product.find('a', class_="core")['href']
      title = info.find('h3', class_="name").text
      price = info.find('div', class_="prc").text
      image = product.find('a',
                           class_="core").find('div',
                                                    class_="img-c").find('img', 
                                                                         class_="img").get('data-src')
      if info and link and price and image:
        dictionary_products[title] = (price , image , f'https://www.jumia.dz{link}')
  else:
    break
  PageNum += 1
  
print("number of pages : ", PageNum-1)
print(len(dictionary_products),f' Product ')
