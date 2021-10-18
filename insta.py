from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
#driver = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')
#link = /home/baskar/.mozilla/firefox/#######.default
options = Options()
#options.headless = True
options.add_argument("-profile")
options.add_argument("/home/#####/.mozilla/firefox/######.default") #enter profile location here
firefox_capabilities = DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True
driver = webdriver.Firefox(capabilities=firefox_capabilities, options=options)
profile_name = "#######" #enter profile name here...
driver.get("http://www.instagram.com/"+profile_name) 
import requests
link = []
post = driver.find_element_by_xpath('//*[@class="g47SY "]')

#print(post.text)
stop = int(post.text)
print("getting all img src links...")
while True:
    time.sleep(1)
    parent_div = len(driver.find_elements_by_xpath('//*[@class="ySN3v"]/div/div/div'))
    #print(parent_div) 
    for k in range(1,int(parent_div)+1):
        child_div = len(driver.find_elements_by_xpath('//*[@class="Nnq7C weEfm"]['+str(k)+']/div'))
        for j in range(1,int(child_div)+1):
            try:
                src = driver.find_element_by_xpath('//*[@class="Nnq7C weEfm"]['+str(k)+']/div['+str(j)+']/a/div/div/img')
                img_src = src.get_attribute('src')
            except:
                break
            if img_src not in link:
                if len(link) <= stop:
                    link.append(img_src)
                else:
                    break            
        if len(link) >= stop:
            break
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1)
    #print(len(link)," ",stop)
    if len(link) >= stop:
        break
print(len(link),'links found')
driver.quit()
print('downloading all images...')
#print(link.count(link[0]))
n  = 0
for i in link:
    n = n+1 
    response = requests.get(i+'&dl=1')
    if response.status_code == 200:
        with open("/home/#####/Desktop/####/test/image_"+str(n)+".jpeg", 'wb') as f: #enter storage location here...
            f.write(response.content)

print('all images download...')

