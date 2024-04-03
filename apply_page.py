from base_class import BaseClass

class ApplyPage(BaseClass):
    def set_leave_type(self):
        dropdown = self.get_by_xpath('//div[text() = "-- Select --"]')
        dropdown.click()

        option = self.get_by_xpath('//div[@role = "listbox"]//span')
        option.click()

    def set_from_date(self):
        from_calendar_button = self.get_by_xpath('//label[text() = "From Date"]/../following-sibling::div//i')
        from_calendar_button.click()

        from_date = self.get_by_xpath("//div[contains(@class, 'oxd-calendar-date') and text()='18']")
        from_date.click()

    def set_to_date(self):
        to_calendar_button = self.get_by_xpath('//label[text() = "To Date"]/../following-sibling::div//i')
        to_calendar_button.click()

        to_date = self.get_by_xpath("//label[text() = 'To Date']/../following-sibling::div//i/../following-sibling::div//div[contains(@class, 'oxd-calendar-date') and text()='20']")
        to_date.click()

    def set_partial_days(self):
        partial_days_dropdown = self.get_by_xpath("//label[text() = 'Partial Days']/../following-sibling::div")
        partial_days_dropdown.click()

        all_days_option = self.get_by_xpath("//label[text() = 'Partial Days']/../following-sibling::div//span[text() = 'All Days']")
        all_days_option.click()

    def set_duration(self):
        duration_dropdown = self.get_by_xpath("//label[text() = 'Duration']/../following-sibling::div")
        duration_dropdown.click()

        half_day_morning_option = self.get_by_xpath("//label[text() = 'Duration']/../following-sibling::div//span[text() = 'Half Day - Morning']")
        half_day_morning_option.click()

    def set_comment(self):
        comment_box = self.get_by_xpath("//label[text() = 'Comments']/../following-sibling::div/textarea")
        comment_box.send_keys("Test Comment Akshay")

    def apply_leave(self):
        apply_button = self.get_by_xpath("//button[normalize-space(text() = 'Apply') and @type = 'submit']")
        apply_button.click()

    def navigate_to_my_leaves(self):
        my_leaves_button = self.get_by_xpath("//a[text() = 'My Leave']")
        my_leaves_button.click()

