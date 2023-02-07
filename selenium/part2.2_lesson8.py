from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import os 

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("y@mail.ru")
    

    current_dir = os.path.abspath(os.path.dirname(__file__))    
    file_path = os.path.join(current_dir, '11.txt')

    element = browser.find_element(By.ID, "file")
    
    element.send_keys(file_path)


    # Отправляем заполненную форму
    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
