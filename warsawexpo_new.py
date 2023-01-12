from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import os

sys.path.insert(0, os.path.dirname(__file__).replace('parsing-new-script', 'global-files/'))
from GlobalFunctions import *
from GlobalVariable import *

try:
    file_name = "war1"
    GlobalFunctions.createFile(file_name)
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    # options.add_argument("headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    path = GlobalVariable.ChromeDriverPath

    scrappedUrl = "https://warsawexpo.eu/en/exhibition-calendar"
    driver = webdriver.Chrome(chrome_options=options, executable_path=path)

    driver.get(scrappedUrl)

    links_raw = driver.find_elements(By.XPATH, "//*[@id='row-unique-2']/div/div/div/div/div/div/div/div[3]/div/a")

    link_list = []
    for i in range(0, len(links_raw)):

        links = links_raw[i].get_attribute("href")
        link_list.append(links)
    

    # print(link_list)
    # print(len(link_list))

    
    for i in link_list:
        driver.get(i)
        
        try:
            event_name = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[1]/div/div/div/div[1]/h1").text

            # print(event_name)
        except:
            pass

        try:
            startdate_raw = driver.find_element(By.XPATH,"/html/body/div[4]/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[1]/div/div/div/div[1]/div/span[1]").text.split("-")
            enddate_raw = driver.find_element(By.XPATH,"/html/body/div[4]/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[1]/div/div/div/div[1]/div/span[2]").text.split("-")

            s_y, e_y = startdate_raw[-1], enddate_raw[-1]
            s_m, e_m = startdate_raw[-2], enddate_raw[-2]
            s_d, e_d = startdate_raw[-3], enddate_raw[-3]

            startdate = f"{s_y}-{s_m}-{s_d}"
            enddate = f"{e_y}-{e_m}-{e_d}"

            # print(startdate)
            # print(enddate)

        except:
            pass

        try:
            orgName  = driver.find_element(By.CLASS_NAME, "organizer").text
            # print(orgName)
        except:
            pass

        try:
            orgWeb = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/p/a[3]").text

            # print(orgWeb)
        except:
            pass


        try:
            cmail = driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div/div/div/p/a[2]").get_attribute("textContent")
            Contactnumber = driver.find_element(By.XPATH,"/html/body/div[4]/div/div[2]/div/div/div/div/div/div[1]/div[2]/div[2]/div[2]/div/div/div/div/div/p/a").get_attribute("textContent")

            # print(Contactnumber)
            # print(cmail)

        except:
            pass

        try:

            venue = driver.find_element(By.XPATH, "//div[@class= 'uncode_text_column']//span[@itemprop='address']").text.replace("\n", " ")
            city= driver.find_element(By.XPATH, "//div[@class= 'uncode_text_column']//span[@itemprop='addressRegion']").text
            country = driver.find_element(By.XPATH, "//div[@class= 'uncode_text_column']//span[@itemprop='address']").text.split("\n")[-1].split(",")[-1].strip()

            # print(country)
            # print(city)
            # print(venue)


            if venue:
                emode = 0
                google_location = GlobalFunctions.get_google_map_url(venue, driver)

                # print(emode)

            else:
                emode = 1
                google_location = ''



                # print(emode)

        except:
            pass

        GlobalFunctions.appendRow(file_name,[scrappedUrl, event_name, startdate, enddate, '', '', '', '', orgName,
                                           orgWeb, '', '', '', '', '', city, country, venue, i,
                                           google_location, cmail, '', emode])
except:
    pass