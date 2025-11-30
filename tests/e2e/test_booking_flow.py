import pytest
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.product_detail_page import ProductDetailPage
from pages.cart_page import CartPage
from pages.booking_page import BookingPage
from data.fake_traveler import generate_korean_traveler

@pytest.mark.e2e
def test_full_booking_flow(page):
    traveler = generate_korean_traveler()

    HomePage(page).open()
    HomePage(page).search("제주도")
    SearchResultsPage(page).open_first_product()

    detail = ProductDetailPage(page)
    detail.select_date("2025-12-25")
    detail.set_people(2)
    detail.add_to_cart()

    CartPage(page).go_to_booking()
    booking = BookingPage(page)
    booking.fill_traveler_info(traveler)
    booking.submit_booking()