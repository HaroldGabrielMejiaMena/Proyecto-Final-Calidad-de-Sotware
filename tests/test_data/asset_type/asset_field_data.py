import random

# Generar datos aleatorios para AssetField (sin assetTypeId, ya que lo obtenemos del setup)
def generate_asset_field_data():
    return {
        "isRequired": random.choice([True, False]),
        "parAssetFieldId": random.choice([8, 9, 10])  # Estos valores son fijos como mencionaste
    }