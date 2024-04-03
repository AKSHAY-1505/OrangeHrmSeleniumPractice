from base_class import BaseClass

class LoginPage(BaseClass):
    def login(self):
        username_field = self.get_by_name('username')
        username_field.send_keys("Admin")

        password_field = self.get_by_name('password')
        password_field.send_keys("admin123")

        login_button = self.get_by_xpath('//button[normalize-space("Login")]')
        login_button.click()
