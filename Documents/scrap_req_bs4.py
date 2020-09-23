import requests
from bs4 import BeautifulSoup

page = requests.get('http://www.jeuxvideo.com/')
contents = page.content

soup = BeautifulSoup(contents, 'html.parser')
soup = soup.find_all('a')
print(soup)