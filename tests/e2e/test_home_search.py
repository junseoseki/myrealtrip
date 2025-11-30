import pytest
from pages.home_page import HomePage

@pytest.mark.e2e
@pytest.mark.smoke
def test_home_search_flow(page):
    home = HomePage(page)
    home.navigate()  # 이제 https://www.myrealtrip.com/ 로 가짐
    home.search("제주도")
    # 검증: 검색 결과 페이지 로드
    assert "제주도" in page.title()
    page.screenshot(path="reports/screenshots/search-success.png")