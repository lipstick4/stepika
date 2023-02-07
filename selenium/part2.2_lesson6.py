from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math


def calc(x):
  return  str(math.log(abs(12*math.sin(int(x)))))
 

try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text   
    y = calc(x)



    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()

    browser.execute_script("window.scrollBy(0, 100);")
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()
    

    # Отправляем заполненную форму
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()