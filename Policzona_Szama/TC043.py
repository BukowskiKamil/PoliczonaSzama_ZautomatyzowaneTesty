import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://policzona-szama.pl/")
driver.maximize_window()
time.sleep(1)

szukaj = driver.find_element(By.XPATH, '//*[@id="SiteHeader"]/div[1]/div[1]/div/div[3]/form/input[3]')
szukaj.send_keys("SZAMA TUNING")
szukaj.submit()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="CollectionAjaxContent"]/div[2]/div/div/div[2]/div[1]/div/a').click()
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/a[2]').click()
driver.find_element(By.XPATH, '//button[normalize-space()="Kup teraz"]').click()
time.sleep(1)
driver.find_element(By.ID, 'TextField0').send_keys('VM5%')
driver.find_element(By.XPATH, '//*[@id="Form0"]/div[1]/div/button').click()

cena = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/aside/div[2]/div/div/div/section/div[2]/div[3]/div[2]/div/div/strong').text
if cena == '16,06 zł':
    print("TC043-Done.")
else:
    print("Nieudane: Cena nie obniżyła się")
time.sleep(2)
driver.quit()
