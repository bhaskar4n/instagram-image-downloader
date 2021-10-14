from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

print('Enter the gmailid and password')
gmailId = "baskar4n8"
password = "4545fuck"

driver = webdriver.Chrome("/home/baskar/Desktop/insa/chromedriver")
options = Options()
options.add_argument("/home/baskar/.config/google-chrome/Default")
#driver = webdriver.Chrome(chrome_options=options)

driver.get(r'https://github.com/bhaskar4n')



#driver.implicitly_wait(15)
#element = driver.find_element_by_xpath('//*[@id="react-root"]/section')
#href = element.get_attribute('href')
#print(element)


"""
loginBox = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
loginBox.send_keys(gmailId)

/html/body/div[1]/div[2]/div/img

passWordBox = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
passWordBox.send_keys(password)

nextButton = driver.find_elements_by_xpath('//*[@id="loginForm"]/div/div[3]')
nextButton[0].click()
nextButton1 = driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
nextButton1[0].click()

nextButton2 = driver.find_elements_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
nextButton2[0].click()

search = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
search.send_keys('prisma')

nextButton3 = driver.find_elements_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div')
nextButton3[0].click()
t =  time.sleep(5)
#driver.find_element_by_tag_name('html').send_keys(Keys.END)
scrolls = 4
while True:
    scrolls -= 1
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    print(driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article/div/div/div[1]/div[1]').text)
    time.sleep(3)
    if scrolls < 0:
        break




"""


"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys








s = driver.get("https://www.instagram.com/prisma")
username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")

username.send_keys("baskar4n8")
password.send_keys("4545fuck")

driver.find_element_by_name("submit").click()


#html = driver.find_element_by_tag_name('html')
#html.send_keys(Keys.END)
#html = driver.page_source
#html = driver.execute_script("return document.documentElement.outerHTML;")

#print(html)
"""
