from playwright.sync_api import Page, Locator

class BasePage:
    BASE_URL = "https://www.myrealtrip.com"
    
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, path: str = "/"):
        self.page.goto(f"{self.BASE_URL}{path}", timeout=90000)
        self.page.wait_for_load_state("domcontentloaded", timeout=60000)

    def wait_for_load(self):
        self.page.wait_for_load_state("networkidle")

    def screenshot(self, name: str):
        self.page.screenshot(path=f"reports/screenshots/{name}.png", full_page=True)