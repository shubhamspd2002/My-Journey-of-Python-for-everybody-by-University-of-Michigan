#you can run this code in jupyter notebook. else you can create a virtual environment in VS code. follow the steps in this link
#https://www.youtube.com/watch?v=ThU13tikHQw

#pip install beautifulsoup4 #[this you have to type in the terminal window after creating a virtual enironment (venv)]
#u can just put pip install (package name) in the terminal window and your work is done

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('enter - ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

#retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))