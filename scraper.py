import requests
from bs4 import BeautifulSoup
import string
import json
total_list = {}

for c in string.ascii_lowercase:
    mlink = 'https://www.moneycontrol.com/india/stockpricequote/' + c
    page = requests.get(mlink)
    soup = BeautifulSoup(page.content, 'html.parser')
    links = soup.find('table', class_="pcq_tbl MT10")
    for a in links.find_all('a', href=True):
        total_list[a.text] = a['href']
    with open(f'companyurl/{c}.json', 'w') as f:
        json.dump([total_list], f)
    print(f'File Saved: {c}')
    total_list ={}






