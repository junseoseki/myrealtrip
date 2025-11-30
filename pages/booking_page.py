from playwright.sync_api import Page, expect
from .base_page import BasePage
from data.fake_traveler import generate_korean_traveler

class BookingPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def fill_traveler_info(self, traveler: dict):
        self.page.fill("input[name='name']", traveler["name"])
        self.page.fill("input[name='phone']", traveler["phone"])
        self.page.fill("input[name='email']", traveler["email"])

    def submit_booking(self):
        self.page.get_by_role("button", name="결제하기").click()
        expect(self.page.get_by_text("예약 완료")).to_be_visible(timeout=20000)