# -*- coding: utf-8 -*-
""" ********************************
autor : aaron.parodip@codeecuador.com

ultima vez editado: 8/06/2021 10:25
*********************************"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os
import wget
import time

driver = webdriver.Chrome('chromedriver.exe') # Driver de chrome para el robot
driver.get("https://www.instagram.com/") # Url semilla

username = WebDriverWait(driver, 10).until\
    (EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']"))) # Elemento Clickeable mediante sentencia CSS
password = WebDriverWait(driver, 10).until\
    (EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

username.clear()
password.clear()

# ********* Datos de inicio de Sessión ********* #
username.send_keys("codeecuadoroficial")
clave = open('clave IG.txt').readline().strip()
password.send_keys(clave)

button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable
                                        ((By.CSS_SELECTOR, "button[type='submit']"))).click()

not_now = WebDriverWait(driver, 10).until\
    (EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Ahora no")]'))).click() # Clikea en las ventanas emergentes
not_now2 = WebDriverWait(driver, 10).until\
    (EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Ahora no")]'))).click() # Clikea en las ventanas emergentes

searchbox = WebDriverWait(driver, 10).until\
    (EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Busca']")))
searchbox.clear()
keyword = '#Kotlin'
searchbox.send_keys(keyword)
time.sleep(5)

searchbox.send_keys(Keys.ENTER)
time.sleep(5)
searchbox.send_keys(Keys.ENTER)
time.sleep(5)


# ******* scroll down to scrape more images ******* #
driver.execute_script("window.scrollTo(0, 4000);")

#target all images on the page
images = driver.find_elements_by_tag_name('img')
images = [image.get_attribute('src') for image in images]
images = images[:-2]
print('Number of scraped images: ', len(images))

# Bajar las imagenes en la carpeta

path = os.getcwd()
path = os.path.join(path, keyword[1:] + "s")

os.mkdir(path)

counter = 0
for image in images:
    save_as = os.path.join(path, keyword[1:] + str (counter)+ '.jpg')
    wget.download(image, save_as)
    counter += 1


