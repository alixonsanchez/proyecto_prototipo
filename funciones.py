from pymongo import MongoClient

# Conectar a la base de datos con un cliente MongoDB eficiente
client = MongoClient("mongodb://localhost:27017/", maxPoolSize=50, minPoolSize=5)
db = client["Banco"]

# Funciones CRUD para Clientes
def crear_cliente(id_cliente, nombre, email):
    db.Clientes.update_one(
        {"id_cliente": id_cliente}, 
        {"$setOnInsert": {"id_cliente": id_cliente, "nombre": nombre, "email": email}}, 
        upsert=True
    )  # upsert=True asegura que si el cliente ya existe, no se crea otro
    print(f"Cliente {nombre} agregado correctamente.")

def leer_cliente(id_cliente):
    cliente = db.Clientes.find_one({"id_cliente": id_cliente})
    return cliente  # Retornamos el cliente en lugar de imprimirlo

def actualizar_cliente(id_cliente, nuevo_nombre=None, nuevo_email=None):
    update_fields = {}
    if nuevo_nombre:
        update_fields["nombre"] = nuevo_nombre
    if nuevo_email:
        update_fields["email"] = nuevo_email
    if update_fields:
        db.Clientes.update_one({"id_cliente": id_cliente}, {"$set": update_fields})
        print(f"Cliente con id {id_cliente} actualizado correctamente.")

def eliminar_cliente(id_cliente):
    db.Clientes.delete_one({"id_cliente": id_cliente})
    print(f"Cliente con id {id_cliente} eliminado correctamente.")

# Funciones CRUD para Transacciones
def crear_transaccion(id_transaccion, id_cliente, monto, fecha, tipo):
    db.Transacciones.insert_one({
        "id_transaccion": id_transaccion,
        "id_cliente": id_cliente,
        "monto": monto,
        "fecha": fecha,
        "tipo": tipo
    })
    print(f"Transacción {id_transaccion} agregada correctamente.")

def leer_transacciones_cliente(id_cliente):
    transacciones = db.Transacciones.find({"id_cliente": id_cliente}).limit(100)  # Limitamos los resultados
    transacciones_list = list(transacciones)  # Convertimos el cursor a una lista
    return transacciones_list

def actualizar_transaccion(id_transaccion, nuevo_monto=None, nuevo_tipo=None):
    update_fields = {}
    if nuevo_monto:
        update_fields["monto"] = nuevo_monto
    if nuevo_tipo:
        update_fields["tipo"] = nuevo_tipo
    if update_fields:
        db.Transacciones.update_one({"id_transaccion": id_transaccion}, {"$set": update_fields})
        print(f"Transacción {id_transaccion} actualizada correctamente.")

def eliminar_transaccion(id_transaccion):
    db.Transacciones.delete_one({"id_transaccion": id_transaccion})
    print(f"Transacción {id_transaccion} eliminada correctamente.")