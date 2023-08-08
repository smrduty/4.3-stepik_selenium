from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):

	def register_new_user(self, email, password):
		email_field = self.browser.find_element(*LoginPageLocators.EMAIL)
		password_field = self.browser.find_element(*LoginPageLocators.PASSWORD)
		password_confirm_field = self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRM)
		email_field.send_keys(email)
		password_field.send_keys(password)
		password_confirm_field.send_keys(password)
		registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
		registration_button.click()
