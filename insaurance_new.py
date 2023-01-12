import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import sys
import json
from random import randint
import time
import requests
from datetime import datetime
sys.path.insert(0, os.path.dirname(__file__).replace(
    'parsing-new-script', 'global-files/'))
from GlobalFunctions import *
from GlobalVariable import *


file_name = "insaurance"

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")


path = GlobalVariable.ChromeDriverPath
driver = webdriver.Chrome()
driver.minimize_window()

url = ("https://www.insuranceinstitute.ca/en/insurance-education/events")
driver.get(url)
# print(url)

link = []
link.extend(link.get_attribute('href') for link in driver.find_elements(
    By.XPATH, '//a[@class = "listing-heading"]'))
# print(len(link))
# print(link)
for url in link:
    try:
        driver.get(url)
        try:
            ename = driver.find_element(By.XPATH, "//h1//span").text
            print(ename)
         #    print("swdwfwfewf")
        except:
            pass
    except:
        pass
    try:
        event_date = driver.find_element(
            By.XPATH, '//*[@id="lockedform_0_lockedcontent_0_maincolumn_1_lblDateAndTime"]').text
        # print(event_date)
        # print(type(event_date))
        char_remov = '(ET)', '(EST)', 'ET', 'PST', 'Atlantic Tim'
        for char in char_remov:
            event_date = event_date.replace(char, "")
        print(event_date)
        s = ",2023"
        start_date = event_date.split(',')[0]
        start_time = event_date.split(' - ')[0].split('2023')[1]
        end_time = event_date.split(' - ')[1].strip()
        print("event ends time -",end_time)
        print("event starts time -",start_time)
        print("event starts date IS -",start_date + s)

    except:
        start_date = ''
        start_time = ''
        end_time = ''
        # print("===========")

    try:
        event_venue = driver.find_element(
            By.XPATH, "//*[@id='lockedform_0_lockedcontent_0_maincolumn_1_lblPlace']").text
        print(event_venue)
        # print("newhcbweubew")
    except:
        event_venue = ''
        
    try:
        cmail= driver.find_element(By.XPATH,'//*[@id="lockedform_0_lockedcontent_0_maincolumn_1_lblDescription"]/font/span/span/font/font/font/span/font/span/font/span/p[15]/font/font[3]/a').text
        print(cmail)
        # print("dhdhd")
    except:
        cmail= ''

        orgName = "Insaurance Institute"
        orgWeb = "https://www.insuranceinstitute.ca"
        url = "https://www.insuranceinstitute.ca"
        
         
    
        
        GlobalFunctions.appendRow(file_name,[url,ename,start_date,start_time,end_time,'','','',link,event_venue,'',orgName,
                                          orgWeb,cmail,''])
    
      
      
    
GlobalFunctions.update_scrpping_execution_status(file_name,'')