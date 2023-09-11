import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#Konto musi być zarejestrowane.
driver = webdriver.Firefox()
driver.get("https://policzona-szama.pl/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="SiteHeader"]/div[1]/div[1]/div/div[4]/div/div[1]/a[2]/span').click()
time.sleep(2)

#logowanie
driver.find_element(By.XPATH, '//*[@id="CustomerEmail"]').send_keys("malykranik@gmail.com")
driver.find_element(By.XPATH, '//*[@id="CustomerPassword"]').send_keys("4AM185gWY.1v")
driver.find_element(By.XPATH, '/html/body/div[3]/div/main/div/div[2]/form/p[1]/button').click()
time.sleep(3)

#kupowanie
driver.get("https://policzona-szama.pl/")
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="CollectionSection-template--18283104076111__dfc7ee7e-4c92-45ab-840b-780c14ce2816"]/div[2]/div/div[1]/div/a').click()
time.sleep(3)
driver.find_element(By.XPATH, "//button[@name='add']").submit()
time.sleep(4)
driver.find_element(By.XPATH, '//*[@id="HeaderCart"]/div/form/div[2]/div[4]/button').click()
time.sleep(2)

#wypełnianie danych do zakupu
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("domator@gmail.com")
driver.find_element(By.XPATH, "//input[@id='TextField1']").send_keys("Daniel")
driver.find_element(By.XPATH, "//input[@id='TextField2']").send_keys("Kowalski")
driver.find_element(By.XPATH, "//input[@id='TextField3']").send_keys("Kocur Sp. z o.o.")
driver.find_element(By.XPATH, "//input[@id='TextField4']").send_keys("Wiosenna 5")
driver.find_element(By.XPATH, "//input[@id='TextField5']").send_keys("765893485")
driver.find_element(By.XPATH, "//input[@id='TextField6']").send_keys("30-450")
driver.find_element(By.XPATH, "//input[@id='TextField7']").send_keys("Tymbark")
driver.find_element(By.XPATH, "//input[@id='TextField8']").send_keys("345345345")
driver.find_element(By.XPATH, "//input[@id='save_shipping_information']").click()
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/main/form/div[1]/div/div[2]/div[2]/div/button").submit()
time.sleep(2)

#wybór wysyłki
driver.find_element(By.XPATH, '//*[@id="shipping_methods"]/div[2]/div[2]').click()
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/main/form/div[1]/div/div/div[2]/div[1]/button").submit()
time.sleep(2)

#dane do faktury
driver.find_element(By.XPATH, "//span[contains(text(),'Użyj innego adresu rozliczeniowego')]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='TextField9']").send_keys("Jan")
driver.find_element(By.XPATH, "//input[@id='TextField10']").send_keys("Kowalski")
driver.find_element(By.XPATH, "//input[@id='TextField11']").send_keys("Kocur Sp z o.o.")
driver.find_element(By.XPATH, "//input[@id='TextField12']").send_keys("Wawrzyńca 10")
driver.find_element(By.XPATH, "//input[@id='TextField13']").send_keys("765893485")
driver.find_element(By.XPATH, "//input[@id='TextField14']").send_keys("30-450")
driver.find_element(By.XPATH, "//input[@id='TextField15']").send_keys("Warszawa")
driver.find_element(By.XPATH, "//input[@id='TextField16']").send_keys("668765364")
lista = driver.find_element(By.XPATH, '//*[@id="Select1"]')
lista = Select(lista)
lista.select_by_visible_text("Polska")
driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div[2]/div/div/div/div[2]/div/div/div/main/div/form/div[1]/div/div[2]/div[1]/button").submit()
time.sleep(7)
print("TC039-Done")
driver.quit()
