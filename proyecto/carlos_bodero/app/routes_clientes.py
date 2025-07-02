# app/routes_clientes.py
from flask import Blueprint, render_template, request, redirect, url_for
from .models import Cliente
from . import db

clientes_bp = Blueprint('clientes', __name__, url_prefix='/clientes')

@clientes_bp.route('/')
def lista():
    clientes = Cliente.query.all()
    return render_template('clientes.html', clientes=clientes)

@clientes_bp.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        c = Cliente(nombre=request.form['nombre'], telefono=request.form['telefono'])
        db.session.add(c)
        db.session.commit()
        return redirect(url_for('clientes.lista'))
    return render_template('cliente_form.html', action="Agregar")

@clientes_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    c = Cliente.query.get_or_404(id)
    if request.method == 'POST':
        c.nombre = request.form['nombre']
        c.telefono = request.form['telefono']
        db.session.commit()
        return redirect(url_for('clientes.lista'))
    return render_template('cliente_form.html', action="Editar", cliente=c)

@clientes_bp.route('/eliminar/<int:id>')
def eliminar(id):
    c = Cliente.query.get_or_404(id)
    db.session.delete(c)
    db.session.commit()
    return redirect(url_for('clientes.lista'))