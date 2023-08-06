import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Firefox()
driver.get("https://agent.beta-kafolat.uz/ru/contracts")


numbers = driver.find_element(By.XPATH, "//div[@class='form-group']/input")
numbers.send_keys("kafolat")
pasword = driver.find_element(By.XPATH, "(//div[@class='form-group form-group-ico'])/input")
pasword.send_keys("kafolat123")
login = driver.find_element(By.XPATH, "//button[@class='btn btn-blue submit']")
login.click()

time.sleep(4)

pon = driver.find_element(By.XPATH, "//a[@href='/ru/contracts/add']")
pon.click()

time.sleep(1)

menu = driver.find_element(By.XPATH, "//input[@readonly='readonly']")
menu.click()

menu1 = driver.find_element(By.XPATH, "//ul[@class='el-scrollbar__view el-select-dropdown__list']//li[@class='el-select-dropdown__item'][5]")
menu1.click()

time.sleep(1)

button5 = driver.find_element(By.XPATH, "//button[@class='btn btn-blue btn-next-step']")
button5.click()

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

tarif = driver.find_element(By.XPATH, "(//input[@class='el-input__inner'])[2]")
tarif.click()

time.sleep(1)
# Функция
def tarif_type (tarif_type_menu):
    tarif1 = driver.find_element(By.XPATH, f"body[1]/div[6]/div[1]/div[1]/ul[1]/li[{tarif_type_menu}]")
    tarif1.click()

# элементы
tarif_type(1)
tarif_type(2)

time.sleep(1)

day = driver.find_element(By.XPATH, "(//div[@class='el-radio-group'])[1]/label[2]")
day.click()

time.sleep(1)
days12456 = driver.find_element(By.XPATH, "(//input[@class='el-input__inner'])[3]")
days12456.click()

time.sleep(1)

# Функция
def days (days_number):
    days1234 = driver.find_element(By.XPATH, f"(//ul[@class='el-scrollbar__view el-select-dropdown__list'])[5]//li[@class='el-select-dropdown__item'][{days_number}]")
    days1234.click()

# элементы
days(1)
days(2)
days(3)
days(4)
days(5)

calendar = driver.find_element(By.XPATH, "(//input[@class='el-input__inner'])[4]")
calendar.click()

calendar1 = driver.find_element(By.XPATH, "//table[@class='el-date-table']//td[@class='available']")
calendar1.click()

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
        travel1 = driver.find_element(By.XPATH, f"(//ul[@class='el-scrollbar__view el-select-dropdown__list'])[5]//li[{number_type_travel}]")
        travel1.click()

type_travel(1)
type_travel(2)
type_travel(3)

time.sleep(1)

years = driver.find_element(By.XPATH, "(//div[@class='el-input']//input)[2]")
years.click()
years.send_keys("12121980")

time.sleep(15)

button = driver.find_element(By.XPATH, "//button[contains(@class,'btn btn-blue')]")
button.click()

time.sleep(7)
seriya = driver.find_element(By.XPATH, '(//div[@class="el-input"]//input)[2]')
seriya.click()
seriya.send_keys('SD')

time.sleep(1)

number = driver.find_element(By.XPATH, "(//div[@class='el-input']//input)[3]")
number.click()
number.send_keys("1234567")

time.sleep(1)

name = driver.find_element(By.XPATH, "(//div[@class='el-input']//input)[4]")
name.send_keys("Muzaffar")

surname = driver.find_element(By.XPATH, "(//div[@class='el-input']//input)[5]")
surname.send_keys("Murodhojaev")

secondname = driver.find_element(By.XPATH, "(//div[@class='el-input']//input)[6]")
secondname.send_keys("Maqsudhoja")

adres = driver.find_element(By.XPATH, "(//label[text()='ПИНФЛ']/following::input)[1]")
adres.send_keys("Улица Амира Темура")

menu2 = driver.find_element(By.XPATH, "(//input[@class='el-input__inner'])[1]")
menu2.click()

menu3 = driver.find_element(By.XPATH, "(//ul[@class='el-scrollbar__view el-select-dropdown__list'])[7]//li[2]")
menu3.click()

alo = driver.find_element(By.XPATH, "((//label[text()='Отчество'])[2]/following::input)[1]")
time.sleep(1)
alo.click()
time.sleep(1)
alo.send_keys('34343443434334')

adress_number = driver.find_element(By.XPATH, "//label[text()='Адрес']/following::input")
adress_number.click()
time.sleep(2)
adress_number.send_keys('992418888')
time.sleep(20)

button2 = driver.find_element(By.XPATH, "(//button[contains(@class,'btn btn-blue')])")
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