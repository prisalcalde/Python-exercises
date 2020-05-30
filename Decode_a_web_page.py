# Use the BeautifulSoup and requests Python packages to print out a list of all the
# article titles on the Guardian homepage (https://www.theguardian.com/uk).

import requests
from bs4 import BeautifulSoup

url = "https://www.theguardian.com/uk"
content = requests.get(url)
soup = BeautifulSoup(content.text, "html.parser")
# print(soup)

# printing the website title
print(soup.title)

# The article titles are all on <span class="js-headline-text"></span>
article_titles = soup.find_all('span', class_="js-headline-text")

# Prints a list of article titles
print(article_titles)

# Prints each article title in a line
for article_title in article_titles:
    # print(article_title)  # prints the titles with the tags
    
    # extracts and prints only the titles without the tags
    print(article_title.text)
