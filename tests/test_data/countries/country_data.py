from faker import Faker

fake = Faker()

def generate_country_data():
    return {
        "name": fake.country(),
        "available": fake.boolean()
    }
    
def generate_city_data(country_id):
    return {
        "name": fake.city(),
        "available": fake.boolean(),
        "countryId": country_id
    }
