import pytest
from playwright.sync_api import Page

@pytest.mark.e2e
@pytest.mark.mobile
def test_mobile_search(page: Page):  # page: Page로 명시
    # page.set_viewport_size() 사용 (context가 아님!)
    page.set_viewport_size({"width": 375, "height": 812})  # iPhone 크기
    page.goto("https://www.myrealtrip.com/")  # 절대 URL
    page.get_by_placeholder("여행지").fill("부산")  # locator 수정 (실제 플레이스홀더로)
    page.get_by_role("button", name="검색").click()
    assert "부산" in page.url
    page.screenshot(path="reports/screenshots/mobile-search.png")