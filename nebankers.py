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
sys.path.insert(0, os.path.dirname(__file__).replace('parsing-new-script','global-files/'))
from GlobalVariable import *
from GlobalFunctions import *

# try:
file_name="nebankers"
#file_name=sys.argv[1]   #file name from arguments (1st)
# port=int(sys.argv[2])   #port number from arguments (2nd)

GlobalFunctions.createFile(file_name)   #to created TSV file with header line

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
# options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

path = GlobalVariable.ChromeDriverPath
driver = webdriver.Chrome(options=options, executable_path=path)

error = ''
 
try:
    links = []
    # coo=[]
    #getting the links of events page from list page and storing them in a list  
    for page in ['https://www.nebankers.org/', ]:
        driver.get(page)
        time.sleep(4)
        links.extend([link.get_attribute("href") for link in driver.find_elements(By.XPATH, "//a[@class='wli-event-link wliComponent']")])
        # print(links,'---------')
        # link=links

    for url in links:
        try:
            driver.get(url)
            time.sleep(3)

            # Event Name
###################################################################################################################################
            try:
                ename  = driver.find_element(By.XPATH, "//h2[@class='wsite-content-title']").text
                # print(title)
                
                print(ename)
            except:
                # title = ''
                ename=''

            if not ename:
                    continue
             
###################################################################################################################################
            try:
                # print(ename,'===')
                st_date  = driver.find_element(By.XPATH, "//div[@class='wc-eventDetailDate']//label").get_attribute("textContent")
                s_date=st_date.split('-')[0].split(',')[1].strip().split(' ')
                ss_date=st_date.split('-')[0].split(',')[2].strip().split(' ')
                print(s_date,'11111111111111111111111111111111111111111111')
                print(ss_date,'222222222222222222222222222222222222222')




                            
                q1=s_date[1]
                q2=s_date[0]
                q3=ss_date[0]
                month = GlobalVariable.months[q2]
                startdate = f"{q3}-{month}-{q1}"
           


                try:
         
                    en_date  = driver.find_element(By.XPATH, "//div[@class='wc-eventDetailDate']//label").get_attribute("textContent")
               
                    e_date=en_date.split('-')[1].split(',')[1].strip().split(' ')
              
                    ee_date=en_date.split('-')[0].split(',')[2].strip().split(' ')
            





                                
                    q1=e_date[1]
                    q2=e_date[0]
                    q3=ee_date[0]
                    month = GlobalVariable.months[q2]
                    enddate = f"{q3}-{month}-{q1}"
                


                    
                except:
                    enddate = startdate
            



                
            except:
                startdate = ''
                enddate=''


    ###################################################################################################################################

            orgName = "nebankers"
            orgWeb = "https://www.nebankers.org/"

    ###################################################################################################################################

            try:
                timess  = driver.find_element(By.XPATH, "//div[@class='wc-eventDetailDate']").get_attribute("textContent")

                s_time=timess.split('-')[0].split(',')[2].strip().split(' ')
                print(s_time)
                start_time=s_time[1]+s_time[2]
                print(start_time,'!!!!!!!!!!!!!!!!!!!!!!!!!1')




                no=timess.split('-')[1]
     
                end_time_raw=no.split('\n')[0].split(' ')
                end_time = end_time_raw[-2] + end_time_raw[-1]
                a=no_cst.strip().split(' ')[-1]
         

                timezone=a
                



                timing = [{"type": "general", "Start_time": start_time, "end_time": end_time,
                "timezone": timezone, "days": "all"}]


    

        

            except:
 
                times=''

            cmail = ""
          
    ###################################################################################################################################
            try:
                venues  = driver.find_element(By.XPATH, "//div[@class='wc-eventDetailLocation']").get_attribute("textContent")
                venue=venues.strip()  

                city_row=venue.split(',')[0].strip().split(' ')[-1]
                city_row=city_row.replace('\n',' ')
                city=city_row.split(" ")[1]
                print(city)

                country_row=venue.split(',')[1].strip().split(' ')[0]
                country_row=country_row.lower()


            except:
                venue = ''
                city=''
                country_row=''
     
            try:
                country=GlobalVariable.states_abv_dict[country_row]
               
            except:
                country=''
         

            if venue:
                emode = 0
                
            else:
                emode = 1
            print(emode)

            google_location=''

            speakerlist=''
            urls='https://www.nebankers.org/'

            GlobalFunctions.appendRow(file_name,[urls, ename, startdate, enddate, timing, '', '', '', orgName,
                                                    orgWeb, '', '', '', '', '', city, country, venue, url,
                                                    '', cmail, '', emode])
            



        except Exception as e:
            # print(e)
            error = str(e)
            continue


except Exception as e:
    print(e)
    error = str(e)


GlobalFunctions.update_scrpping_execution_status(file_name, error)
# driver.quit()
