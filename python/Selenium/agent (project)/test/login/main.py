import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
driver.get("https://beta-kafolat.uz/")
btn_log_in = driver.find_element(By.XPATH, "//div[@class='d-flex justify-content-end']""//a[@class='btn btn-blue btn-loading btn-small']")
btn_log_in.click()

numbers = driver.find_element(By.XPATH, "//div[@class='standard-input'][1]/input")
numbers.send_keys("992418888")
pasword = driver.find_element(By.XPATH, "//div[@class='standard-input'][2]/input")
pasword.send_keys("asdadgafgeargerrag")
login = driver.find_element(By.CSS_SELECTOR, '.form-group')
login.click()

time.sleep(5)
driver.close()