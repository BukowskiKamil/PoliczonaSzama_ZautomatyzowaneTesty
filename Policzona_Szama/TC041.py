import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://policzona-szama.pl/")
driver.maximize_window()
time.sleep(2)

flaga = driver.find_element(By.XPATH, '//*[@id="shopify-block-f4a051e2-c85d-4de3-8076-515e537883ea"]/div/div/section/div[1]')
driver.execute_script("arguments[0].scrollIntoView();", flaga)
time.sleep(1)

ata = driver.find_elements(By.CLASS_NAME, "jdgm-carousel-item__review-title")
print(len(ata))
if len(ata) == 15:
    print("TC041-Done")
else:
    print("TC041-nieudane")
driver.quit()