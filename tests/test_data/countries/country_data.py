from faker import Faker

fake = Faker()

def generate_country_data():
    return {
        "name": fake.country(),
        "available": fake.boolean()
    }