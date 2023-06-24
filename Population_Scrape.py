import requests
from bs4 import BeautifulSoup

url = "https://www.worldometers.info/world-population/population-by-country/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

table_head = soup.find('thead')
table_body = soup.find('tbody')

titles = []
for title in table_head.find_all('th'):
    titles.append(title.text)

rows_list = []

for row in table_body.find_all('tr'):
    cells_list = []
    rows = row.find_all('td')
    for cell in rows:
        cells_list.append(cell.text.strip())
    rows_list.append(cells_list)
