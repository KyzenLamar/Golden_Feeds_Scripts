import requests
from PIL import Image
from io import BytesIO

def linkChecker():
    file =open('m&s_broken_links.txt','w')
    file.close()

    file = open('m&s_links.txt', 'r')
    urls = file.readlines()

    for row in urls:
        link = row.strip()
        s = requests.get(link)
        p = Image.open(BytesIO(s.content))
        widthheight = str(p.size)

        if (widthheight) == "(1000, 1000)":
            file = open('m&s_broken_links.txt', 'a')
            file.write(link + '\n')
            file.close
            #print('ОК')
            print('Less')

        else:
            print('Not ОК')
            #print('Less')
            #file = open('m&s_broken_links.txt', 'a')
            #file.write(link + '\n')
            #file.close

linkChecker()