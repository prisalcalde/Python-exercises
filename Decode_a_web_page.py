# Use the BeautifulSoup and requests Python packages to print out a list of all the
# article titles on the Guardian homepage (https://www.theguardian.com/uk).

import requests
from bs4 import BeautifulSoup

url = "https://www.theguardian.com/uk"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
print(soup)
