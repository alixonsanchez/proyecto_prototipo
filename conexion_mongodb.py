from pymongo import MongoClient
from faker import Faker
import datetime

# Crear una conexión compartida y eficiente a MongoDB utilizando el pool de conexiones
client = MongoClient("mongodb://localhost:27017/", maxPoolSize=50, minPoolSize=5)
db = client["Banco"]

# Generar datos falsos con Faker
fake = Faker()

# Crear y insertar 1000 clientes si no existen
clientes = []
for _ in range(1000):
    cliente = {
        "id_cliente": fake.unique.random_number(digits=10),
        "nombre": fake.name(),
        "email": fake.email(),
    }
    clientes.append(cliente)

# Insertar clientes en la colección 'Clientes' de forma eficiente
db.Clientes.insert_many(clientes, ordered=False)  # ordered=False para evitar bloqueos si hay errores
print("1000 clientes insertados correctamente.")

# Crear transacciones
transacciones = []
for cliente in clientes:
    for _ in range(5):  # Cada cliente tendrá 5 transacciones
        fecha = fake.date_this_century()  # Generar una fecha aleatoria dentro de este siglo
        
        # Convertir la fecha a un objeto datetime
        fecha_datetime = datetime.datetime.combine(fecha, datetime.datetime.min.time())
        
        transaccion = {
            "id_transaccion": fake.unique.random_number(digits=6),
            "id_cliente": cliente["id_cliente"],
            "monto": fake.random_int(min=10, max=5000),
            "fecha": fecha_datetime,  # Usar la fecha convertida a datetime
            "tipo": fake.random_element(elements=("depósito", "retiro")),
        }
        transacciones.append(transaccion)

# Insertar transacciones en la colección 'Transacciones' de forma eficiente
db.Transacciones.insert_many(transacciones, ordered=False)  # ordered=False para optimización
print("Transacciones insertadas correctamente.")