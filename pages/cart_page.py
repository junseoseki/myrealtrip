from playwright.sync_api import Page, expect
from .base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.proceed_button = page.get_by_role("button", name="예약하기")

    def go_to_booking(self):
        self.proceed_button.click()
        self.page.wait_for_url("**/booking**")