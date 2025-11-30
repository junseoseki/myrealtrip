from playwright.sync_api import Page, expect
from .base_page import BasePage

class MyPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.booking_list = page.locator("div.booking-item")

    def verify_booking_exists(self):
        expect(self.booking_list).to_have_count(1, timeout=10000)