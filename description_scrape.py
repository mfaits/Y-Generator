import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

# specify the url
company_page = 'https://www.ycombinator.com/companies/'

# YC page loads table with a javascript call so access it using selenium
# browser instead of loading it straight into soup
browser = webdriver.Chrome()
browser.get(company_page)

# returns the inner HTML as a string and gives it to soup
innerHTML = browser.execute_script("return document.body.innerHTML") 
soup = BeautifulSoup(innerHTML)

table = soup.table
table_rows = table.find_all('tr')

descriptions = []

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    descriptions.append(row[2])

df_descriptions = pd.DataFrame(descriptions)

df_descriptions.to_csv('Data\\company_descriptions.csv',
                        header=False,
                        index=False)