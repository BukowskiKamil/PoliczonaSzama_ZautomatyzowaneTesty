import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#Przy każdym teście należy zmienić dane do rejestracji na nowe.

driver = webdriver.Firefox()
driver.get("https://policzona-szama.pl/")
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="SiteHeader"]/div[1]/div[1]/div/div[4]/div/div[1]/a[2]/span').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="customer_register_link"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="FirstName"]').send_keys("Jan")
driver.find_element(By.XPATH, '//*[@id="LastName"]').send_keys("Kowalski")
driver.find_element(By.XPATH, '//*[@id="Email"]').send_keys("malykranik@gmail.com")
driver.find_element(By.XPATH, '//*[@id="CreatePassword"]').send_keys("4AM185gWY.1v")
driver.find_element(By.XPATH, '//*[@id="register-submit"]').click()
time.sleep(3)
a = driver.title

if a == "Policzona Szama - Wszystko by odżywiać się lepiej":
    print("TC001-done")
else:
    print("TC001-nieudane")
driver.quit()