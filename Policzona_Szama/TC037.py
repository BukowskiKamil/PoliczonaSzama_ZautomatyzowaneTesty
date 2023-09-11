import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://policzona-szama.pl/")
time.sleep(1)
a = driver.find_element(By.XPATH, "//div[@class='header-item header-item--search small--hide']//input[@placeholder='Szukaj...']")
a.send_keys('D3246')
time.sleep(1)
a.submit()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="CollectionAjaxContent"]/div[2]/div/div/div[2]/div/div/a').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="AddToCartForm-template--18283104469327__main-7076462821533"]/div[2]/button').submit()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="HeaderCart"]/div/form/div[1]/div[1]/div/div/div[2]/div[2]/div[1]/div[1]/button[2]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="HeaderCart"]/div/form/div[1]/div[1]/div/div/div[2]/div[2]/div[1]/div[1]/button[2]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="HeaderCart"]/div/form/div[1]/div[1]/div/div/div[2]/div[2]/div[1]/div[1]/button[2]').click()
a = driver.find_element(By.XPATH, '//*[@id="cart_updates_41172967784605:a9121be1629516f9b4bb7d87ac62c1b3"]')
ilosc_produktow = a.get_attribute("value")

if ilosc_produktow == str(4):
    print("TC037-Done. Liczba produktów w koszyku to:", ilosc_produktow)
else:
    print("TC037-nieudane, liczba produktów w koszyku to:", ilosc_produktow)
driver.quit()
