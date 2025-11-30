from playwright.sync_api import Page, expect
from .base_page import BasePage

class SearchResultsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.product_cards = page.locator("a[data-testid*='product-card']")
        self.first_product = self.product_cards.first

    def verify_results_loaded(self):
        expect(self.product_cards).to_have_count(10, timeout=15000)

    def open_first_product(self):
        with self.page.expect_navigation():
            self.first_product.click()