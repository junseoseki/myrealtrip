from playwright.sync_api import Page, expect
from .base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.search_input = page.locator('input[placeholder*="여행지"]')
        self.search_button = page.get_by_role("button", name="검색")

    def open(self):
        self.page.goto("http://localhost:8000/")
        # 확실하게 로딩 완료 기다리기
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_selector("data-loaded=true", timeout=30000)
        expect(self.search_input).to_be_visible(timeout=10000)

    def search(self, keyword: str):
        self.search_input.fill(keyword)
        self.search_button.click()
        self.page.wait_for_url("**/search**", timeout=10000)