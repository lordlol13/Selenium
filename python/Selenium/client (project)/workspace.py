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

driver.get("https://beta-kafolat.uz/")

def select_element(element_xpath):
    element = driver.find_element(By.XPATH, element_xpath)
    element.click()
    time.sleep(1)

for i in range(1, 5):
    select_element(f'//div[@class="fast-fetch"]/span[{i}]')

time.sleep(1)

def select_tarif(tariff_number):
    tarif_windows = driver.find_element(By.XPATH, "(//input[@class='el-input__inner'])[2]")
    tarif_windows.click()
    time.sleep(1)
    tarifs = driver.find_element(By.XPATH, f"(//ul[@class='el-scrollbar__view el-select-dropdown__list'])[2]//li[{tariff_number}]")
    tarifs.click()

for i in range(1, 3):
    select_tarif(i)

time.sleep(1)

days = driver.find_element(By.XPATH, "(//div[@class='el-radio-group'])[1]/label[2]")
days.click()
time.sleep(1)

days12456 = driver.find_element(By.XPATH, "(//input[@class='el-input__inner'])[3]")
days12456.click()
time.sleep(1)

def select_days(day_number):
    days1234 = driver.find_element(By.XPATH, f"(//ul[@class='el-scrollbar__view el-select-dropdown__list'])[3]//li[{day_number}]")
    days1234.click()
    time.sleep(1)

for i in range(1, 6):
    select_days(i)

calendar = driver.find_element(By.XPATH, "(//input[@class='el-input__inner'])[4]")
calendar.click()
time.sleep(1)

calendar123 = driver.find_element(By.XPATH, "//table[@class='el-date-table']//td[@class='available']")
calendar123.click()
time.sleep(1)

travel = driver.find_element(By.XPATH, "(//input[@class='el-input__inner'])[6]")
travel.click()
time.sleep(1)

def select_type_travel(type_travel_number):
    if type_travel_number == 2:
        def select_type_travel_2(type_travel_number_2):
            travel2 = driver.find_element(By.XPATH, f"(//ul[@class='el-scrollbar__view el-select-dropdown__list'])[5]//li[{type_travel_number_2}]")
            travel2.click()

        select_type_travel_2(1)
        select_type_travel_2(2)
        select_type_travel_2(3)

    else:
        travel1 = driver.find_element(By.XPATH, f"(//ul[@class='el-scrollbar__view el-select-dropdown__list'])[4]//li[{type_travel_number}]")
        travel1.click()

for i in range(1, 4):
    select_type_travel(i)

time.sleep(1)

years = driver.find_element(By.XPATH, "(//div[@class='el-input']//input)[1]")
years.click()
years.send_keys("16072007")

time.sleep(3)

button = driver.find_element(By.XPATH, '//div[@class="d-flex flex-wrap justify-content-sm-end justify-content-center flex-sm-row align-items-center"]/button[2]')
button.click()

time.sleep(3)

button1 = driver.find_element(By.XPATH, '//div[@class="d-flex justify-content-end mt-5"]/button')
button1.click()

time.sleep(1)

seriya = driver.find_element(By.XPATH, '(//div[@class="el-input"]//input)[2]')
seriya.click()
seriya.send_keys('AD')

time.sleep(1)

number = driver.find_element(By.XPATH, "(//div[@class='el-input']//input)[3]")
number.click()
number.send_keys("3979115")

time.sleep(1)

name = driver.find_element(By.XPATH, "(//div[@class='el-input']//input)[4]")
name.send_keys("Muzaffar")

surname = driver.find_element(By.XPATH, "(//div[@class='el-input']//input)[5]")
surname.send_keys("Murodhojaev")

secondname = driver.find_element(By.XPATH, "(//div[@class='el-input']//input)[6]")
secondname.send_keys("Maqsudhoja")

adres = driver.find_element(By.XPATH, "(//label[text()='ПИНФЛ']/following::input)[1]")
adres.send_keys("Улица Амира Темура")

time.sleep(10)

button2 = driver.find_element(By.XPATH, "(//button[contains(@class,'btn btn-blue')])[2]")
button2.click()