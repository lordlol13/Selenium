import random
import time

from selenium import webdriver
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

driver.get("https://beta-kafolat.uz/")


random_number = random.randint(1,2)

pon = driver.find_element(By.XPATH, "(//button[contains(@class,'btn btn-blue')])[2]")
pon.click()

time.sleep(1)

# data =  driver.find_element(By.XPATH, '//div[@class="fast-fetch"]/span[1]')
# data1 =  driver.find_element(By.XPATH, '//div[@class="fast-fetch"]/span[2]')
# data2 =  driver.find_element(By.XPATH, '//div[@class="fast-fetch"]/span[3]')
# data3 =  driver.find_element(By.XPATH, '//div[@class="fast-fetch"]/span[4]')
# data.click()
# data1.click()
# data2.click()
# data3.click()

country = driver.find_element(By.XPATH, "//div[@class='el-select__tags']//input[1]")
country.click()

for i in range(5):
    random_number = random.randint(1, 228)

countrys = driver.find_element(By.XPATH, f"(//ul[@class='el-scrollbar__view el-select-dropdown__list'])[1]//li[{i}]")
countrys.click()
time.sleep(1)
countrys = driver.find_element(By.XPATH, f"(//ul[@class='el-scrollbar__view el-select-dropdown__list'])[1]//li[{i}]")
countrys.click()
time.sleep(1)
countrys = driver.find_element(By.XPATH, f"(//ul[@class='el-scrollbar__view el-select-dropdown__list'])[1]//li[{i}]")
countrys.click()
time.sleep(1)
countrys = driver.find_element(By.XPATH, f"(//ul[@class='el-scrollbar__view el-select-dropdown__list'])[1]//li[{i}]")
countrys.click()
time.sleep(1)
countrys = driver.find_element(By.XPATH, f"(//ul[@class='el-scrollbar__view el-select-dropdown__list'])[1]//li[{i}]")
countrys.click()
time.sleep(1)


tarif = driver.find_element(By.XPATH, "(//input[@class='el-input__inner'])[2]")
tarif.click()

time.sleep(1)

tarif1 = driver.find_element(By.XPATH, "(//ul[@class='el-scrollbar__view el-select-dropdown__list'])[2]//li[1]")
tarif1.click()

time.sleep(1)

days = driver.find_element(By.XPATH, "(//div[@class='el-radio-group'])[1]/label[2]")
days.click()

time.sleep(1)

days12456 = driver.find_element(By.XPATH, "(//input[@class='el-input__inner'])[3]")
days12456.click()

time.sleep(1)

days1234 = driver.find_element(By.XPATH, "(//ul[@class='el-scrollbar__view el-select-dropdown__list'])[3]//li[5]")
days1234.click()

time.sleep(1)

travel = driver.find_element(By.XPATH, "(//input[@class='el-input__inner'])[6]")
travel.click()

time.sleep(1)

travel1 = driver.find_element(By.XPATH, "(//ul[@class='el-scrollbar__view el-select-dropdown__list'])[4]//li[1]")
travel1.click()

time.sleep(1)

years = driver.find_element(By.XPATH, "(//div[@class='el-input']//input)[1]")
years.click()
years.send_keys("12121980")

time.sleep(15)

button = driver.find_element(By.XPATH, '//div[@class="d-flex flex-wrap justify-content-sm-end justify-content-center flex-sm-row align-items-center"]/button[2]')
button.click()

time.sleep(7)

button1 = driver.find_element(By.XPATH, '//div[@class="d-flex justify-content-end mt-5"]/button')
button1.click()

time.sleep(1)

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