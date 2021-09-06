from xmlutils.xml2csv import xml2csv

'''converter = xml2csv("huawei_akakce.xml", "huawei_akakce.csv", encoding="utf-8")
converter.convert(delimiter=",")'''

'''import csv
import xml.etree.ElementTree as ET

tree = ET.parse('huawei_akakce.xml')
root = tree.getroot()
with open('huawei_akakce.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile,root, quotechar='|',
                        quoting=csv.QUOTE_MINIMAL)'''



from xml.dom import minidom

xmldoc = minidom.parse('sitemap.xml')
linklist = xmldoc.getElementsByTagName('loc')
print(linklist)
for link in linklist:
    print(link.firstChild.nodeValue)#.replace('casas-rurales','casa-rural'))


import csv
from datetime import date, timedelta


# with open('fake_rates.csv', 'a') as outFile:
#     fieldnames = ['Checkin', 'Nights', 'Property', 'BaseRate', 'Tax', 'OtherFees', 'Flexible', 'OccupiedRooms','BarLevel']
#     writer = csv.DictWriter(outFile, fieldnames=fieldnames)
#     writer.writeheader()
#
#
# with open('property_list.csv','r',encoding='utf-8') as input:
#     property_list = list(csv.reader(input))
#
#     for hotels in property_list:
#         print(hotels)
#
#         start_date = date(2020, 5, 21)
#         end_date = date(2020, 6, 5)
#         delta = timedelta(days=1)
#         days = 9
#
#         while start_date <= end_date:
#             print(start_date.strftime("%m-%d-%Y"))
#             start_date += delta
#
#             for day in range(0,9):
#                 day += 1
#                 print (day)
#
#
#                 with open('fake_rates.csv', 'a') as outFile:
#                     writer = csv.DictWriter(outFile, fieldnames=fieldnames)
#                     writer.writerow({'Checkin': start_date.strftime("%m-%d-%Y"), 'Nights': day, 'Property': hotels, 'BaseRate': "-1",'Tax':"",'OtherFees':"",'Flexible':"-1",'OccupiedRooms':"",'BarLevel':"78"})
#                         #hotels += 1


'''word = 'UUUURGGGEEEEENT'
result = ''.join(sorted(set(word), key=word.index))
print (result)'''