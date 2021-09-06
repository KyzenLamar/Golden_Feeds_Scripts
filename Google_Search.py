'''from googlesearch.googlesearch import GoogleSearch
import urllib.request

import pandas

inputAddres = pandas.read_csv('Google_Search.csv', encoding='utf-8')

#Google = urllib.request.urlopen("http://google.com")
for row in inputAddres:

    query = GoogleSearch().search(row)
    for result in query.results:#(query,
                         #tld = 'com',
                         #lang = 'en',
                         #num = 5,
                         #start= 0,
                         #stop = 5,
                         #pause=  3.0,):
        print(result.title)'''

#import pandas as pd
import time
import csv, pandas
import requests
from bs4 import BeautifulSoup

headers_Get = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }

#def google():
inputAdress = open('Google_Search.csv', encoding='utf-8')
colomn = (inputAdress.readlines())
#print(colomn)
for row in colomn:
    addres = row
    row += ' hotel'

    s = requests.Session()
    q = '+'.join(row.split())
    #print(q)
    url = 'https://www.google.com/search?q=' + q + '&ie=utf-8&oe=utf-8'
    time.sleep(2)
    r = s.get(url, headers=headers_Get)
    time.sleep(2)

    soup = BeautifulSoup(r.text, "html.parser")
    #output = []
    try:

        #for searchWrapper in soup.find_all('h2',{'data-attrid':'title'}):
        #for searchWrapper in soup.find_all('div.xpdopen h2 span'):
        for searchWrapper in soup.find_all('div',{"class":"xpdopen"}): # h2 span'):

            '''try:
                search = searchWrapper.find('span')
                final_res = str(search)'''
            search = searchWrapper.find_all('h2')
            result = search.find('span')
            final_res = str(result)

        with open('Google_result.csv', 'a') as file:
            fieldnames = ['Result']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'Result': final_res +','+ addres})

            print(final_res + ','+ addres)
            '''except:
                with open('Google_result.csv', 'a') as file:
                    fieldnames = ['Result']
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    writer.writerow({'Result': " Not Found"+ ','+ addres})
                    print('Not Found!')'''
    except:
        with open('Google_result.csv', 'a') as file:
            fieldnames = ['Result']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerow({'Result': " Not Found" + ','+ addres})
            print('Not Found!')
        #print(searchWrapper)'''

        #url = searchWrapper.find('a')["href"]
        #text = searchWrapper.find('span').text.strip()
        #result = {'text': text}
        #output.append(result)
    #return output

#google()

