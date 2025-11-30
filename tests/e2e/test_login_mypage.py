import pytest
from pages.mypage_page import MyPage

@pytest.mark.e2e
def test_mypage_has_booking(page):
    page.goto("/my/bookings")
    mypage = MyPage(page)
    mypage.verify_booking_exists()