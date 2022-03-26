from dataclasses import dataclass
import enum
import time 
import requests
import csv
from selenium import webdriver
from bs4 import BeautifulSoup
start_url="https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser=webdriver.Chrome("C:\Users\DELL\Desktop\chromedriver_win32")
browser.get(start_url)
browser.get(start_url)
time.sleep(10)
planetdata=[]
newplanetdata=[]
headers=["name","light_years_from_earth","planet_mass","stellar_magnitude","discovery_date","hyperlink,planet_type","planet_radius","orbital_radius","orbital_period","eccentricity"]
def scrap():
    for i in range(1,430):
        while True:
            time.sleep(2)
            soup=BeautifulSoup(browser.page_source,"html.parser")
            currentpageno=int(soup.find_all("input",attrs={"class","pageno"})[0].get("value"))
            if currentpageno<i :
                browser.find_element_by_xpath
            elif currentpageno>i :
                browser.find_element_by_xpath
            else:
                break
        for ul_tag in soup.find_all("ul",attrs={"class","exoplanet"}):
            li_tags=ul_tag.fined_all("li")
            templist=[]
            for index,li_tags in enumerate(li_tags):
                if index==0:
                    templist.append(li_tags.find_all("a")[0].contents[0])
                else:
                    try:
                        templist.append(li_tags.contents[0])
                    except:
                        templist.append("")
            hyperlink_li_tag=li_tags[0]
            templist.append()
            planetdata.append(templist)
        browser.find_element_by_xpath()
def scrapmoredata(hyperlink):
    try:
        page=requests.get(hyperlink)
        soup=BeautifulSoup(page.content)
        templist=[]
    except:
        page.append(templist)
    
scrap()
for index,data in enumerate(planetdata):
    scrapmoredata(data[5])
finalplanetdata=[]
for index,data in enumerate:
    newplanetdataelement=newplanetdata[index]
    newplanetdataelement=newplanetdata[:7]
    finalplanetdata.append(data+newplanetdataelement)  
with open("final.csv","w")as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(finalplanetdata)
   
     