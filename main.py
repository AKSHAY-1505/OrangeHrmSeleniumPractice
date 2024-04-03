from selenium import webdriver

from login_page import LoginPage
from dashboard_page import DashboardPage
from leave_page import LeavePage
from apply_page import ApplyPage
from my_leaves_page import MyLeavesPage
from leave_details_page import LeaveDetailsPage
from base_class import BaseClass

def main():
    driver = webdriver.Chrome()
    base_obj = BaseClass(driver)
    base_obj.get_url()

    login_page = LoginPage(driver)
    login_page.login()

    dashboard_page = DashboardPage(driver)
    dashboard_page.click_on_leave()

    leave_page = LeavePage(driver)
    leave_page.click_on_apply_button()

    apply_page = ApplyPage(driver)
    apply_page.set_leave_type()
    apply_page.set_from_date()
    apply_page.set_to_date()
    apply_page.set_partial_days()
    apply_page.set_duration()
    apply_page.set_comment()
    apply_page.apply_leave()
    apply_page.navigate_to_my_leaves()

    my_leaves_page = MyLeavesPage(driver)
    my_leaves_page.view_leave_details()

    leave_details_page = LeaveDetailsPage(driver)
    leave_details_page.cancel_leave()
    leave_details_page.log_out()

if __name__ == "__main__":
    main()

