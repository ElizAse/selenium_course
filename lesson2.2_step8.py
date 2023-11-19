from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.XPATH, '//input[@placeholder = "Enter first name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, '//input[@placeholder = "Enter last name"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, '//input[@placeholder = "Enter email"]')
    input3.send_keys("fggdgd@gmail.com")
    element = browser.find_element(By.XPATH, "//input[@name='file']")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'test_less.txt')  # добавляем к этому пути имя файла
    element.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()