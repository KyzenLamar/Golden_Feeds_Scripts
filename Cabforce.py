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


driver.get("https://www.cabforce.com/en#/search")
time.sleep(2)



# WORKING VERSION
with open('Cabforse_addres.csv','r',encoding='utf-8') as input:
    lines = list(csv.reader(input))

    # This part for changing airport each time in loop # START
    for line in lines:
        pickup = line[0]
        destination = line[1]
        #print(pickup)
        #FINISH
        time.sleep(3)
        oneWayClick = driver.find_element_by_xpath('//*[@ng-bind="labelOneWay"]').click()
        input_pickup = driver.find_element_by_xpath('//*[@id="input-pickup"]')
        input_pickup.send_keys(pickup)
        time.sleep(2)
        airport = driver.find_element_by_xpath('//*[@id="item-0-0"]').click()

    # Loop for iteration only with destination.Uncomment and move code below to right once.

    #for line in lines:

        input_dropoff = driver.find_element_by_xpath('//*[@id="input-dropoff"]')
        input_dropoff.send_keys(destination)
        time.sleep(7)
        location_is_present = driver.find_elements_by_xpath('//*[@id="ct-dropoff-select"]/div[2]/div/div/div[1]/div[2]/ul/li')
        if location_is_present:
            print("OK")
            if len(location_is_present)== 1:
                for variants in location_is_present:
                    variant = variants.text.replace("Location","")
                    print(variant)
                    with open('Cabforse_result.csv', 'a') as outFile:
                        fieldnames = ['destination_location', 'status' , 'variation_location']
                        writer = csv.DictWriter(outFile, fieldnames=fieldnames)
                        writer.writerow({'destination_location': line, 'status': "okay",'variation_location': variant }) #'variation_location': variant
                        input_dropoff = driver.find_element_by_xpath('//*[@id="input-dropoff"]').clear()
        #else:
            #input_dropoff = driver.find_element_by_xpath('//*[@id="dropoffLocation"]').clear()

        #for variants in location_is_present:
            #print(variants.text)
            #input_dropoff = driver.find_element_by_xpath('//*[@id="dropoffLocation"]').clear()
            else:
                for variants in location_is_present:
                    variant = variants.text

                    print("shit")
                    with open('Cabforse_result.csv', 'a') as outFile:
                        fieldnames = ['destination_location', 'status' ,'variation_location']
                        writer = csv.DictWriter(outFile, fieldnames=fieldnames)
                        writer.writerow({'destination_location': line, 'status': "has variation", 'variation_location': variant})
                        input_dropoff = driver.find_element_by_xpath('//*[@id="input-dropoff"]').clear()
        else:
            with open('Cabforse_result.csv', 'a') as outFile:
                fieldnames = ['destination_location', 'status', 'variation_location']
                writer = csv.DictWriter(outFile, fieldnames=fieldnames)
                writer.writerow({'destination_location': line, 'status': "has variation", 'variation_location': "no variants"})
                input_dropoff = driver.find_element_by_xpath('//*[@id="input-dropoff"]').clear()



