from faker import Faker
import random
import json

fake = Faker()


def generate_floor_data(buildingId):
   
    def generate_random_time():
        hour = random.choice(range(0, 24))
        minute = random.choice([0, 10, 20, 30, 40, 50])
        return f'{hour:02d}:{minute:02d}:00'

    
    def generate_random_cleaning_time():
        hour = random.choice(range(0, 8))
        minute = random.choice([0, 10, 20, 30, 40, 50])
        return f'{hour:02d}:{minute:02d}:00'

    
    return {
        "name": fake.company(),  
        "parFloorTypeId": random.choice([11, 12]),
        "openingTime": generate_random_time(),
        "closingTime": generate_random_time(),
        "cleaningTime": generate_random_cleaning_time(),
        "buildingId": buildingId
    }