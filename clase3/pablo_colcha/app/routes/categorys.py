from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.category import Category
from app.extensions import db
from datetime import datetime

bp = Blueprint('categorys', __name__, url_prefix='/categorias')

@bp.route('/')
def listar():
    categorias = Category.query.order_by(Category.fecha_creacion.desc()).all()
    return render_template('categorias.html', categorias=categorias)

@bp.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        try:
            categoria = Category(
                nombre=request.form['nombre']
            )
            db.session.add(categoria)
            db.session.commit()
            flash('Categoria creada exitosamente.', 'success')
            return redirect(url_for('categorys.listar'))
        except ValueError:
            db.session.rollback()
            flash(f'error al crear la categoria: {str(e)}', 'danger')
    return render_template('form_c.html', accion='Crear', categoria=None)

@bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    categoria = Category.query.get_or_404(id)

    if request.method == 'POST':
        nombre = request.form['nombre'].strip()

        if not nombre:
            flash('Nombre es obligatorio.', 'error')
            return redirect(url_for('categorys.editar', id=id))

        categoria.nombre = nombre

        db.session.commit()
        flash('Categoria actualizada exitosamente.', 'success')
        return redirect(url_for('categorys.listar'))

    return render_template('form_c.html', accion='Editar', categoria=categoria)

@bp.route('/eliminar/<int:id>')
def eliminar(id):
    categoria = Category.query.get_or_404(id)
    db.session.delete(categoria)
    db.session.commit()
    flash('Categoria eliminada exitosamente.', 'success')
    return redirect(url_for('categorys.listar'))