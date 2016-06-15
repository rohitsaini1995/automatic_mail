from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common import action_chains, keys
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import time
import os
chromedriver = "C:\Users\Rohit Saini\Downloads\chromedriver_win32\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get('https://www.gmail.com/')
print("Opened gmail...")
time.sleep(2)
#action = action_chains.ActionChains(driver)
#action.send_keys(keys.Keys.CONTROL+keys.Keys.SHIFT+'i')
#action.perform()
# this below ENTER is to rid of the above "i"
#action.send_keys(keys.Keys.ENTER)
# inject the JavaScript...
#action.send_keys("document.querySelectorAll('label.boxed')[1].click()")
#action.perform()
email = driver.find_element_by_xpath("//input[@id='Email' or @name='Email']")
email.send_keys('rohitsainisirsma')
#action.send_keys(keys.Keys.ENTER)
print("Email Id entered...")
button = driver.find_element_by_xpath("//input[@id='next' or @name='signIn']")
button.click()
time.sleep(2)
password = driver.find_element_by_xpath("//input[@id='Passwd' or @name='Passwd']")
password.send_keys('r7357643380')
print("Password entered...")
#button=password.send_keys(Keys.TAB)
button = driver.find_element_by_xpath("//div[contains(@class, 'slide-in')]//input[@name='signIn']")
button.click()
print "gmail-opened"
#button.send_keys(Keys.ENTER)
time.sleep(10)
button = driver.find_element_by_xpath("//div[contains(@class, 'nH')]//div[contains(@class, 'T-I J-J5-Ji T-I-KE L3')]")
button.click()
print "compose box opened"
time.sleep(5)
button = driver.find_element_by_xpath("//div[contains(@class, 'wO nr l1')]//textarea[@id=':oi']")
button.send_keys('sahilbhatia1995@gmail.com')
button = driver.find_element_by_xpath("//div[contains(@class, 'aoD az6')]//input[@name='subjectbox']")
button.send_keys('first python project')
button = driver.find_element_by_xpath("//div[contains(@class, 'Ar Au')]//div[@id=':p7']")
button.send_keys('first Automated email')
button = driver.find_element_by_xpath("//div[contains(@class, 'J-J5-Ji')]//div[@id=':ns']")
button.click()
