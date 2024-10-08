# Ejecutar el comando para instalar lo necesario para ejecutar el proyecto
pip install -r requirements.txt

# Ejecutar las pruebas en paralelo
pytest -s -m ui_automation -n 4

# Ejecutar las pruebas en un solo Navegador
pytest -s -m ui_automation 

# Ejecutar el reporte de allure
allure serve reports
