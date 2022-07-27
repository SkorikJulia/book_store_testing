        # 1. Откройте http://practice.automationtesting.in/
        # 2. Залогиньтесь
        # 3. Нажмите на вкладку "Shop"
        # 4. Откройте книгу "HTML 5 Forms"
        # 5. Добавьте тест, что заголовок книги назвается: "HTML5 Forms"
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

shop_menu = driver.find_element(By.LINK_TEXT, "Shop")
shop_menu.click()

book_html = driver.find_element(By.CSS_SELECTOR, ".post-181 a")
book_html.click()

book_name = driver.find_element(By.CSS_SELECTOR, ".summary h1")
book_name_text = book_name.text
assert book_name_text == "HTML5 Forms"
print('Book name is ', book_name_text)

driver.quit()
'''

###########################################

        # 1. Откройте http://practice.automationtesting.in/
        # 2. Залогиньтесь
        # 3. Нажмите на вкладку "Shop"
        # 4. Откройте категорию "HTML"
        # 5. Добавьте тест, что отображается три товара
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

shop_menu = driver.find_element(By.LINK_TEXT, "Shop")
shop_menu.click()

html_category = driver.find_element(By.CSS_SELECTOR, ".cat-item-19 a")
html_category.click()

book_quantity = driver.find_elements(By.XPATH, "//ul[@class='products masonry-done']/li")
print(len(book_quantity), 'книги в категории')

book_quantity = driver.find_elements(By.CSS_SELECTOR, ".product.type-product")
if len(book_quantity) == 3:
    print('В категории 3 книги')
else:
    print("Ошибка. Количество книг в категории: " + str(len(book_quantity)))
driver.quit()
'''

#################################################

        # 1. Откройте http://practice.automationtesting.in/
        # 2. Залогиньтесь
        # 3. Нажмите на вкладку "Shop"
        # 4. Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию
        # 5. Отсортируйте товары по цене от большей к меньшей
        # 6. Добавьте тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей
'''
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
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
#ime.sleep(1)

log_btn = driver.find_element(By.CSS_SELECTOR, ".form-row .woocommerce-Button")
log_btn.click()
time.sleep(1)

shop_menu = driver.find_element(By.LINK_TEXT, "Shop")
shop_menu.click()

selector = driver.find_element(By.CLASS_NAME, "orderby")
selector_default_check = selector.get_attribute("value")
assert selector_default_check == "menu_order"

selector_sort = Select(selector)
selector_sort.select_by_index(5)

selector = driver.find_element(By.CLASS_NAME, "orderby")
selector_price_check = selector.get_attribute("value")
assert selector_price_check == "price-desc"

driver.quit()
'''

###############################################

        # 1. Откройте http://practice.automationtesting.in/
        # 2. Залогиньтесь
        # 3. Нажмите на вкладку "Shop"
        # 4. Откройте книгу "Android Quick Start Guide"
        # 5. Добавьте тест, что содержимое старой цены = "₹600.00"
        # 6. Добавьте тест, что содержимое новой цены = "₹450.00"
        # 7. Добавьте явное ожидание и нажмите на обложку книги
        # 8. Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)
'''
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
ime.sleep(1)

log_btn = driver.find_element(By.CSS_SELECTOR, ".form-row .woocommerce-Button")
log_btn.click()
time.sleep(1)

shop_menu = driver.find_element(By.LINK_TEXT, "Shop")
shop_menu.click()

book_android = driver.find_element(By.CSS_SELECTOR, ".post-169 a")
book_android.click()

old_price = driver.find_element(By.CSS_SELECTOR, "del .woocommerce-Price-amount")
old_price_get_text = old_price.text
assert old_price_get_text == "₹600.00"

new_price = driver.find_element(By.CSS_SELECTOR, "ins .woocommerce-Price-amount")
new_price_get_text = new_price.text
assert new_price_get_text == "₹450.00"

wait = WebDriverWait(driver, 10)
book_img = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "images"))).click()

close_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "pp_close"))).click()

driver.quit()
'''

##############################################

        # 1. Откройте http://practice.automationtesting.in/
        # 2. Нажмите на вкладку "Shop"
        # 3. Добавьте в корзину книгу "HTML5 WebApp Development"
        # 4. Добавьте тест, что возле коризны(вверху справа) количество товаров = "1 Item", а стоимость = "₹180.00"
        # 5. Перейдите в корзину
        # 6. Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
        # 7. Используя явное ожидание, проверьте что в Total отобразилась стоимость
'''
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

#driver.implicitly_wait(20)
driver.get("http://practice.automationtesting.in/")

shop_menu = driver.find_element(By.LINK_TEXT, "Shop")
shop_menu.click()

add_cart_btn = driver.find_element(By.CSS_SELECTOR, "li.post-182>.button").click()
time.sleep(5)

cart = driver.find_element(By.CLASS_NAME, "wpmenucart-contents")
cart_check = cart.text
assert "1 Item" in cart_check
assert "₹180.00" in cart_check

cart.click()

wait = WebDriverWait(driver, 10)
subtotal = wait.until(EC.presence_of_element_located((By.XPATH, "//tr [@class='cart-subtotal']/td/span")))
total = wait.until(EC.presence_of_element_located((By.XPATH, "//tr[@class='order-total']/td/strong")))

driver.quit()
'''

################################################

        # 1. Откройте http://practice.automationtesting.in/
        # 2. Нажмите на вкладку "Shop"
        # 3. Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
        # 4. Перейдите в корзину
        # 5. Удалите первую книгу
        # 6. Нажмите на Undo (отмена удаления)
        # 7. В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“
        # 8. Нажмите на кнопку "UPDATE BASKET"
        # 9. Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3
        # 10. Нажмите на кнопку "APPLY COUPON"
        # 11. Добавьте тест, что возникло сообщение: "Please enter a coupon code."
'''
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.implicitly_wait(20)
driver.get("http://practice.automationtesting.in/")

shop_menu = driver.find_element(By.LINK_TEXT, "Shop")
shop_menu.click()

driver.execute_script("window.scrollBy(0,300);")

book_1_add = driver.find_element(By.CSS_SELECTOR, "li.post-182>.button").click()
time.sleep(3)

book_2_add = driver.find_element(By.CSS_SELECTOR, "li.post-180>.button").click()

cart = driver.find_element(By.CLASS_NAME, "wpmenucart-contents").click()
time.sleep(3)

delete_btn = driver.find_element(By.XPATH, "//a[@data-product_id='182']").click()
time.sleep(3)

undo_link = driver.find_element(By.LINK_TEXT, "Undo?").click()
time.sleep(1)

quantity_field = driver.find_element(By.XPATH, "//input[@name='cart[045117b0e0a11a242b9765e79cbf113f][qty]']")
quantity_field.clear()
time.sleep(1)
quantity_field.send_keys("3")
time.sleep(3)

coupon_btn = driver.find_element(By.CSS_SELECTOR, "div.coupon .button").click()
time.sleep(3)

coupon_massage = driver.find_element(By.CLASS_NAME, "woocommerce-error").text
assert coupon_massage == "Please enter a coupon code."
print(coupon_massage)

driver.quit()
'''

############################################

        # 1. Откройте http://practice.automationtesting.in/
        # 2. Нажмите на вкладку "Shop" и проскролльте на 300 пикселей вниз
        # 3. Добавьте в корзину книгу "HTML5 WebApp Development"
        # 4. Перейдите в корзину
        # 5. Нажмите "PROCEED TO CHECKOUT"
        # 6. Заполните все обязательные поля
        # 7. Выберите способ оплаты "Check Payments"
        # 8. Нажмите PLACE ORDER
        # 9. Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
        # 10. Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()

driver.implicitly_wait(20)
driver.get("http://practice.automationtesting.in/")

shop_menu = driver.find_element(By.LINK_TEXT, "Shop")
shop_menu.click()

driver.execute_script("window.scrollBy(0,300);")

book_1_add = driver.find_element(By.CSS_SELECTOR, "li.post-182>.button").click()
time.sleep(3)

cart = driver.find_element(By.CLASS_NAME, "wpmenucart-contents").click()
time.sleep(3)

wait = WebDriverWait(driver, 20)
checkout_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button.button.alt.wc-forward"))).click()

first_name_field = wait.until(EC.element_to_be_clickable((By.ID, "billing_first_name"))).send_keys("Julia")

last_name = driver.find_element(By.ID, "billing_last_name").send_keys("Skorik")

email = driver.find_element(By.ID, "billing_email").send_keys("julia_skorik@mail.ru")

phone = driver.find_element(By.ID, "billing_phone").send_keys("78951456825")

country_selector = driver.find_element(By.CSS_SELECTOR, "#s2id_billing_country .select2-arrow").click()
country_field = driver.find_element(By.ID, "s2id_autogen1_search").send_keys("Russia")
country = driver.find_element(By.ID, "select2-results-1").click()
time.sleep(1)

driver.execute_script("window.scrollBy(0,600);")
time.sleep(3)

address_1 = driver.find_element(By.ID, "billing_address_1").send_keys("Mayakovskogo")
address_2 = driver.find_element(By.ID, "billing_address_2").send_keys("12")
time.sleep(1)

town = driver.find_element(By.ID, "billing_city").send_keys("Voronezh")
state = driver.find_element(By.ID, "billing_state").send_keys("Voronezh")
postcode = driver.find_element(By.ID, "billing_postcode").send_keys("86420")

pay_method = driver.find_element(By.ID, "payment_method_cheque").click()

place_order_btn = driver.find_element(By.ID, "place_order").click()

present_text_1 = wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))

present_text_2 = wait.until(EC.text_to_be_present_in_element((By.XPATH, "//td[text() = 'Check Payments']"), "Check Payments"))

driver.quit()