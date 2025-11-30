from playwright.sync_api import Page, expect
from .base_page import BasePage

class ProductDetailPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.date_picker = page.locator("[data-testid='date-picker']")
        self.people_input = page.locator("input[name='people']")
        self.add_to_cart_btn = page.get_by_text("장바구니 담기")

    def select_date(self, date: str):
        self.date_picker.click()
        self.page.get_by_text(date, exact=True).click()

    def set_people(self, count: int):
        self.people_input.fill(str(count))

    def add_to_cart(self):
        self.add_to_cart_btn.click()
        expect(self.page.get_by_text("장바구니에 담겼습니다")).to_be_visible()