from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista en memoria, cada alumno tiene un id único
productos = [
    {'id': 1, 'nombre': 'martillo', 'precio': 20, 'categoria':'herramienta'},
    {'id': 2, 'nombre': 'Pinzas', 'precio': 21, 'categoria': 'herramienta'},
    {'id': 3, 'nombre': 'Alicate', 'precio': 22, 'categoria': 'herramienta'}
]
_next_id = 4

@app.route('/')
def lista_productos():
    return render_template('productos.html', productos=productos)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar_producto():
    global _next_id
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = int(request.form['precio'])
        categoria = request.form['categoria']
        productos.append({'id': _next_id, 'nombre': nombre, 'precio': precio, 'categoria': categoria})
        _next_id += 1
        return redirect(url_for('lista_productos'))
    return render_template('agregar.html')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_producto(id):
    producto = next((a for a in productos if a['id'] == id), None)
    if not producto:
        return "Producto no encontrado", 404
    if request.method == 'POST':
        producto['nombre'] = request.form['nombre']
        producto['precio'] = int(request.form['precio'])
        producto['categoria'] = request.form['categoria']
        return redirect(url_for('lista_productos'))
    return render_template('editar.html', producto=producto)

@app.route('/eliminar/<int:id>')
def eliminar_producto(id):
    global productos
    producto = [a for a in productos if a['id'] != id]
    return redirect(url_for('lista_productos'))

if __name__ == '__main__':
    app.run(debug=True)
