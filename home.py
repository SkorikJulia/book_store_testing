
        # 1. Откройте http://practice.automationtesting.in/
        # 2. Проскролльте страницу вниз на 600 пикселей
        # 3. Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE"
        # 4. Нажмите на вкладку "REVIEWS"
        # 5. Поставьте 5 звёзд
        # 6. Заполните поле "Review" сообщением: "Nice book!"
        # 7. Заполните поле "Name"
        # 8. Заполните "Email"
        # 9. Нажмите на кнопку "SUBMIT"

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.implicitly_wait(20)
driver.get("http://practice.automationtesting.in/")

driver.execute_script("window.scrollBy(0,600);")
time.sleep(2)

selenium_rubi_btn = driver.find_element(By.CSS_SELECTOR, ".post-160 a")
selenium_rubi_btn.click()

reviews_btn = driver.find_element(By.CSS_SELECTOR, ".reviews_tab a")
reviews_btn.click()
time.sleep(2)

stars = driver.find_element(By.CLASS_NAME, "star-5")
stars.click()
time.sleep(2)

driver.execute_script("window.scrollBy(0,300);")
time.sleep(1)

review_field = driver.find_element(By.ID, "comment")
review_field.send_keys("Nice book!")
time.sleep(2)

name_field = driver.find_element(By.ID, "author")
name_field.send_keys("Julia")
time.sleep(2)

email_field = driver.find_element(By.ID, "email")
email_field.send_keys("julia@mail.com")
time.sleep(2)

submit_btn = driver.find_element(By.CLASS_NAME, "submit")
submit_btn.click()

driver.quit()



