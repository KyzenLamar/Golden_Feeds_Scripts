# WORKING VERSION WITH NOMINATIUM
from geopy.geocoders import Nominatim
#from geopy.
geolocator = Nominatim(user_agent="user")
#location = geolocator.geocode("5805 Armada Dr, Carlsbad, CA 92008, USA")
location = geolocator.reverse("-29.45430946, 30.15353966")
print(location.address)

import csv, pandas
import pandas as pd


'''df= pd.read_csv('Booking_destinations_geo.csv', names=['rout_id','original_pickup_location','original_destination_location'],
                usecols=['rout_id','original_pickup_location','original_destination_location'])
rout_id = df['rout_id']
#print(rout_id[5])
original_pickup_location = df['original_pickup_location']
#print(original_pickup_location[7])
original_destination_location = df['original_destination_location']
#print(original_destination_location[12])

rout_id_list = pd.Series(list(rout_id))
original_pickup_location_list = pd.Series(list(original_pickup_location))
original_destination_location_list = pd.Series(list(original_destination_location))

#for rout in rout_id_list:
    #for pickup in original_pickup_location_list:
for destination in original_destination_location_list:
    #print(destination)
    try:
        geolocator = Nominatim(user_agent="user")
        location = geolocator.geocode(destination)
        result = (location.latitude, location.longitude)
        print(type(location))
        print(result)

        df = pandas.DataFrame(data={"rout_id": rout_id_list, "original_pickup_location": original_pickup_location_list,
                                    "original_destination_location": original_destination_location_list,
                                    "Result": result})
        df.to_csv('Booking_destinations_geo_result.csv',sep=',', index=False, header=True ,columns=None)
    except:
        result = 'None'

        df = pandas.DataFrame(data={"rout_id": rout_id_list, "original_pickup_location": original_pickup_location_list,
                                    "original_destination_location": original_destination_location_list,
                                    "Result": result})
        df.to_csv('Booking_destinations_geo_result.csv', sep=',', index=False, header=True, columns=None)'''

#################################

#VERSION WITH GOOGLE MAPS API KEYS

from geopy import geocoders

from geopy.geocoders import GoogleV3


google = GoogleV3(api_key='AIzaSyBhz63gAuF1DLQvblWlge--yFTiL0s_ync') #geocoding
#google = GoogleV3(api_key='AIzaSyA1wateckOO9di-Sq5t84fz6n_R8exC8lg') #places

# WITH CSV USING

'''inputAdress = open('Booking_destinations_geo.csv','r',encoding='utf-8')
fieldnames = ['rout_id', 'original_pickup_location' , 'original_destination_location']
#address = list(csv.reader(inputAdress))
address = csv.DictReader(inputAdress)
for rows in address:
    print(rows.items("original_destination_location"))
    #location = google.geocode(row['original_destination_location'],timeout=30)
    #print(location.raw)
    #print(location.address)
    print(len(rows['original_destination_location']))
    #print(rows)'''


# WITH PANDAS USING
'''inputAdress = pandas.read_csv('Booking_destinations_geo.csv',encoding='utf-8')
column = inputAdress.original_destination_location
#try:
for row in column:
    try:
        location = google.geocode(row, timeout=20,sensor=True)
        #location = google.reverse("7.4151886, 9.1168594")
        #print(location.raw)
        address = location.address

        print(location.address)
        #print(location.latitude , location.longitude)
        #fieldnames = ['Result']
        df = pandas.DataFrame(data={"": [address]})
        df.to_csv('Booking_destinations_geo_result2.csv',mode='a',index=False, header=True, columns=None)


            #df = pandas.DataFrame(data={"": ["Some Error happend"]})
            #df.to_csv('Booking_destinations_geo_result.csv',mode='a',index=False)
    except:
        print("Some Error happend")
        df = pandas.DataFrame(data={"": ["Some Error happend"]})
        df.to_csv('Booking_destinations_geo_result2.csv',mode='a',index=False)'''


