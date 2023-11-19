from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x1_element = browser.find_element(By.CSS_SELECTOR, "span[id = num1]")
    x1 = x1_element.text
    x2_element = browser.find_element(By.CSS_SELECTOR, "span[id = num2]")
    x2 = x2_element.text
    summa = str(int(x1) + int(x2))
    list_n = browser.find_element(By.CSS_SELECTOR, "option[value='{0}']".format(summa))
    list_n.click()

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
