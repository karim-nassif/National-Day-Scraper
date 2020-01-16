from bs4 import BeautifulSoup
import requests
import datetime

d = datetime.datetime.today();
day = '1'
month = d.strftime('%B')

url = "https://nationaltoday.com/"+month.lower()+"-"+day+"-holidays"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
rows = soup.find_all('table')[0].findChildren(['tr'])

dayList = []

for row in rows[1:]:
	dayList.append(row.findAll('td')[1].text)

days = ', '.join(map(str, dayList))
print days

