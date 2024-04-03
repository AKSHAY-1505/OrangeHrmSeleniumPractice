from base_class import BaseClass

class MyLeavesPage(BaseClass):
    def view_leave_details(self):
        three_dot_button = self.get_by_xpath("//div[@class = 'oxd-table-card']//button[text() = ' Cancel ']//ancestor::div//div[text() = 'Test Comment Akshay']/parent::div/following-sibling::div//li/button")
        three_dot_button.click()

        view_leave_details_button = self.get_by_xpath("//ul[@class = 'oxd-dropdown-menu']//p[text() = 'View Leave Details']")
        view_leave_details_button.click()
