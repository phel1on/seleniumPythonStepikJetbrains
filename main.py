import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://stepik.org/catalog?auth=login')
time.sleep(3)
driver.find_element(By.XPATH, "//input[@id='id_login_email']").send_keys('store2_korzinka@mail.ru')
driver.find_element(By.XPATH, "//input[@id='id_login_password']").send_keys('isa2516530')
driver.find_element(By.XPATH, "//*[@id="login_form"]/button)
# register

# driver.get('https://stepik.org/catalog?auth=registration')
# time.sleep(3)
# driver.find_element(By.XPATH, "//input[contains(@id, 'id_registration_full-name')]").send_keys('rick morty')
# driver.find_element(By.XPATH, "//input[contains(@id, 'id_registration_email')]").send_keys('store2_korzinka@mail.ru')
# driver.find_element(By.XPATH, "//input[contains(@id, 'id_registration_password')]").send_keys('isa2516530')
# time.sleep(3)
# driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div/div[2]/div/div/div/div/div/div/div/form/button").click()

#driver.quit()



# driver.get('https://stepik.org/catalog?auth=login')
# driver.find_element(By.XPATH, "//input[contains(@id, 'id_login_email')]").send_keys('store2_korzinka@mail.ru')
# driver.find_element(By.XPATH, "//input[contains(@id, 'id_login_password')]").send_keys('isa2516530')
# driver.find_element(By.XPATH, "/html/body/div[4]/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/button").click()
# time.sleep(3)
# driver.find_element(By.XPATH, "//input[contains(@class, 'search-form__input ')]").send_keys('поколение python')
#
# driver.find_element(By.XPATH, '/html/body/main/div[1]/div[1]/div/div/button[3]').click()


# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()