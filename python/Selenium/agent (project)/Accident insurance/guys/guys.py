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

time.sleep(15)

pon = driver.find_element(By.XPATH, "//a[@href='/ru/contracts/add']")
pon.click()

time.sleep(1)

menu = driver.find_element(By.XPATH, "//input[@readonly='readonly']")
menu.click()

menu1 = driver.find_element(By.XPATH, "(//ul[@class='el-scrollbar__view el-select-dropdown__list'])//li[@class='el-select-dropdown__item'][2]")
menu1.click()

time.sleep(1)

button5 = driver.find_element(By.XPATH, "//button[@class='btn btn-blue btn-next-step']")
button5.click()

time.sleep(1)

type_mune = driver.find_element(By.XPATH, "(//input[@class='el-input__inner'])[1]")
type_mune.click()

type = driver.find_element(By.XPATH, "(//ul[@class='el-scrollbar__view el-select-dropdown__list'])[2]//li[4]")
type.click()

period = driver.find_element(By.XPATH, "(//input[@class='el-input__inner'])[2]")
period.click()

period1 = driver.find_element(By.XPATH, "(//ul[@class='el-scrollbar__view el-select-dropdown__list'])[3]//li[4]")
period1.click()

calendar = driver.find_element(By.XPATH, "(//input[@class='el-input__inner'])[3]")
calendar.click()

calendar1 = driver.find_element(By.XPATH, "//table[@class='el-date-table']//td[@class='available']")
calendar1.click()
time.sleep(15)

button = driver.find_element(By.XPATH, "//button[contains(@class,'btn btn-blue')]")
button.click()


# оформление!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



time.sleep(7)
seriya = driver.find_element(By.XPATH, '(//div[@class="el-input"]//input)[2]')
seriya.click()
seriya.send_keys('SD')

time.sleep(1)
years = driver.find_element(By.XPATH, "(//div[@class='el-input']//input)[1]")
years.click()
years.send_keys("12121980")


time.sleep(1)

number = driver.find_element(By.XPATH, "(//div[@class='el-input']//input)[3]")
number.click()
number.send_keys("1234567")


time.sleep(1)
when = driver.find_element(By.XPATH, "(//div[@class='el-input']//input)[4]")
when.click()
when.send_keys("TTTT5555555555")

time.sleep(1)

name = driver.find_element(By.XPATH, "(//div[@class='el-input']//input)[5]")
name.send_keys("Muzaffar")

surname = driver.find_element(By.XPATH, "(//div[@class='el-input']//input)[6]")
surname.send_keys("Murodhojaev")

secondname = driver.find_element(By.XPATH, "(//div[@class='el-input']//input)[7]")
secondname.send_keys("Maqsudhoja")

workplace = driver.find_element(By.XPATH, "(//span[text()[normalize-space()='Женский']]/following::input)[1]")
workplace.send_keys("Kafolat")

adres = driver.find_element(By.XPATH, "(//label[text()='ПИНФЛ']/following::input)[1]")
adres.send_keys("Улица Амира Темура")

menu2 = driver.find_element(By.XPATH, "(//input[@class='el-input__inner'])[3]")
menu2.click()

menu3 = driver.find_element(By.XPATH, "(//ul[@class='el-scrollbar__view el-select-dropdown__list'])[8]//li[2]")
menu3.click()

alo = driver.find_element(By.XPATH, "((//label[text()='Отчество'])[2]/following::input)[1]")
alo.click()
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