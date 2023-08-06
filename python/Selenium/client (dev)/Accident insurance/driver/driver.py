import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Firefox()
driver.get("http://dev.beta-kafolat.uz/")

btn_log_in = driver.find_element(By.XPATH, "//div[@class='d-flex justify-content-end']""//a[@class='btn btn-blue btn-loading btn-small']")
btn_log_in.click()

numbers = driver.find_element(By.XPATH, "//div[@class='standard-input'][1]/input")
numbers.send_keys("992418888")
pasword = driver.find_element(By.XPATH, "//div[@class='standard-input'][2]/input")
pasword.send_keys("mmm2007mama")
login = driver.find_element(By.CSS_SELECTOR, '.form-group')
login.click()

time.sleep(2)

driver.get("http://dev.beta-kafolat.uz/ru")

pon = driver.find_element(By.XPATH, "(//button[contains(@class,'btn btn-blue')])[2]")
pon.click()

menu = driver.find_element(By.XPATH, "(//ul[@class='products-list'])//li[2]")
menu.click()

time.sleep(2)

type_insurance = driver.find_element(By.XPATH, "(//input[@class='el-input__inner'])[1]")
type_insurance.click()

time.sleep(1)

Accidentinsurance = driver.find_element(By.XPATH, "(//ul[@class='el-scrollbar__view el-select-dropdown__list'])//li[5]")
Accidentinsurance.click()

time.sleep(1)

calendar1 = driver.find_element(By.XPATH, "//div[@class='col-md-6'][1]")
calendar1.click()
calendar = driver.find_element(By.XPATH, '(//table[@class="el-date-table"]//td[@class="available"])[1]')
calendar.click()

time.sleep(8)

button = driver.find_element(By.XPATH, "(//button[contains(@class,'btn btn-blue')])[1]")
button.click()

time.sleep(6)

button = driver.find_element(By.XPATH, "(//button[contains(@class,'btn btn-blue')])[1]")
button.click()

time.sleep(1)

#паспорт Узбекистана

data = driver.find_element(By.XPATH, "(//div[@class='birthday'])[1]//input")
data.click()
data.send_keys("12121980")


seriya = driver.find_element(By.XPATH, "(//div[@class='form-group seria mw icon-right'])[1]//input")
seriya.click()
seriya.send_keys('SD')

time.sleep(1)

number = driver.find_element(By.XPATH, "(//div[@class='form-group number mw icon-right'])[1]//input")
number.click()
number.send_keys("1234567")

time.sleep(3)

name = driver.find_element(By.XPATH, "(//div[@class='form-group mw icon-right'])[1]//input")
name.send_keys("Muzaffar")

surname = driver.find_element(By.XPATH, "(//div[@class='form-group mw icon-right'])[2]//input")
surname.send_keys("Murodhojaev")

secondname = driver.find_element(By.XPATH, "(//div[@class='form-group mw icon-right'])[3]//input")
secondname.send_keys("Maqsudhoja")

time.sleep(1)

adres = driver.find_element(By.XPATH, "(//label[text()='ПИНФЛ']/following::input)[1]")
adres.send_keys("Улица Амира Темура")

time.sleep(1)

button3 = driver.find_element(By.XPATH, "(//button[contains(@class,'btn btn-blue')])[2]")
button3.click()

time.sleep(1)

button4 = driver.find_element(By.XPATH, "//button[@class='btn btn-blue btn-large ml-sm-3 mb-2 btn-loading']")
button4.click()

time.sleep(1)

cards = driver.find_element(By.XPATH, "(//div[@class='el-input']//input)[1]")
cards.find_element('1111111111111111')

time.sleep(1)

cards1 = driver.find_element(By.XPATH, "(//div[@class='el-input']//input)[2]")
cards1.find_element('1111')

time.sleep(1)

button5 = driver.find_element(By.XPATH, "(//button[contains(@class,'btn btn-blue')])[2]")
button5.click()