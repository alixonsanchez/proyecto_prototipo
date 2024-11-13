from flask import Flask, render_template, request, redirect, url_for
from funciones import (
    crear_cliente, leer_cliente, actualizar_cliente, eliminar_cliente,
    crear_transaccion, leer_transacciones_cliente, actualizar_transaccion, eliminar_transaccion
)

app = Flask(__name__)

@app.route('/')
def index():
    # Página de inicio
    return render_template('index.html')

# Rutas para la gestión de clientes
@app.route('/cliente/nuevo', methods=['GET', 'POST'])
def nuevo_cliente():
    if request.method == 'POST':
        # Obtiene datos del formulario para crear un nuevo cliente
        id_cliente = int(request.form['id_cliente'])
        nombre = request.form['nombre']
        email = request.form['email']
        crear_cliente(id_cliente, nombre, email)
        return redirect(url_for('index'))
    return render_template('cliente.html', action="Crear")

@app.route('/cliente/<int:id_cliente>')
def ver_cliente(id_cliente):
    # Muestra la información de un cliente específico
    cliente = leer_cliente(id_cliente)
    if not cliente:
        return "Cliente no encontrado", 404
    return render_template('cliente.html', cliente=cliente, action="Ver")

@app.route('/cliente/actualizar/<int:id_cliente>', methods=['GET', 'POST'])
def actualizar_cliente_view(id_cliente):
    if request.method == 'POST':
        # Obtiene datos del formulario para actualizar el cliente
        nuevo_nombre = request.form.get('nombre')
        nuevo_email = request.form.get('email')
        actualizar_cliente(id_cliente, nuevo_nombre, nuevo_email)
        return redirect(url_for('index'))
    cliente = leer_cliente(id_cliente)
    if not cliente:
        return "Cliente no encontrado", 404
    return render_template('cliente.html', cliente=cliente, action="Actualizar")

@app.route('/cliente/eliminar/<int:id_cliente>', methods=['POST'])
def eliminar_cliente_view(id_cliente):
    # Elimina un cliente
    eliminar_cliente(id_cliente)
    return redirect(url_for('index'))

# Rutas para la gestión de transacciones
@app.route('/transaccion/nueva', methods=['GET', 'POST'])
def nueva_transaccion():
    if request.method == 'POST':
        # Obtiene datos del formulario para crear una nueva transacción
        id_transaccion = int(request.form['id_transaccion'])
        id_cliente = int(request.form['id_cliente'])
        monto = float(request.form['monto'])
        fecha = request.form['fecha']
        tipo = request.form['tipo']
        crear_transaccion(id_transaccion, id_cliente, monto, fecha, tipo)
        return redirect(url_for('index'))
    return render_template('transaccion.html', action="Crear")

@app.route('/transacciones/<int:id_cliente>')
def ver_transacciones(id_cliente):
    # Muestra las transacciones de un cliente específico con paginación
    transacciones = leer_transacciones_cliente(id_cliente)
    return render_template('transaccion.html', transacciones=transacciones, action="Ver")

@app.route('/transaccion/actualizar/<int:id_transaccion>', methods=['GET', 'POST'])
def actualizar_transaccion_view(id_transaccion):
    if request.method == 'POST':
        # Obtiene datos del formulario para actualizar la transacción
        nuevo_monto = request.form.get('monto', type=float)
        nuevo_tipo = request.form.get('tipo')
        actualizar_transaccion(id_transaccion, nuevo_monto, nuevo_tipo)
        return redirect(url_for('index'))
    return render_template('transaccion.html', action="Actualizar")

@app.route('/transaccion/eliminar/<int:id_transaccion>', methods=['POST'])
def eliminar_transaccion_view(id_transaccion):
    # Elimina una transacción específica
    eliminar_transaccion(id_transaccion)
    return redirect(url_for('index'))

# Inicia la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True, threaded=True)  # threaded=True para manejar múltiples solicitudes concurrentemente