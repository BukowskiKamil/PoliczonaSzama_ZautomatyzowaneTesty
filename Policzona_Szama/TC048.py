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
cena_w_zl = driver.find_element(By.XPATH, '//*[@id="HeaderCart"]/div/form/div[2]/div[1]/div[2]')
if cena_w_zl.text == "10110 zł":
    print("TC048 part 1/2 Done")
else:
    print("Part 1/2 nieudane")
driver.find_element(By.XPATH, '//*[@id="HeaderCart"]/div/form/div[1]/div[1]/div/div/div[2]/div[2]/div[1]/div[1]/button[1]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="HeaderCart"]/div/form/div[1]/div[1]/div/div/div[2]/div[2]/div[1]/div[1]/button[1]').click()
time.sleep(1)
cena_w_zl2 = driver.find_element(By.XPATH, '//*[@id="HeaderCart"]/div/form/div[2]/div[1]/div[2]')
if cena_w_zl2.text == "3370 zł":
    print("TC048 part 2/2 Done")
else:
    print("Part 2/2 nieudane")




time.sleep(2)
driver.quit()
