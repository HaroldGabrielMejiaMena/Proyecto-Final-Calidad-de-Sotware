from faker import Faker

fake = Faker()

def generate_brand_data():
    return {
        "name": fake.name(),
    }