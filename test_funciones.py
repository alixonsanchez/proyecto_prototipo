from funciones import crear_cliente, crear_transaccion, leer_cliente, leer_transacciones_cliente
# Ejecución de pruebas

crear_cliente(1005839274, "Alixon Sánchez", "alixonsanchez14@gmail.com")
crear_transaccion(1001, 1005839274, 10000, "2024-11-12", "depósito")
leer_cliente(1005839274)
leer_transacciones_cliente(1005839274)
