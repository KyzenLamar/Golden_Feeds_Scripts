import requests
#import requests_html
#from typing import Coroutine, TYPE_CHECKING
import bs4
import csv
import pprint

'''def linkChecker():
    file =open('m&s_broken_links.txt','w')
    file.close()

    #with open('m&s_links.csv',newline='') as f:
    file = open('m&s_links.txt','r')
    urls = file.readlines()
        #urls = csv.DictReader(f)
        #links = csv.reader(f)
        #links = links.strip()
    for row in urls:
        link = row.strip()
        s = requests.get(link)
        #print(link)

        b = bs4.BeautifulSoup(s.text, "html.parser")
        #p = b.find(text="cdn2.rcstatic.com")
        p = b.find(text ="Sorry, we can't")
        p1 = b.find(text="Internal Error")
        p2 = b.find(text="Please try again | M&S")
        #p = b.select('.italic')
        value = p
        value_error = p1
        value_error_2 = p2
        #print(p)
        if value == "Sorry, we can't" or value_error == "Internal Error" or value_error_2 == "Please try again | M&S":
            print('B')
            file = open('m&s_broken_links.txt','a')
            file.write(link+'\n')
            file.close
        else:
            print('Status OK')

linkChecker()'''




def linkChecker():
    file = open('broken_links_result.txt', 'w')
    file.close()

    #file = open('gucci_kr.txt', 'w')
    #file.close()

    file = open('deep_links_for_check.txt', 'r')
    urls = file.readlines()

    for row in urls:
        link = row.strip()
        s = requests.get(link)
        print(link)
        #print(s.history)
        #if s.status_code == 200:
        if s.history == '301': #and s.status_code == 200:
            print("OK")
            #file = open('gucci_kr.txt','a')
            #file.write(link+ '\n')
            #file.close
        else:
            print("Broken")
            file = open('m&s_broken_links.txt', 'a')
            file.write(link + '\n')
            file.close

linkChecker()




'''file = open('m&s_broken_links.txt', 'w')
file.close()

file = open('gucci_kr.txt', 'r')
urls = file.readlines()

for row in urls:
  #Cabforse
  #rowz = row[68:73].replace('_','')
  #Booking
  #rowz = row[72:77].replace('_', '')
  #Mozio
  #rowz = row[65:70].replace('_', '')
  #print(rowz)
  rowz = row[-8:]
  print(rowz)
  file = open('m&s_broken_links.txt', 'a')
  file.write(rowz)
  file.close'''

'''from PIL import Image

im = Image.open("Spa_Garden.jpg")
hight = 1000
width = 1000
img = im.resize((hight , width),Image.ANTIALIAS)
img.save("Spa_Garden_final.jpg")'''

