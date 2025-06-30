from flask import Blueprint, render_template, request, redirect, url_for, flash
from datetime import datetime
from app.extensions import db
from app.models.user import User

bp= Blueprint('usuarios', __name__, url_prefix='/usuarios')

@bp.route('/')
def listar():
    usuarios = User.query.all()
    return render_template('usuarios.html', usuarios=usuarios,datatime=datetime)

@bp.route('/usuarios/crear', methods=['GET', 'POST'])
def crear_usuario():
    if request.method == 'POST':
        nombre = request.form['nombre'].strip()
        correo = request.form['correo'].strip()
        telefono = request.form.get('telefono','').strip()
        fecha_nacimiento = request.form.get('fecha_nacimiento')

        try:
            fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d').date() if fecha_nacimiento else None
        except ValueError:
            flash('Formato de fecha de nacimiento inválida.', 'error')
            return redirect(url_for('usuarios.crear_usuario'))

        if not nombre or not correo:
            flash('Todos los campos son obligatorios.', 'error')
            return redirect(url_for('usuarios.crear_usuario'))
        if User.query.filter_by(correo=correo).first():
            flash('El correo ya está registrado.', 'error')
            return redirect(url_for('usuarios.crear_usuario'))
        nuevo_usuario = User(nombre=nombre, correo=correo, telefono=telefono, fecha_nacimiento=fecha_nacimiento)
        db.session.add(nuevo_usuario)
        db.session.commit()
        flash('Usuario creado exitosamente.', 'success')
        return redirect(url_for('usuarios.crear_usuario'))

    return render_template('form.html', accion='Crear', usuario=None)

@bp.route('/usuarios/editar/<int:id>', methods=['GET', 'POST'])
def editar_usuario(id):
    usuario=User.query.get_or_404(id)

    if request.method == 'POST':
        nombre = request.form['nombre'].strip()
        correo = request.form['correo'].strip()
        telefono = request.form['telefono'].strip()
        fecha_nacimiento = request.form['fecha_nacimiento'].strip()

        try:
            fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d').date() if fecha_nacimiento else None
        except ValueError:
            flash('Formato de fecha de nacimiento inválida.', 'error')
            return redirect(url_for('usuarios.editar_usuario', id=id))

        if not nombre or not correo:
            flash('Todos los campos son obligatorios.', 'error')
            return redirect(url_for('usuarios.editar_usuario', id=id))
        if correo != usuario.correo and User.query.filter_by(correo=correo).first():
            flash('El correo ya está registrado.', 'error')
            return redirect(url_for('usuarios.editar_usuario', id=id))

        usuario.nombre = nombre
        usuario.correo = correo
        usuario.telefono = telefono
        usuario.fecha_nacimiento = fecha_nacimiento

        db.session.commit()
        flash('Usuario editado exitosamente.', 'success')
        return redirect(url_for('usuarios.crear_usuario', id=id))

    return render_template('form.html', accion='Editar', usuario=usuario)

@bp.route('/usuarios/eliminar/<int:id>')
def eliminar_usuario(id):
    usuario=User.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    flash('Usuario eliminado exitosamente.', 'success')
    return redirect(url_for('usuarios.crear_usuario'))
