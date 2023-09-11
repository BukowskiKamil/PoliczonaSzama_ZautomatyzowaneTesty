import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#Konto nie może być zarejestrowane.
driver = webdriver.Firefox()
driver.get("https://policzona-szama.pl/")
time.sleep(1)

driver.find_element(By.XPATH, '//*[@id="SiteHeader"]/div[1]/div[1]/div/div[4]/div/div[1]/a[2]/span').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="customer_register_link"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="FirstName"]').send_keys('Jan')
driver.find_element(By.XPATH, '//*[@id="LastName"]').send_keys('Kowalski')
driver.find_element(By.XPATH, '//*[@id="Email"]').send_keys('kowalski123@gmail.com')
driver.find_element(By.XPATH, '//*[@id="CreatePassword"]').send_keys('jK-1iuyu89huid8Iuhgtuij90.kjhG')
driver.find_element(By.XPATH, '//*[@id="register-submit"]').click()
time.sleep(2)
a = driver.current_url
if a == "https://policzona-szama.pl/":
    print("TC016-done.")
else:
    print("TC016-nieudane. Aktualny adres to:", a)
driver.quit()
