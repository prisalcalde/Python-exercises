# Take the code from the 'How To Decode A Website' exercise, and instead
# of printing the results to a screen, write the results to a txt file.
# In your code, just make up a name for the file you are saving to.

# Extras:
# Ask the user to specify the name of the output file that will be saved.

# Code from 'How to Decode a Website' exercise:
import requests
from bs4 import BeautifulSoup

url = "https://www.theguardian.com/uk"
content = requests.get(url)
soup = BeautifulSoup(content.text, "html.parser")

# The article titles are all on <a href="" class="js-headline-text"></a>
article_titles = soup.find_all('a', class_="js-headline-text")

# 1. Writing today's headlines on todays_news.txt file
with open('todays_news.txt', 'w') as file:
    for article_title in article_titles:
        file.write(str(article_title.text))

# 2. Asking the user to specify the name of the output file that will be saved
user_file = input("What's the name of the file that you want to save today's news? \n")

with open(user_file, 'w') as file:
    for article_title in article_titles:
        file.write(str(article_title.text))
