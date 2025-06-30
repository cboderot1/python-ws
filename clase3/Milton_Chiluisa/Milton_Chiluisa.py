from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista que simula la base de datos
productos = []
contador_id = 1

# Ruta: Mostrar todos los productos
@app.route('/productos')
def listar_productos():
    return render_template('lista_productos.html', productos=productos)

# Ruta: Formulario para crear un nuevo producto
@app.route('/productos/nuevo', methods=['GET', 'POST'])
def nuevo_producto():
    global contador_id
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = float(request.form['precio'])
        cantidad = int(request.form['cantidad'])
        producto = {
            'id': contador_id,
            'nombre': nombre,
            'precio': precio,
            'cantidad': cantidad
        }
        productos.append(producto)
        contador_id += 1
        return redirect(url_for('listar_productos'))
    return render_template('nuevo_producto.html')

# Ruta: Editar un producto
@app.route('/productos/editar/<int:id>', methods=['GET', 'POST'])
def editar_producto(id):
    producto = next((p for p in productos if p['id'] == id), None)
    if not producto:
        return "Producto no encontrado", 404
    if request.method == 'POST':
        producto['nombre'] = request.form['nombre']
        producto['precio'] = float(request.form['precio'])
        producto['cantidad'] = int(request.form['cantidad'])
        return redirect(url_for('listar_productos'))
    return render_template('editar_producto.html', producto=producto)

# Ruta: Eliminar un producto
@app.route('/productos/eliminar/<int:id>')
def eliminar_producto(id):
    global productos
    productos = [p for p in productos if p['id'] != id]
    return redirect(url_for('listar_productos'))

if __name__ == '__main__':
    app.run(debug=True)
