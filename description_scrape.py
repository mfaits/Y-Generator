import requests
from bs4 import BeautifulSoup

# specify the url
company_page = 'https://www.ycombinator.com/companies/'

# query the website and return the html to the variable ‘page’
page = requests.get(company_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page.text, 'html.parser')