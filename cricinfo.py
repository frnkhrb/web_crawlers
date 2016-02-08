#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
from time import sleep

print ('Live Cricket Matches:')
print ('='*len('Live Cricket Matches:'))
url = "http://static.cricinfo.com/rss/livescores.xml"
sc = requests.get(url)
soup = BeautifulSoup(sc.text,'lxml')

i = 1
for data in soup.findAll('item'):
    print (str(i)+'. '+data.find('description').text)
    i += 1

list_links = []    
for link in soup.findAll('item'):
    list_links.append(link.find('guid').text)

while True:
    try:
        match_no = int(input('Enter match no : '))
    except ValueError:
        print ('Enter correct input')
        continue
    if match_no < 1 or match_no > len(list_links):
        print ('Enter correct input')
        continue
    else:
        break
        
url = list_links[match_no - 1]
sc = requests.get(url)
soup = BeautifulSoup(sc.text,'lxml')

for score in soup.findAll('title'):
    while True:
        print (score.text)
        sleep (60)
