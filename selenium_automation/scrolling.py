from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.wikipedia.org/')
elem = driver.find_element_by_tag_name('html')

# scrolling down the page
elem.send_keys(Keys.END)
time.sleep(3)

# scrolling up the page
elem.send_keys(Keys.HOME)
time.sleep(5)

# click the link text and print the url
elem = driver.find_element_by_link_text('Privacy Policy')
elem.click()
print(driver.current_url)
