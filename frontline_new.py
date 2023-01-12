from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import os

sys.path.insert(0, os.path.dirname(__file__).replace('parsing-new-script', 'global-files/'))
from GlobalFunctions import *
from GlobalVariable import *

try:
    file_name = "Frontier"
    GlobalFunctions.createFile(file_name)
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    # options.add_argument("headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    path = GlobalVariable.ChromeDriverPath

    scrappedUrl = "https://frontiersmeetings.com/upcoming-conferences"
    driver = webdriver.Chrome(chrome_options=options, executable_path=path)
    driver.minimize_window()

    driver.get(scrappedUrl)


    links = driver.find_elements(By.XPATH, "//div[@class='event-hover proimg']/a")
    # print(link)


        
    link_list=[]
    for i in links:
        link = i.get_attribute("href")
        # print(link)

        link_list.append(link)

    for j in link_list:

        driver.get(j) 
        
        try:
            ename = driver.find_element(By.XPATH, "//div[@class='carousel-caption car-cap1']/h2[2]").text
            print(ename)
        except:
            ename = driver.find_element(By.XPATH, "//div[@class='carousel-caption car-cap1']/h2").text
            print(ename)
        try:
            event_date = driver.find_element(By.XPATH,'//div[@class = "row"]// ul[@class = "car-capul"]//li[2]').text
            # char_remov = ["-",","]
            # for char in char_remov:
            #     event_date = event_date.replace(char," ")
            
            
            fdate = event_date
            # print(fdate)
                
            s_d , e_d = fdate.split('-')[0].split(' ')[1] , fdate.split('-')[1].split(',')[0]
            s_m , e_m =fdate.split(' ')[0],fdate.split(' ')[0]
            s_y , e_y =fdate.split(',')[1], fdate.split(',')[1]
            # print(s_m,e_m)
            # print(s_y, e_y)
            # print(s_d,e_d)
            
            stratDate, endDate = f"{s_y}-{GlobalVariable.months[s_m]}-{s_d}" , f"{e_y}-{GlobalVariable.months[e_m]}-{e_d}"
            print(stratDate,endDate)
        except:
            event_date = ''
        try:
            event_venue = driver.find_element(By.XPATH,'//div[@class= "row"]// ul[@class = "car-capul"]//li[3]').text
            print(event_venue)
            city_name = event_venue.split(',')[0]
            country_name = event_venue.split(',')[1]
            
            print(city_name)
            print(country_name)
        except:
            event_venue = ''
            orgName = "frontiersmeeting"
            orgWeb = "https://frontiersmeetings.com"
            
        try:
            cmail = driver.find_element(By.XPATH,"//div[@class='row'][3]//ul[@class='foot-imgdet']//li[1]//a").text
            print(cmail)
        except:
            cmail = 'info@frontiersmeetings.com'
            print("=====================================")
            
            
            GlobalFunctions.appendRow(file_name,[scrappedUrl,ename,stratDate,endDate,'','','',
                                               city_name,country_name,orgName,
                                               orgWeb,'','','',cmail,''])
             
except Exception as e:
    print(e)
    error = str(e)  
   
    
            
            

               