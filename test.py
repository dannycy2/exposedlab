from selenium import webdriver

###################
# Browser test for app
###################
# if chromedriver is not in your path, you’ll need to add it here
driver = webdriver.Chrome()

def site_login():
driver.get (“URL”)
driver.find_element_by_id(“user”).send_keys(“testaccount”)
driver.find_element_by_id (“password”).send_keys(“!testPASSSW0RDarena!”)
driver.find_element_by_id(“submit”).click()
