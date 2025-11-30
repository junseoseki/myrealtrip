from faker import Faker
import random

fake = Faker("ko_KR")

def generate_korean_traveler(num_people=1):
    """한국 여행자 데이터 생성 (1~num_people 명)"""
    travelers = []
    for _ in range(num_people):
        traveler = {
            "name": fake.name(),
            "phone": fake.phone_number().replace("-", ""),
            "email": fake.free_email(),
            "birth": fake.date_of_birth(minimum_age=20, maximum_age=65).strftime("%Y-%m-%d"),
            "gender": random.choice(["M", "F"]),
            "passport": fake.bothify(text="M########"),
            "special_request": fake.sentence(nb_words=random.randint(5, 10)) if random.random() > 0.7 else ""
        }
        travelers.append(traveler)
    return travelers

def generate_booking_payload(product_id=12345, date="2025-12-25"):
    """예약 API 페이로드 생성"""
    travelers = generate_korean_traveler(random.randint(1, 4))
    return {
        "productId": product_id,
        "date": date,
        "adults": len([t for t in travelers if t["gender"] == "M" or random.choice([True, False])]),  # 랜덤 성인/어린이
        "children": len(travelers) - len([t for t in travelers if t["gender"] == "M" or random.choice([True, False])]),
        "travelers": travelers,
        "totalPrice": random.randint(100000, 500000)
    }