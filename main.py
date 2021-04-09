import requests
import urllib.request
from bs4 import BeautifulSoup
import json
import string
import time

mydict = {}
# list containing the final data

name = input()
# input value (case sensitive)

file_name = name[0]
# first character of the stock name
if file_name in string.ascii_uppercase:
    with open("F:/python projects/scrape/companyurl/" + file_name + ".json", "r") as f:
        data = json.load(f)
# if first letter is an alphabet
elif file_name not in string.ascii_lowercase:
    with open("F:/python projects/scrape/companyurl/others.json", "r") as f:
        data = json.load(f)

# if first letter is not an alphabet

url = data[0][name]
page = urllib.request.urlopen(url)
# headers={'cache-control': 'no-cache'}
# page.add_header('Pragma', 'no-cache')
time.sleep(5)
data = page.read()
soup = BeautifulSoup(data, 'html.parser')
option = soup.find('select', class_="graph-nav-tab").text.split('\n')
option.pop(0)
option.pop(-1)

#print(option)

if 'NSE' in option:
    nse = soup.find('div', id='inp_nse')
    nsep = nse.find('div', class_="inprice1 nsecp")
    if nsep is None:
        nsep = "Stock not traded in BSE for last 30 days."
        nse_change = "No data"
    elif nsep is not None:
        nsep = nsep.text
        nse_change = nse.find('div', id='nsechange')
        nse_change = nse_change.text
elif 'NSE' not in option:
    nsep = 'Not traded in NSE'
    nse_change = 'No data'

#print(nsep, nse_change)

if 'BSE' in option:
    bse = soup.find('div', id='inp_bse')
    bsep = bse.find('div', class_="inprice1 bsecp")
    if bsep is None:
        bsep = "Stock not traded in BSE for last 30 days."
        bse_change = "No data"
    elif bsep is not None:
        bsep = bsep.text
        bse_change = bse.find('div', class_='pricupdn bsechange grn')
        if bse_change is None:
            bse_change = bse.find('div', class_='pricupdn bsechange red')
            bse_change = bse_change.text
        elif bse_change is not None:
            bse_change = bse_change.text
elif 'BSE' not in option:
   bsep = 'Not traded in BSE'
   bse_change = 'No data'

#print(bsep, bse_change)


mydict["Stock Name"] = [name]
mydict["Exchange"] = [option]
mydict["nse price"] = [nsep]
mydict["nse change"] = [nse_change]
mydict["bse price"] = [bsep]
mydict["bse change"] = [bse_change]

print(mydict)






