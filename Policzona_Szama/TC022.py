import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://policzona-szama.pl/")
time.sleep(1)

driver.find_element(By.XPATH, '//*[@id="SiteHeader"]/div[1]/div[1]/div/div[4]/div/div[1]/a[2]/span').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="customer_register_link"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="FirstName"]').send_keys('Jan')
driver.find_element(By.XPATH, '//*[@id="LastName"]').send_keys('Kowalski')
driver.find_element(By.XPATH, '//*[@id="Email"]').send_keys('malykranik@gmail.com')
a = driver.find_element(By.XPATH, '//*[@id="CreatePassword"]')
a.send_keys('JK-1IUYU')
time.sleep(2)

if a.text == "":
    print("TC022-Done")
else:
    print("TC022-nieudane")

driver.quit()
