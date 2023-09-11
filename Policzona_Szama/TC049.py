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
driver.find_element(By.XPATH, '//*[@id="HeaderCart"]/div/form/div[1]/div[1]/div/div/div[2]/div[2]/div[1]/div[1]/button[2]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="HeaderCart"]/div/form/div[1]/div[1]/div/div/div[2]/div[2]/div[1]/div[1]/button[2]').click()
time.sleep(1)

nazwa_1 = driver.find_element(By.XPATH, '//*[@id="HeaderCart"]/div/form/div[1]/div[1]/div/div/div[2]/div[1]/a')
nazwa_1t = nazwa_1.text
print("Nazwa produktu w mini koszyku:", nazwa_1t)
cena_1 = driver.find_element(By.XPATH, '//*[@id="HeaderCart"]/div/form/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/span/span[1]')
cena_1t = cena_1.text
print("Cena produktu w mini koszyku:", cena_1t, "(Cena podana w groszach)")

driver.get("https://policzona-szama.pl/cart")
time.sleep(1)
nazwa_2 = driver.find_element(By.XPATH, '//*[@id="CartPageForm"]/div/div[1]/div/div/div[2]/div[1]/a')
nazwa_2t = nazwa_2.text
print("Nazwa produktu w koszyku:", nazwa_2t)
cena_2 = driver.find_element(By.XPATH, '//*[@id="CartPageForm"]/div/div[1]/div/div/div[2]/div[2]/div[2]/span/span[1]')
cena_2t = cena_2.text
print("Cena produktu w koszyku:", cena_2t, "(Cena podana w groszach)")

if nazwa_1t == nazwa_2t and cena_1t == cena_2t:
    print("TC049-Done.")
else:
    print("Niudane")




time.sleep(3)
driver.quit()