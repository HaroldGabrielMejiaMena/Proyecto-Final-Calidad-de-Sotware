from faker import Faker


fake = Faker()

# Generar datos para un modelo comercial
def generate_commercial_model_data():
    return {
        "name": fake.company(), 
        "parModelTypeId": 3,  
        "modCommercialModelId": None  
    }

# Generar datos para un modelo de fábrica
def generate_factory_model_data(commercial_model_id):
    return {
        "name": fake.company(),  
        "parModelTypeId": 4,  
        "modCommercialModelId": commercial_model_id

    }
