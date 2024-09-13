from faker import Faker

fake = Faker()

def generate_building_data():
    return {
        "name": fake.company(),  
        "direction": fake.street_address()
    }