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

#dojście do edycji
driver.find_element(By.XPATH, '//*[@id="MainContent"]/div/div/div[2]/p[3]/a').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="MainContent"]/div/p[3]/button[1]').click()
time.sleep(1)

#edycja
driver.find_element(By.XPATH, '//*[@id="AddressFirstName_9513694396751"]').clear()
driver.find_element(By.XPATH, '//*[@id="AddressFirstName_9513694396751"]').send_keys('Dawid')

driver.find_element(By.XPATH, '//*[@id="AddressLastName_9513694396751"]').clear()
driver.find_element(By.XPATH, '//*[@id="AddressLastName_9513694396751"]').send_keys('Kowalski')

driver.find_element(By.XPATH, '//*[@id="AddressCompany_9513694396751"]').clear()
driver.find_element(By.XPATH, '//*[@id="AddressCompany_9513694396751"]').send_keys('FTX.com')

driver.find_element(By.XPATH, '//*[@id="AddressAddress1_9513694396751"]').clear()
driver.find_element(By.XPATH, '//*[@id="AddressAddress1_9513694396751"]').send_keys('XXI wieku 20/28')

driver.find_element(By.XPATH, '//*[@id="AddressCity_9513694396751"]').clear()
driver.find_element(By.XPATH, '//*[@id="AddressCity_9513694396751"]').send_keys('Sosnowiec')

driver.find_element(By.XPATH, '//*[@id="AddressZip_9513694396751"]').clear()
driver.find_element(By.XPATH, '//*[@id="AddressZip_9513694396751"]').send_keys('24-400')

driver.find_element(By.XPATH, '//*[@id="AddressPhone_9513694396751"]').clear()
driver.find_element(By.XPATH, '//*[@id="AddressPhone_9513694396751"]').send_keys('465893489')
driver.find_element(By.XPATH, '//*[@id="address_default_address_9513694396751"]').click()

driver.find_element(By.XPATH, '//*[@id="addresses-update-submit"]').click()
time.sleep(2)

a = driver.find_element(By.XPATH, '//*[@id="MainContent"]/div/p[2]/text()[1]')

if a.text == "Dawid Kowalski":
    print("TC027-Done.")
else:
    print("TC027-nieudane. Aktualny adres to:", a)
driver.quit()
