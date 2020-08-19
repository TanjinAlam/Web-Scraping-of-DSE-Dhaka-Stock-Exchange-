from datetime import datetime
import csv
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options,executable_path='chromedriver.exe')  # see edit for recent code change.
d1 = '01/01/2020'
d2 = '08/11/2020'
cname = 'CITYBANK'
path = "chromedriver.exe"
driver.implicitly_wait(4)

b = False
while(b==True):

    try:
        driver.get("https://www.dsebd.org/displayCompany.php?name=1JANATAMF")
        x = driver.find_element_by_xpath(
            '/html/body/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table[11]/tbody')
        value = x.text
        print(value)

    except:
        print("An exception occurred")
        b=False
        break