from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.product import Product
from app.models.category import Category
from app.extensions import db
from datetime import datetime

bp = Blueprint('products', __name__, url_prefix='/productos')

@bp.route('/')
def listar():
    productos = Product.query.order_by(Product.fecha_creacion.desc()).all()
    return render_template('productos.html', productos=productos)

@bp.route('/crear', methods=['GET', 'POST'])
def crear():
    categorias = Category.query.order_by(Category.nombre).all()
    if request.method == 'POST':
        try:
            categoria_id = request.form.get('categoria_id')
            producto=Product(
                nombre=request.form['nombre'],
                descripcion=request.form['descripcion'],
                precio=float(request.form['precio']),
                stock=int(request.form['stock']),
                categoria_id=int(categoria_id) if categoria_id else None
            )
            db.session.add(producto)
            db.session.commit()
            flash('Producto creado exitosamente.', 'success')
            return redirect(url_for('products.listar'))
        except ValueError:
            db.session.rollback()
            flash(f'error al crear el producto: {str(e)}', 'danger')
    return render_template('form_p.html', accion='Crear', producto=None, categorias=categorias)


@bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    producto = Product.query.get_or_404(id)
    categorias = Category.query.order_by(Category.nombre).all()
    if request.method == 'POST':
        categoria_id = request.form.get('categoria_id')
        
        nombre = request.form['nombre'].strip()
        descripcion = request.form['descripcion'].strip()
        precio = request.form['precio'].strip()
        stock = request.form['stock'].strip()
        

        if not nombre or not precio or not stock:
            flash('Nombre, precio y stock son obligatorios.', 'error')
            return redirect(url_for('products.editar', id=id))

        try:
            producto.precio = float(precio)
            producto.stock = int(stock)
        except ValueError:
            flash('Precio debe ser numérico y stock debe ser un número entero.', 'error')
            return redirect(url_for('products.editar', id=id))

        producto.nombre = nombre
        producto.descripcion = descripcion
        producto.categoria_id = int(categoria_id) if categoria_id else None

        db.session.commit()
        flash('Producto actualizado exitosamente.', 'success')
        return redirect(url_for('products.listar'))

    return render_template('form_p.html', accion='Editar', producto=producto)

@bp.route('/eliminar/<int:id>')
def eliminar_producto(id):
    producto = Product.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    flash('Producto eliminado exitosamente.', 'success')
    return redirect(url_for('products.listar'))
