from bs4 import BeautifulSoup
import requests
import datetime

def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

d = datetime.datetime.today();
day = d.strftime('%B-%d')

url = "https://nationaltoday.com/"+day.lower()+"-holidays"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
rows = soup.find_all('table')[0].findChildren(['tr'])

dayList = []

for row in rows[1:]:
	dayList.append(strip_non_ascii(row.findAll('td')[1].text))

days = ', '.join(map(str, dayList))
print days