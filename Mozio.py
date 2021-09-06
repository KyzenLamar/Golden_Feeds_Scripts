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


driver.get("https://www.mozio.com/en-us")
time.sleep(2)

with open('Mozio_Check.csv','r',encoding='utf-8') as input:
    lines = list(csv.reader(input))
    #next(lines,None)
    input_pickup = driver.find_element_by_xpath('//*[@id="start_address"]')
    input_pickup.send_keys("VLC airport")
    time.sleep(2)
    input_pickup.send_keys(Keys.ENTER)
    for line in lines:

        input_dropoff = driver.find_element_by_xpath('//*[@id="end_address"]')
        input_dropoff.send_keys(line)
        time.sleep(4)
        location_is_present = driver.find_elements_by_xpath('//*[@x-placement="bottom"]')
        if location_is_present:
            print("OK")
            print(len(location_is_present))
            if len(location_is_present)== 1:
                with open('Mozio_result.csv', 'a') as outFile:
                    fieldnames = ['destination_location', 'status']
                    writer = csv.DictWriter(outFile, fieldnames=fieldnames)
                    writer.writerow({'destination_location': line, 'status': "okay"})

            for variants in location_is_present:
                print(variants.text)
                input_pickup = driver.find_element_by_xpath('//*[@id="start_address"]').clear()
                time.sleep(1)
                input_dropoff = driver.find_element_by_xpath('//*[@id="end_address"]').clear()
                time.sleep(1)
        else:
            print("shit")
            with open('Mozio_result.csv', 'a') as outFile:
                fieldnames = ['destination_location', 'status']
                writer = csv.DictWriter(outFile, fieldnames=fieldnames)
                writer.writerow({'destination_location': line, 'status': "has variation"})