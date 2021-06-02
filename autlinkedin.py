from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome('./chromedriver.exe')
driver.get("https://linkedin.com")

username = driver.find_element_by_xpath("//input[@name='session_key']")
password = driver.find_element_by_xpath("//input[@name='session_password']")

time.sleep(2)

username.send_keys("parodi-14@hotmail.com")
password.send_keys("aparodi123")
#password = open('password.txt.txt').read().strip()


submit = driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(2)


driver.get("https://www.linkedin.com/search/results/people/?network=%5B%22F%22%5D&origin=FACETED_SEARCH")
time.sleep(2)

all_buttons = driver.find_elements_by_tag_name("button")

# for btn in all_buttons:
message_buttons = [btn for btn in all_buttons if btn.text == "Enviar mensaje"]
message_buttons[0].click()
time.sleep(2)
# for i in message_buttons:
#     i.click()

main_div = driver.find_element_by_xpath("//div[starts-with(@class, 'msg-form__msg-content-container')]")
main_div.click()

paragraphs = driver.find_elements_by_tag_name("p")
paragraphs[-5].send_keys("Hola! por favor sigue mi página https://www.linkedin.com/company/codeecuador/?viewAsMember=true")

