import pandas as pd
import plotly.express as px

df = pd.read_csv('BookingGO_raw_data_qa_Graph.csv',usecols=['pickup_date','Booking_price'],encoding='utf-8')

fig = px.bar(df,x= 'pickup_date' , y= 'Booking_price', title = 'Booking Price Graphic')
fig.show()


import csv


file = open('.csv', 'r', encoding='utf-8')
fullAddress = dict(csv.reader(file))

fileTwo = open('.csv', 'r', encoding='utf-8')
finedAddress = dict(csv.reader(fileTwo))

