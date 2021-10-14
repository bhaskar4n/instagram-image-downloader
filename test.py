# not yet finished!
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
#driver = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')
options = Options()
options.add_argument("-profile")
options.add_argument("/home/baskar/.mozilla/firefox/pv01og9w.default")
firefox_capabilities = DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True
driver = webdriver.Firefox(capabilities=firefox_capabilities, options=options)
driver.get("http://instagram.com/prisma")
#element = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[2]/article/div[1]/div/div[1]/div[2]/a')
#print(element.get_attribute('href'))

scrolls = 10
while True:
    scrolls -= 1
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    parent_div = len(driver.find_elements_by_xpath("/html/body/div[1]/section/main/div/div[2]/article/div/div/div"))
    #element = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article/div/div')
    #print(element)
    #print(driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article/div/div/div[1]/div[1]').text)
    for j in range(parent_div-1):
        for i in range(3):
            element =  driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[2]/article/div/div/div['+str(j+1)+']/div['+str(i+1)+']/a')
            print(element.get_attribute('href'))
    time.sleep(2)
    if scrolls < 0:
        break





""""
for i in range(3):
    for i in range(3):
        element = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[2]/article/div/div/div[1]/div['+str(i+1)+']/a')
        print(element.get_attribute('href'))

/html/body/div[1]/section/main/div/div[2]/article/div[1]/div/div[2]/div[1]/a



/html/body/div[1]/section/main/div/div[2]/article/div/div/div[1]/div[2]/a
/html/body/div[1]/section/main/div/div[2]/article/div/div/div[1]/div[4]/a
/html/body/div[1]/section/main/div/div[2]/article/div/div/div[1]/div[5]/a
/html/body/div[1]/section/main/div/div[2]/article/div/div/div[1]/div[6]/a
/html/body/div[1]/section/main/div/div[2]/article/div/div/div[1]/div[7]/a
/html/body/div[1]/section/main/div/div[2]/article/div/div/div[1]/div[8]/a


from selenium import webdriver
driver = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')
options = Options()

options.add_argument("/home/baskar/.mozilla/firefox/pv01og9w.default")
#fp = webdriver.FirefoxProfile('/home/baskar/.mozilla/firefox/pv01og9w.default')
#driver = webdriver.Firefox(fp)
driver.get("https://github.com")
"""

