import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

file = open('test.txt', 'w')

tags = soup('a')
for tag in tags:
    file.write(tag.get('href', None))

file.close()