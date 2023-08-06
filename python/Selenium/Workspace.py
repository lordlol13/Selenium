import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Firefox()
driver.get("https://beta-kafolat.uz/")

btn_log_in = driver.find_element(By.XPATH, "//div[@class='d-flex justify-content-end']""//a[@class='btn btn-blue btn-loading btn-small']")
btn_log_in.click()

numbers = driver.find_element(By.XPATH, "//div[@class='standard-input'][1]/input")
numbers.send_keys("992418888")
pasword = driver.find_element(By.XPATH, "//div[@class='standard-input'][2]/input")
pasword.send_keys("mmm2007mama")
login = driver.find_element(By.CSS_SELECTOR, '.form-group')
login.click()

time.sleep(2)

driver.get("https://beta-kafolat.uz/")

pon = driver.find_element(By.XPATH, "(//button[contains(@class,'btn btn-blue')])[2]")
pon.click()

menu = driver.find_element(By.XPATH, "(//ul[@class='products-list'])//li[2]")
menu.click()

time.sleep(2)

type_insurance = driver.find_element(By.XPATH, "(//input[@class='el-input__inner'])[1]")
type_insurance.click()

time.sleep(1)

Accidentinsurance = driver.find_element(By.XPATH, "(//ul[@class='el-scrollbar__view el-select-dropdown__list'])//li[4]")
Accidentinsurance.click()

time.sleep(1)

person = driver.find_element(By.XPATH, "(//div[@class='el-input']//input)[1]").send_keys(Keys.BACKSPACE, "4")

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

# типы паспортов!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def pasport (Menu,passport,dataid,seria,phone,first,second,third,):
    type_pasport_menu = driver.find_element(By.XPATH,f"(//input[@class='el-input__inner'])[2]")
    type_pasport_menu.click()
    time.sleep(1)


    type_pasport = driver.find_element(By.XPATH, f"(//li[@class='el-select-dropdown__item'])[{Menu}]")
    type_pasport.click()


    data = driver.find_element(By.XPATH, "(//div[@class='birthday'])[2]//input")
    data.click()
    data.send_keys(f"{dataid}")


    seriya = driver.find_element(By.XPATH, f"(//div[@class='form-group seria mw icon-right'])[2]//input")
    seriya.click()
    seriya.send_keys(f'{seria}')


    time.sleep(1)


    number = driver.find_element(By.XPATH, "(//div[@class='form-group number mw icon-right'])[2]//input")
    number.click()
    number.send_keys(f"{phone}")

    time.sleep(3)

    name = driver.find_element(By.XPATH, f"(//div[@class='form-group mw icon-right'])[4]//input")
    name.send_keys(f"{first}")

    surname = driver.find_element(By.XPATH, f"(//div[@class='form-group mw icon-right'])[5]//input")
    surname.send_keys(f"{second}")

    secondname = driver.find_element(By.XPATH, f"(//div[@class='form-group mw icon-right'])[6]//input")
    secondname.send_keys(f"{third}")

