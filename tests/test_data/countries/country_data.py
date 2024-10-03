from faker import Faker

fake = Faker()

def generate_country_data():
    return {
        "name": fake.unique.country() + "_" + fake.unique.word(),
        "available": fake.boolean()
    }
    
def generate_city_data(country_id):
    return {
        "name": fake.unique.city() + "_" + fake.unique.word(),
        "available": fake.boolean(),
        "countryId": country_id
    }

def generate_department_data(country_id):
    return {
        "name": fake.unique.company()+ "_" + fake.unique.word(),
        "countryId": country_id
    }