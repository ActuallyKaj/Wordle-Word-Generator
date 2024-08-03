# Wordle Word Generator
# 04/08/24
# V1.1: Trying to convert html data to string and seperate  words - not working

import requests
from bs4 import BeautifulSoup

# Making a GET request
r = requests.get('https://byjus.com/english/5-letter-words/')

# check status code for response received
# success code - 200
print(r)

# print content of request
#print(r.content)

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
soup = str(soup)
soup = [soup].split()
