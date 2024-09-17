from time import sleep
from os import getenv 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
from dotenv import load_dotenv

LOGIN_PAGE = "https://www.saucedemo.com"

def clear_input(field) -> None:
    field.click()  # Устанавливаем курсор
    field.send_keys(Keys.END)
    field.send_keys(Keys.SHIFT, Keys.HOME)  # Выделяем текст
    field.send_keys(Keys.DELETE)  # Удаляем выделенное

def test_purchase(username, password):
    # 1. Открыть сайт
    driver.get(LOGIN_PAGE)

    # Очистка полей ввода перед вводом новых значений
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    
    clear_input(username_field)
    clear_input(password_field)
    
    # Ввод нового пароля 
    username_field.send_keys(username)
    password_field.send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    # 3. Выбор товара
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # 4. Переход в корзину
    driver.find_element(By.ID, "shopping_cart_container").click()

    # 5. Проверка, что товар добавлен
    assert "Sauce Labs Backpack" in driver.page_source

    # 6. Оформление покупки
    driver.find_element(By.ID, "checkout").click()
    driver.find_element(By.ID, "first-name").send_keys("John")
    driver.find_element(By.ID, "last-name").send_keys("Doe")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()

    # 7. Завершение покупки
    driver.find_element(By.ID, "finish").click()

    # 8. Проверка успешного завершения покупки
    assert "Thank you for your order!" in driver.page_source

if __name__ == "__main__":
    # Инициализация драйвера
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    load_dotenv()

    PASSWORD = getenv('password')
    USERNAME = getenv('username')

    try:
        test_purchase(username=USERNAME, password=PASSWORD)
    except Exception:
        print(Exception)
    finally:
        # Закрытие драйвера
        sleep(5)
        driver.quit()
        
