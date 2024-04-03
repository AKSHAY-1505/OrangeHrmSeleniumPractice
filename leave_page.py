from base_class import BaseClass

class LeavePage(BaseClass):
    def click_on_apply_button(self):
        apply_button = self.get_by_xpath('//a[text() = "Apply"]')
        apply_button.click()
