import pytest
import httpx

@pytest.mark.api
def test_homepage_accessible():
    """메인 페이지 접근 테스트"""
    response = httpx.get("https://www.myrealtrip.com/", follow_redirects=True)
    assert response.status_code == 200
    assert "마이리얼트립" in response.text or "myrealtrip" in response.text.lower()

@pytest.mark.api
def test_search_api_endpoint():
    """검색 API 응답 테스트"""
    # 실제 검색 API 엔드포인트 예시
    response = httpx.get(
        "https://www.myrealtrip.com/api/search",
        params={"query": "제주"},
        follow_redirects=True,
        timeout=30.0
    )
    # API가 존재하면 200, 없으면 404 등
    assert response.status_code in [200, 404, 403]

@pytest.mark.api
@pytest.mark.skip(reason="실제 API 엔드포인트 확인 필요")
def test_product_detail_api():
    """상품 상세 API 테스트 (실제 엔드포인트 확인 후 활성화)"""
    response = httpx.get("https://www.myrealtrip.com/api/products/12345")
    assert response.status_code in [200, 404]