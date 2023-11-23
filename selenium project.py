from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get("https://www.automationpanda.com/")

driver.find_element(By.ID,"menu-item-9").click()

text = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/article/div/div[1]/div[1]").text

print(text)

driver.implicitly_wait(6000)

