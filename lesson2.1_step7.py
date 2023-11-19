from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "img[id = treasure]")
    x = x_element.get_attribute('valuex')
    y = calc(x)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    checkbox = browser.find_element(By.CSS_SELECTOR, ".check-input[type='checkbox']")
    checkbox.click()
    radio = browser.find_element(By.CSS_SELECTOR, ".check-input[id = robotsRule]")
    radio.click()

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
