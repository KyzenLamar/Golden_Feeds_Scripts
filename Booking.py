from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import requests
import bs4
import csv
import time

chrome_options = Options()
#chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.set_window_size(1440, 1440)


driver.get("https://taxi.booking.com/")
time.sleep(2)

with open('Booking_Check.csv','r',encoding='utf-8') as input:
    lines = list(csv.reader(input))
    #next(lines,None)
    input_pickup = driver.find_element_by_xpath('//*[@id="pickupLocation"]')
    input_pickup.send_keys("SYX")
    time.sleep(2)
    input_pickup.send_keys(Keys.ENTER)

    for line in lines:

        input_dropoff = driver.find_element_by_xpath('//*[@id="dropoffLocation"]')
        input_dropoff.send_keys(line)
        time.sleep(9)
        location_is_present = driver.find_elements_by_xpath('//*[@id="dropoffLocation-items"]/li/button/div')
        if location_is_present:
            print("OK")
            if len(location_is_present)== 1:
                for variants in location_is_present:
                    variant = variants.text
                    print(variant)
                    with open('Booking_result.csv', 'a') as outFile:
                        fieldnames = ['destination_location', 'status' , 'variation_location']
                        writer = csv.DictWriter(outFile, fieldnames=fieldnames)
                        writer.writerow({'destination_location': line, 'status': "okay",'variation_location': variant }) #'variation_location': variant
                        input_dropoff = driver.find_element_by_xpath('//*[@id="dropoffLocation"]').clear()
        #else:
            #input_dropoff = driver.find_element_by_xpath('//*[@id="dropoffLocation"]').clear()

        #for variants in location_is_present:
            #print(variants.text)
            #input_dropoff = driver.find_element_by_xpath('//*[@id="dropoffLocation"]').clear()
            else:
                for variants in location_is_present:
                    variant = variants.text
                    #input_dropoff = driver.find_element_by_xpath('//*[@id="dropoffLocation"]').clear()
                    print("shit")
                    with open('Booking_result.csv', 'a') as outFile:
                        fieldnames = ['destination_location', 'status' ,'variation_location']
                        writer = csv.DictWriter(outFile, fieldnames=fieldnames)
                        writer.writerow({'destination_location': line, 'status': "has variation", 'variation_location': variant})
                        input_dropoff = driver.find_element_by_xpath('//*[@id="dropoffLocation"]').clear()
        else:
            with open('Booking_result.csv', 'a') as outFile:
                fieldnames = ['destination_location', 'status', 'variation_location']
                writer = csv.DictWriter(outFile, fieldnames=fieldnames)
                writer.writerow({'destination_location': line, 'status': "has variation", 'variation_location': "no variants"})
                input_dropoff = driver.find_element_by_xpath('//*[@id="dropoffLocation"]').clear()
