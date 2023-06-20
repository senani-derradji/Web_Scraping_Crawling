import requests
from bs4 import BeautifulSoup

response = requests.get("https://weather.com/weather/tenday/l/f2530b22dc823cf0e2ee317dbd4c6b8574ef34408f0b496f56975a942c57ba33#detailIndex5")
sp = BeautifulSoup(response.content, 'html.parser')

dict = {}
div_gn = sp.find("div", class_="DailyForecast--DisclosureList--nosQS")
details = div_gn.find_all('details', class_="DaypartDetails--DayPartDetail--2XOOV Disclosure--themeList--1Dz21")
for dt in details:
    inside = dt.find('div', class_="DetailsSummary--DetailsSummary--1DqhO DetailsSummary--fadeOnOpen--KnNyF")
    day = inside.find('h3').text
    temperature = inside.find('div', class_="DetailsSummary--temperature--1kVVp").text
    cond = inside.find('div', class_="DetailsSummary--condition--2JmHb").find('span').text
    rain = inside.find('div',class_="DetailsSummary--wind--1tv7t DetailsSummary--extendedData--307Ax").find('span').text
    dict[day] = (temperature, cond, rain)
location = sp.find('h1', class_='LocationPageTitle--PageHeader--JBu5- DailyForecast--CardHeader--3ATQ0')
print(f"Location : {location.get_text()[15:]}")
# print(f"{time.text} -- {location.text}")
for day, (tmp , con , rain) in dict.items():
    print(f"-- {day} -- {tmp} -- {con} -- {rain} --")
