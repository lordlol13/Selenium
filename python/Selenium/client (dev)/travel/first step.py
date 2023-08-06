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

time.sleep(1)

driver.get("https://beta-kafolat.uz/")


random_number = random.randint(1,2)

pon = driver.find_element(By.XPATH, "(//button[contains(@class,'btn btn-blue')])[2]")
pon.click()

time.sleep(1)

data =  driver.find_element(By.XPATH, '//div[@class="fast-fetch"]/span[1]')
data1 =  driver.find_element(By.XPATH, '//div[@class="fast-fetch"]/span[2]')
data2 =  driver.find_element(By.XPATH, '//div[@class="fast-fetch"]/span[3]')
data3 =  driver.find_element(By.XPATH, '//div[@class="fast-fetch"]/span[4]')
data.click()
data1.click()
data2.click()
data3.click()

time.sleep(1)

def two_tarif(tarif):
    tarif_windows = driver.find_element(By.XPATH, "(//input[@class='el-input__inner'])[2]")
    tarif_windows.click()

    time.sleep(1)

    tarifs = driver.find_element(By.XPATH, f"(//ul[@class='el-scrollbar__view el-select-dropdown__list'])[2]//li[{tarif}]")
    tarifs.click()

two_tarif(1)
two_tarif(2)

time.sleep(1)

days = driver.find_element(By.XPATH, "(//div[@class='el-radio-group'])[1]/label[2]")
days.click()

time.sleep(1)

days12456 = driver.find_element(By.XPATH, "(//input[@class='el-input__inner'])[3]")
days12456.click()

time.sleep(1)

def days(day):
    days1234 = driver.find_element(By.XPATH, f"(//ul[@class='el-scrollbar__view el-select-dropdown__list'])[3]//li[{day}]")
    days1234.click()

    time.sleep(1)

days(1)
days(2)
days(3)
days(4)
days(5)

calendar = driver.find_element(By.XPATH, "(//input[@class='el-input__inner'])[4]")
calendar.click()

calendar123 = driver.find_element(By.XPATH, "//table[@class='el-date-table']//td[@class='available']")
calendar123.click()

time.sleep(1)

travel = driver.find_element(By.XPATH, "(//input[@class='el-input__inner'])[6]")
travel.click()

time.sleep(1)

def type_travel(number_type_travel):
    if number_type_travel == 2:
        def type_travel_2(number_type_travel_2):
            travel2 = driver.find_element(By.XPATH, f"(//ul[@class='el-scrollbar__view el-select-dropdown__list'])[5]//li[{number_type_travel_2}]")
            travel2.click()

        type_travel_2(1)
        type_travel_2(2)
        type_travel_2(3)

    else:
        travel1 = driver.find_element(By.XPATH, f"(//ul[@class='el-scrollbar__view el-select-dropdown__list'])[4]//li[{number_type_travel}]")
        travel1.click()

type_travel(1)
type_travel(2)
type_travel(3)

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

icon = driver.find_element(By.XPATH, "//span[@class='el-checkbox__input']//span[1]")
icon.click()

button3 = driver.find_element(By.XPATH, "(//button[contains(@class,'btn btn-blue')])[1]")
button3.click()

cards = driver.find_element(By.XPATH, "(//div[@class='el-input']//input)[1]")
cards.click()
cards.send_keys("1111111111111111")

cards_date = driver.find_element(By.XPATH, "(//div[@class='el-input']//input)[2]")
cards_date.click()
cards_date.send_keys("1111")

button4 = driver.find_element(By.XPATH, "(//button[contains(@class,'btn btn-blue')])[2]")
button4.click()

time.sleep(30)
driver.quit()