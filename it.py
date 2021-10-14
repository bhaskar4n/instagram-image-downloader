#program to download images in instagram website.
#only required profile name
import json
import urllib.request
import urllib.request
import json
import re
import bs4 as bs
import urllib
from socket import timeout
import time
from bs4 import BeautifulSoup as soup
#urllib.request.urlretrieve('https://instagram.fmaa1-2.fna.fbcdn.net/t51.2885-15/e35/16789245_1231140993619505_838931546701299712_n.jpg','imagge.jpg')
import requests


my_url = open('inn.html', 'r')
page_soup = soup(my_url, "html.parser")
#print(page_soup.find_all('body'))
#div = page_soup.find(id="react-root")
div = page_soup.find("div", {"style": "flex-direction: column; padding-bottom: 0px; padding-top: 577.969px;"})
#input_tag = page_soup.find("meta", property="og:image")
#data  = page_soup.find_all("script")
print(div)
"""
jsondata = str(data[4])
jd = str(jsondata[52:])
data11 = str(jd[:-10])
#print(data11)
shortcodes = list()
src = list()
mydict = json.loads(data11)
id = list()
for i in range(15):

    code = mydict['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['shortcode']
    disp_src = mydict['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges'][i]['node']['display_url']
    disp_src = disp_src[:-6] + '83d603'
    url = "https://www.instagram.com/p/"+code
    shortcodes.append(url)
    src.append(disp_src)
    print(disp_src)
"""


"""
    response = requests.get(str(src[i]))
    if response.status_code == 200:    
        with open("/home/baskar/Desktop/insa/sam"+str(i+1)+".jpeg", 'wb') as f:
            f.write(response.content)
 """           
#https://instagram.fcjb5-1.fna.fbcdn.net/v/t51.2885-15/e35/p1080x1080/172398333_780294475927478_2915675902331386746_n.jpg?_nc_ht=instagram.fcjb5-1.fna.fbcdn.net&_nc_cat=102&_nc_ohc=STDmGr1qFGQAX_EWMq0&edm=AABBvjUBAAAA&ccb=7-4&oh=0658437de962c49d30a2c6e0b5a7add0&oe=616AB7EE&_nc_sid=83d603

#print(shortcodes)
#83d603


#print(src[0])


































































#headers = {'User-Agent': 'Mozilla/5.0'}
#web_link = "https://www.instagram.com/prisma"
#page = requests.get(web_link,headers=headers)
#html_contents = page.text
#soup = bs.BeautifulSoup(html_contents, 'html.parser')
#t =  time.sleep(5)
#data  = soup.find_all("script")
#print(html_contents)
#print(soup.prettify())




"""
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome("/home/baskar/Desktop/insa/chromedriver")

search_url=("https://www.instagram.com/prisma/") 
driver.get(search_url)
html = driver.page_source
#data  = bs.BeautifulSoup.find_all("script")


print(html)
"""
