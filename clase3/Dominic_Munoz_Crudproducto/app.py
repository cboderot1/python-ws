from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'clave_secreta_segura_123'  # Cambia esta clave por una secreta

productos = []
contador_id = 1


@app.route('/')
def home():
    return redirect(url_for('listar_productos'))


@app.route('/productos')
def listar_productos():
    return render_template('listar_productos.html', productos=productos)


@app.route('/productos/nuevo', methods=['GET', 'POST'])
def nuevo_producto():
    global contador_id
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        cantidad = request.form['cantidad']

        try:
            precio = float(precio)
            cantidad = int(cantidad)
        except ValueError:
            flash('Precio o cantidad inválidos.')
            return redirect(url_for('nuevo_producto'))

        productos.append({
            'id': contador_id,
            'nombre': nombre,
            'precio': precio,
            'cantidad': cantidad
        })
        contador_id += 1
        flash(f'Producto "{nombre}" creado correctamente.')
        return redirect(url_for('listar_productos'))

    return render_template('nuevo_producto.html')


@app.route('/productos/editar/<int:id>', methods=['GET', 'POST'])
def editar_producto(id):
    producto = next((p for p in productos if p['id'] == id), None)
    if not producto:
        flash('Producto no encontrado.')
        return redirect(url_for('listar_productos'))

    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        cantidad = request.form['cantidad']

        try:
            precio = float(precio)
            cantidad = int(cantidad)
        except ValueError:
            flash('Precio o cantidad inválidos.')
            return redirect(url_for('editar_producto', id=id))

        producto['nombre'] = nombre
        producto['precio'] = precio
        producto['cantidad'] = cantidad

        flash(f'Producto "{nombre}" actualizado correctamente.')
        return redirect(url_for('listar_productos'))

    return render_template('editar_producto.html', producto=producto)


@app.route('/productos/eliminar/<int:id>', methods=['POST'])
def eliminar_producto(id):
    global productos
    producto = next((p for p in productos if p['id'] == id), None)
    if producto:
        productos = [p for p in productos if p['id'] != id]
        flash(f'Producto "{producto["nombre"]}" eliminado correctamente.')
    else:
        flash('Producto no encontrado.')
    return redirect(url_for('listar_productos'))


if __name__ == '__main__':
    app.run(debug=True)
