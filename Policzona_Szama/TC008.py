import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#Konto musi być zarejestrowane.
driver = webdriver.Firefox()
driver.get("https://policzona-szama.pl/")
time.sleep(1)

driver.find_element(By.XPATH, '//*[@id="SiteHeader"]/div[1]/div[1]/div/div[4]/div/div[1]/a[2]/span').click()
time.sleep(1)

driver.find_element(By.XPATH, '//*[@id="CustomerEmail"]').send_keys("pmazur@gmail.com")
driver.find_element(By.XPATH, '//*[@id="CustomerPassword"]').send_keys("hdyui6o.0")
driver.find_element(By.XPATH, '/html/body/div[3]/div/main/div/div[2]/form/p[1]/button').click()
time.sleep(20)
a = driver.current_url

if a == "https://policzona-szama.pl/account/login":
    print("TC008-done")
else:
    print("TC008-nieudane. Aktualny adres to", a)
driver.quit()