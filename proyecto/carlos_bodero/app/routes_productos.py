from flask import Blueprint, render_template, request, redirect, url_for
from .models import Producto
from . import db

productos_bp = Blueprint('productos', __name__, url_prefix='/productos')

@productos_bp.route('/')
def lista():
    productos = Producto.query.all()
    return render_template('productos.html', productos=productos)

@productos_bp.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        p = Producto(nombre=request.form['nombre'], precio=request.form['precio'], cantidad=request.form['cantidad'])
        db.session.add(p)
        db.session.commit()
        return redirect(url_for('productos.lista'))
    return render_template('producto_form.html', action="Agregar")

@productos_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    p = Producto.query.get_or_404(id)
    if request.method == 'POST':
        p.nombre = request.form['nombre']
        p.precio = request.form['precio']
        p.cantidad = request.form['cantidad']
        db.session.commit()
        return redirect(url_for('productos.lista'))
    return render_template('producto_form.html', action="Editar", producto=p)

@productos_bp.route('/eliminar/<int:id>')
def eliminar(id):
    p = Producto.query.get_or_404(id)
    db.session.delete(p)
    db.session.commit()
    return redirect(url_for('productos.lista'))