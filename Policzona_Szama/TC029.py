import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#Konto musi być zarejestrowane.
driver = webdriver.Firefox()
driver.get("https://policzona-szama.pl/")
time.sleep(1)

#logowanie
driver.find_element(By.XPATH, '//*[@id="SiteHeader"]/div[1]/div[1]/div/div[4]/div/div[1]/a[2]/span').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="CustomerEmail"]').send_keys('malykranik@gmail.com')
driver.find_element(By.XPATH, '//*[@id="CustomerPassword"]').send_keys('4AM185gWY.1v')
driver.find_element(By.XPATH, '//*[@id="customer_login"]/p[1]/button').click()
time.sleep(2)

#przejście do dodawania adresu
driver.find_element(By.XPATH, '//*[@id="MainContent"]/div/header/button').click()
time.sleep(1)

#Dodawanie
driver.find_element(By.XPATH, '//*[@id="AddressFirstNameNew"]').clear()
driver.find_element(By.XPATH, '//*[@id="AddressFirstNameNew"]').send_keys('Dawid')

driver.find_element(By.XPATH, '//*[@id="AddressLastNameNew"]').clear()
driver.find_element(By.XPATH, '//*[@id="AddressLastNameNew"]').send_keys('Kowalski')

driver.find_element(By.XPATH, '//*[@id="AddressCompanyNew"]').clear()
driver.find_element(By.XPATH, '//*[@id="AddressCompanyNew"]').send_keys('FTX.com')

driver.find_element(By.XPATH, '//*[@id="AddressAddress1New"]').clear()
driver.find_element(By.XPATH, '//*[@id="AddressAddress1New"]').send_keys('XXI wieku 20/28')

driver.find_element(By.XPATH, '//*[@id="AddressCityNew"]').clear()
driver.find_element(By.XPATH, '//*[@id="AddressCityNew"]').send_keys('Sosnowiec')

driver.find_element(By.XPATH, '//*[@id="AddressZipNew"]').clear()
driver.find_element(By.XPATH, '//*[@id="AddressZipNew"]').send_keys('24-400')

driver.find_element(By.XPATH, '//*[@id="AddressPhoneNew"]').clear()
driver.find_element(By.XPATH, '//*[@id="AddressPhoneNew"]').send_keys('465893489')
driver.find_element(By.XPATH, '//*[@id="address_default_address_9513694396751"]').click()

driver.find_element(By.XPATH, '//*[@id="addresses-add-submit"]').click()
time.sleep(2)

a = driver.find_element(By.XPATH, '//*[@id="MainContent"]/div/p[2]/text()[1]')

if a.text == "Dawid Kowalski":
    print("TC029-Done.")
else:
    print("TC029-nieudane. Aktualny adres to:", a)
driver.quit()
