        # 1. Откройте http://practice.automationtesting.in/
        # 2. Нажмите на вкладку "My Account Menu"
        # 3. В разделе "Register", введите email для регистрации
        # 4. В разделе "Register", введите пароль для регистрации
        # 5. Нажмите на кнопку "Register"

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.implicitly_wait(20)
driver.get("http://practice.automationtesting.in/")

my_account = driver.find_element(By.LINK_TEXT, "My Account")
my_account.click()

email_reg = driver.find_element(By.ID, "reg_email")
email_reg.send_keys("julia@mail.com")
time.sleep(1)

pass_reg = driver.find_element(By.ID, "reg_password")
pass_reg.send_keys("Esuhub38")
time.sleep(1)

reg_btn = driver.find_element(By.CSS_SELECTOR, ".woocomerce-FormRow .woocommerce-Button")
reg_btn.click()
time.sleep(1)

driver.quit()

###############################

        # 1. Откройте http://practice.automationtesting.in/
        # 2. Нажмите на вкладку "My Account Menu"
        # 3. В разделе "Login", введите email для логина
        # 4. В разделе "Login", введите пароль для логина
        # 5. Нажмите на кнопку "Login"
        # 6. Добавьте проверку, что на странице есть элемент "Logout"
'''
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.implicitly_wait(20)
driver.get("http://practice.automationtesting.in/")

my_account = driver.find_element(By.LINK_TEXT, "My Account")
my_account.click()

email_log = driver.find_element(By.ID, "username")
email_log.send_keys("julia@mail.com")
time.sleep(1)

pass_log = driver.find_element(By.ID, "password")
pass_log.send_keys("Esuhub38")
time.sleep(1)

log_btn = driver.find_element(By.CSS_SELECTOR, ".form-row .woocommerce-Button")
log_btn.click()
time.sleep(1)

logout_check = driver.find_element(By.LINK_TEXT, "Logout")
logout_check_text = logout_check.text
assert logout_check_text == "Logout"

driver.quit()
'''