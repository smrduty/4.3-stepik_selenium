from selenium.webdriver.common.by import By

class BasePageLocators():

	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	
	LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

	BASKET_LINK = (By.XPATH, "//span/a")

class ProductPageLocators():

	SUCCESS_MESSAGE = (By.CLASS_NAME, "alertinner ")

	BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, '[value="Add to basket"]')

	TEXT_AFTER_ADDING_TO_CART = (By.XPATH, '//*[@class="alertinner "]/strong')

	NAME_OF_PRODUCT = (By.XPATH, '//*[@class="col-sm-6 product_main"]/h1')

	PRICE_OF_PRODUCT = (By.XPATH, "//p[@class='price_color']")

	PRICE_AFTER_ADDING_TO_CART = (By.XPATH, '//*[@class="alertinner "]/p/strong')

class BasketPageLocators():

	BASKET_IS_NOT_EMPTY = (By.CLASS_NAME, "basket-items")
