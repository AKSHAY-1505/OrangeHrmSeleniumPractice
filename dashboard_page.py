from base_class import BaseClass

class DashboardPage(BaseClass):
    def click_on_leave(self):
        leave_button = self.get_by_xpath("//span[text() = 'Leave']/..")
        leave_button.click()
