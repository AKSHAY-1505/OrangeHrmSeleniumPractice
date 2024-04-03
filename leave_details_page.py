from base_class import BaseClass

class LeaveDetailsPage(BaseClass):
    def cancel_leave(self):
        cancel_button = self.get_by_xpath("(//button[text()= ' Cancel '])[1]")
        cancel_button.click()
