import requests
import bs4
import csv
from datetime import datetime
import urllib.request as ur
import urllib.error
import pandas as pd
import os
import sys


if getattr(sys, 'frozen', False):
    path = os.path.join(sys._MEIPASS, "Company_Name.csv")
    df = pd.read_csv(path)
else:
    df = pd.read_csv('Company_Name.csv')


c_name = []
for i in df[' TRADING CODE']:
    c_name.append(i)

tm = datetime.today().strftime('%Y-%m-%d')
row0 = ['SL NO' ,'Date', 'TRADING CODE', 'July Update Status']
sl = []
date = []
trading_code = []
July_update = []
idx = 0
l = len(c_name)
print("Please wait")
print("Connecting to internet...")
while l!=0:

    print(c_name[idx])
    url = ('https://www.dsebd.org/displayCompany.php?name=' + str(c_name[idx]))
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.text, "lxml")
    try:
        result = ur.urlopen(url)
    except urllib.error.HTTPError as e:
        print("ERROR")
    except requests.exceptions.InvalidURL:
        print("ERROR")



    table = soup.find_all('table', id='company')
    x = table[23:24]
    value = []
    for i in x:
        value.append((i.text))

    value = [w.replace("\r", "") for w in value]
    value = [w.replace("\t", "") for w in value]
    value = [w.replace("\n", "") for w in value]

    value = str(value)
    if "Jul" in value:
        sl.append(idx+1)
        date.append(tm)
        trading_code.append(c_name[idx])
        July_update.append("YES")
    else:
        sl.append(idx + 1)
        date.append(tm)
        trading_code.append(c_name[idx])
        July_update.append("NO")

    idx += 1
    l -= 1


rows = zip(sl,date,trading_code,July_update)
with open('July_Update.csv','w',encoding='utf-8',
          newline='') as csvfile:
    lw = csv.writer(csvfile)
    lw.writerow(row0)
    for item in rows:
        lw.writerow(item)


