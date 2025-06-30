
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Base de datos en memoria
productos = []
contador_id = 1

@app.route('/productos')
def lista_productos():
    return render_template('lista_productos.html', productos=productos)
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
        return redirect(url_for('lista_productos'))
    return render_template('nuevo_producto.html')

@app.route('/productos/editar/<int:producto_id>', methods=['GET', 'POST'])
def editar_producto(producto_id):
    producto = next((p for p in productos if p['id'] == producto_id), None)
    if not producto:
        return "Producto no encontrado", 404
    
    if request.method == 'POST':
        producto['nombre'] = request.form['nombre']
        producto['precio'] = float(request.form['precio'])
        producto['cantidad'] = int(request.form['cantidad'])
        return redirect(url_for('lista_productos'))
    
    return render_template('editar_producto.html', producto=producto)

@app.route('/productos/eliminar/<int:producto_id>', methods=['GET'])
def eliminar_producto(producto_id):
    global productos
    productos = [p for p in productos if p['id'] != producto_id]
    return redirect(url_for('lista_productos'))

if __name__ == '__main__':
    app.run(debug=True)




    