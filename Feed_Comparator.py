import csv
import pandas as pd


with open('new.csv', 'r', encoding='utf-8') as t1, open('old.csv', 'r', encoding='utf-8') as t2:

    fileone = t1.readlines()   #,lineterminator='\r\n',quoting=csv.QUOTE_NONE)

    filetwo = t2.readlines()    #,lineterminator='\r\n',quoting=csv.QUOTE_NONE)


with open('update.csv', 'w',encoding='utf-8') as outFile:
    for line in filetwo:
        if line in fileone:

            write = outFile.write(line)



# with open('new.csv', 'r', encoding='utf-8') as file:
#     lines = list(csv.reader(file))
#     for line in lines:
#         for countrys in line:
#             country = countrys.split(',')
#         #line = line.split(',')
#             country = country[-2]
#             print(country)




