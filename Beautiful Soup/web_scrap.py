import requests
import bs4

import re
import csv
from datetime import datetime

index = []
trading_code = []
today_cp = []
yesterday_cp = []
time = []
tm = datetime.today().strftime('%Y-%m-%d')
row0 = ['Date', 'SL NO' , 'TRADING CODE', 'CLOSE PRICE',"YESTERDAY CLOSING PRICE"]
r = requests.get('https://www.dsebd.org/dse_close_price.php')
print(r)

soup = bs4.BeautifulSoup(r.text,"lxml")
x = soup.find(text=re.compile("^1JANATAMF"))
print(x)
t = soup.find_all('td')
cnt = 0
ck = 1
for i in t[828:3186]:
    if ck == 1:
        cnt += 1
        index.append(cnt)
        time.append(tm)
        ck +=1
    elif ck == 2:
        trading_code.append(i.text)
        ck += 1
    elif ck == 3:
        today_cp.append(i.text)
        ck += 1
    elif ck == 4:
        yesterday_cp.append(i.text)
        ck = 1
    #print(str("PIASH")+str(cnt))
    #print(i)

print(type(time))

rows = zip(time,index,trading_code,today_cp,yesterday_cp)

with open('August6.csv','w',encoding='utf-8',
          newline='') as csvfile:
    lw = csv.writer(csvfile)
    lw.writerow(row0)
    for item in rows:
        lw.writerow(item)