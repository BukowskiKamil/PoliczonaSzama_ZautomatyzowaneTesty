import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://policzona-szama.pl/")
driver.maximize_window()
time.sleep(1)

driver.find_element(By.XPATH, '//*[@id="CollectionSection-template--18283104076111__dfc7ee7e-4c92-45ab-840b-780c14ce2816"]/div[2]/div/div[3]/div/a').click()
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/a[2]').click()
driver.find_element(By.XPATH, "//button[@name='add']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//button[@name='add']").click()
time.sleep(1)
liczba = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div/div/header/div[4]/div/div[1]/div/form/div[1]/div[1]/div/div/div[2]/div[2]/div[1]/div[1]/input').get_attribute("value")
if liczba == "2":
    print("TC046-Done.")
else:
    print("Nieudane.")

time.sleep(1)
driver.quit()
