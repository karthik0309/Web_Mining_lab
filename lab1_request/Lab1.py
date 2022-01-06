import requests
from bs4 import BeautifulSoup
 
URL = "https://www.vit.ac.in/admissions/overview"
response = requests.get(URL,verify=False)

soup = BeautifulSoup(response.text, 'lxml') 

print(soup.prettify())


# python3 -m pip install lxml      