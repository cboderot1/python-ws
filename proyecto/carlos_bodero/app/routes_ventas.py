# app/routes_ventas.py
from flask import Blueprint, render_template, request, redirect, url_for
from .models import Venta, Cliente, Producto
from . import db

ventas_bp = Blueprint('ventas', __name__, url_prefix='/ventas')

@ventas_bp.route('/')
def lista():
    ventas = Venta.query.all()
    return render_template('ventas.html', ventas=ventas)

@ventas_bp.route('/agregar', methods=['GET', 'POST'])
def agregar():
    clientes = Cliente.query.all()
    productos = Producto.query.all()
    if request.method == 'POST':
        v = Venta(cliente_id=request.form['cliente_id'], producto_id=request.form['producto_id'])
        db.session.add(v)
        db.session.commit()
        return redirect(url_for('ventas.lista'))
    return render_template('venta_form.html', clientes=clientes, productos=productos)

@ventas_bp.route('/eliminar/<int:id>')
def eliminar(id):
    v = Venta.query.get_or_404(id)
    db.session.delete(v)
    db.session.commit()
    return redirect(url_for('ventas.lista'))
