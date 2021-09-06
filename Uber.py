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


driver.get("https://www.uber.com/ua/en/")
time.sleep(2)
ride = driver.find_element_by_xpath('//*[@id="1"]/div/div/span').click()
time.sleep(1)

with open('Uber_Check.csv','r',encoding='utf-8') as input:
    lines = list(csv.reader(input))
    #next(lines,None)
    input_pickup = driver.find_element_by_xpath('//*[@name="pickup"]')
    input_pickup.send_keys("Tenerife - Airport")
    time.sleep(2)
    input_pickup.send_keys(Keys.ENTER)

    for line in lines:

        input_dropoff = driver.find_element_by_xpath('//*[@name="destination"]')
        input_dropoff.send_keys(line)
        time.sleep(9)
        location_is_present = driver.find_elements_by_xpath('//*[@role="listbox"]//li')
        if location_is_present:
            print("OK")
            if len(location_is_present)== 1:
                for variants in location_is_present:
                    variant = variants.text
                    print(variant)
                    with open('Uber_result.csv', 'a') as outFile:
                        fieldnames = ['destination_location', 'status' , 'variation_location']
                        writer = csv.DictWriter(outFile, fieldnames=fieldnames)
                        writer.writerow({'destination_location': line, 'status': "okay",'variation_location': variant }) #'variation_location': variant
                        input_dropoff = driver.find_element_by_xpath('//*[@name="destination"]').clear()
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
                    with open('Uber_result.csv', 'a') as outFile:
                        fieldnames = ['destination_location', 'status' ,'variation_location']
                        writer = csv.DictWriter(outFile, fieldnames=fieldnames)
                        writer.writerow({'destination_location': line, 'status': "has variation", 'variation_location': variant})
                        input_dropoff = driver.find_element_by_xpath('//*[@name="destination"]').clear()
        else:
            with open('Uber_result.csv', 'a') as outFile:
                fieldnames = ['destination_location', 'status', 'variation_location']
                writer = csv.DictWriter(outFile, fieldnames=fieldnames)
                writer.writerow({'destination_location': line, 'status': "has variation", 'variation_location': "no variants"})
                input_dropoff = driver.find_element_by_xpath('//*[@name="destination"]').clear()
