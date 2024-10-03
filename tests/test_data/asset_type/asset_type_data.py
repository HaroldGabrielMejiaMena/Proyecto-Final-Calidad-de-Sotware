from faker import Faker

fake = Faker()

def generate_asset_type_data():
    return {
        "name": fake.word(),  
        "parAssetCategoryId": fake.random_element(elements=[1, 2])  
    }
