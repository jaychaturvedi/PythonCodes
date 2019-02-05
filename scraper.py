from urllib.request import  urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests
import pandas


site = "https://www.amazon.com/best-sellers-books-Amazon/zgbs"

def getsoup(urls):                                                              #grabs the Source of page
    uClient = uReq(urls)
    page =  uClient.read()
    uClient.close()
    temp = soup(page,"html.parser")
    return  temp

pagesoup = getsoup(site)
index = pagesoup.find("ul",{"id":"zg_browseRoot"}).ul
indexlist = index.findAll("li")

fl = []

def openpage(hre):                                                              #iterate through the Categoroies on Main pages

    l=[]
    for j in range(1,6):
        href = hre + "#"+str(j)                                                 #Retrieving url for
        print(href)
        page = getsoup(href)
        allsec = page.findAll("div", {"class": "zg_itemWrapper"})
        for i in allsec:
            d = {}
            try:
                d["names"] = i.find("div", {"class": "p13n-sc-truncate"}).text.strip()
            except:
                d["names"] = None
            try:
                d["ratings"] = i.find("span", {"class": "a-icon-alt"}).text.strip()
            except:
                d["ratings"] = None
            try:
                d["price"] = i.find("span", {"class": "p13n-sc-price"}).text.strip()
            except:
                d["price"] = None
            try:
                d["availability"] = str("In Stock")
            except:
                d["availability"] =None
            l.append(d)
    return l

for links in indexlist:                                                         #
    href = links.a["href"]
    fl.extend(openpage(href))

print("csv")
df = pandas.DataFrame(fl)
df.to_csv("output.csv")
