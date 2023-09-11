import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#Konto nie może być zarejestrowane.
driver = webdriver.Firefox()
driver.get("https://policzona-szama.pl/")
time.sleep(1)

driver.find_element(By.XPATH, '//*[@id="SiteHeader"]/div[1]/div[1]/div/div[4]/div/div[1]/a[2]/span').click()
time.sleep(1)

driver.find_element(By.XPATH, '//*[@id="RecoverPassword"]').click()
driver.find_element(By.XPATH, '//*[@id="RecoverEmail"]').send_keys("pmazur@gmail.com")
driver.find_element(By.XPATH, '//*[@id="RecoverPasswordForm"]/div/form/p/button').click()
time.sleep(2)
a = driver.find_element(By.XPATH, '//*[@id="RecoverPasswordForm"]/div/form/div/ul/li/text()')
if a.text == "Nie znaleziono konta z tym e-mailem.":
    print("TC007-done")
else:
    print("TC007-nieudane")
driver.quit()