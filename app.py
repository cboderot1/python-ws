from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'mi_clave_secreta'  # necesario para flash

# Simulación de base de datos en memoria
productos = []
contador_id = 1

@app.route('/')
def index():
    return redirect(url_for('listar_productos'))

@app.route('/productos')
def listar_productos():
    return render_template('lista_productos.html', productos=productos)

@app.route('/productos/nuevo', methods=['GET', 'POST'])
def nuevo_producto():
    global contador_id
    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        precio = request.form.get('precio', '').strip()
        cantidad = request.form.get('cantidad', '').strip()

        # Validaciones
        if not nombre:
            flash('El nombre es obligatorio.', 'danger')
            return render_template('nuevo_producto.html', nombre=nombre, precio=precio, cantidad=cantidad)
        try:
            precio = float(precio)
            if precio <= 0:
                flash('El precio debe ser un número positivo mayor a cero.', 'danger')
                return render_template('nuevo_producto.html', nombre=nombre, precio=precio, cantidad=cantidad)
        except:
            flash('El precio debe ser un número válido.', 'danger')
            return render_template('nuevo_producto.html', nombre=nombre, precio=precio, cantidad=cantidad)

        try:
            cantidad = int(cantidad)
            if cantidad <= 0:
                flash('La cantidad debe ser un número entero positivo mayor a cero.', 'danger')
                return render_template('nuevo_producto.html', nombre=nombre, precio=precio, cantidad=cantidad)
        except:
            flash('La cantidad debe ser un número entero válido.', 'danger')
            return render_template('nuevo_producto.html', nombre=nombre, precio=precio, cantidad=cantidad)

        # Guardar producto
        nuevo = {
            'id': contador_id,
            'nombre': nombre,
            'precio': precio,
            'cantidad': cantidad
            # 'imagen': 'ruta/a/imagen.jpg'  # Aquí podrías agregar imagen más adelante
        }
        productos.append(nuevo)
        contador_id += 1

        flash('Producto creado con éxito.', 'success')
        return redirect(url_for('listar_productos'))

    return render_template('nuevo_producto.html')

@app.route('/productos/editar/<int:id>', methods=['GET', 'POST'])
def editar_producto(id):
    producto = next((p for p in productos if p['id'] == id), None)
    if not producto:
        flash('Producto no encontrado.', 'danger')
        return redirect(url_for('listar_productos'))

    if request.method == 'POST':
        nombre = request.form.get('nombre', '').strip()
        precio = request.form.get('precio', '').strip()
        cantidad = request.form.get('cantidad', '').strip()

        # Validaciones
        if not nombre:
            flash('El nombre es obligatorio.', 'danger')
            return render_template('editar_producto.html', producto=producto)
        try:
            precio = float(precio)
            if precio <= 0:
                flash('El precio debe ser un número positivo mayor a cero.', 'danger')
                return render_template('editar_producto.html', producto=producto)
        except:
            flash('El precio debe ser un número válido.', 'danger')
            return render_template('editar_producto.html', producto=producto)

        try:
            cantidad = int(cantidad)
            if cantidad <= 0:
                flash('La cantidad debe ser un número entero positivo mayor a cero.', 'danger')
                return render_template('editar_producto.html', producto=producto)
        except:
            flash('La cantidad debe ser un número entero válido.', 'danger')
            return render_template('editar_producto.html', producto=producto)

        # Actualizar producto
        producto['nombre'] = nombre
        producto['precio'] = precio
        producto['cantidad'] = cantidad

        flash('Producto actualizado con éxito.', 'success')
        return redirect(url_for('listar_productos'))

    return render_template('editar_producto.html', producto=producto)

@app.route('/productos/eliminar/<int:id>')
def eliminar_producto(id):
    global productos
    productos = [p for p in productos if p['id'] != id]
    flash('Producto eliminado correctamente.', 'success')
    return redirect(url_for('listar_productos'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)

