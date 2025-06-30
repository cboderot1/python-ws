from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'un_api_key'

base_de_datos_usuarios = []

def imprimir_usuarios():
    print("\n--- LISTA ACTUAL DE USUARIOS ---")
    print("-------------------------------\n")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/productos')
def productos():
    return render_template('productos.html')

@app.route('/usuarios')
def usuarios():
    imprimir_usuarios()
    return render_template('usuarios.html', usuarios=base_de_datos_usuarios)

@app.route('/usuarios/crear', methods=['GET', 'POST'])
def crear_usuario():
    if request.method == 'POST':
        nombre = request.form['nombre'].strip()
        correo = request.form['correo'].strip()

        if nombre and correo:
            base_de_datos_usuarios.append({'nombre': nombre, 'correo': correo})
            flash('Usuario creado con éxito.', 'success')
            imprimir_usuarios()
            return redirect(url_for('usuarios'))
        else:
            flash('Todos los campos son obligatorios.', 'error')
            return redirect(url_for('crear_usuario'))

    return render_template('form.html', accion='Crear', usuario={})

@app.route('/usuarios/editar/<int:indice>', methods=['GET', 'POST'])
def editar_usuario(indice):
    if indice >= len(base_de_datos_usuarios):
        flash('Índice de usuario inválido.', 'error')
        return redirect(url_for('usuarios'))

    usuario = base_de_datos_usuarios[indice]

    if request.method == 'POST':
        nombre = request.form['nombre'].strip()
        correo = request.form['correo'].strip()

        if nombre and correo:
            print(f"\nEditando usuario #{indice + 1}:")
            print(f"Antes: Nombre: {usuario['nombre']}, Correo: {usuario['correo']}")
            usuario['nombre'] = nombre
            usuario['correo'] = correo
            print(f"Después: Nombre: {nombre}, Correo: {correo}")
            imprimir_usuarios()
            flash('Usuario editado con éxito.', 'success')
            return redirect(url_for('usuarios'))
        else:
            flash('Todos los campos son obligatorios.', 'error')
            return redirect(url_for('editar_usuario', indice=indice))

    return render_template('form.html', accion='Editar', usuario=usuario, indice=indice)

@app.route('/usuarios/eliminar/<int:indice>')
def eliminar_usuario(indice):
    if 0 <= indice < len(base_de_datos_usuarios):
        usuario_eliminado = base_de_datos_usuarios[indice]
        print(f"\nEliminando usuario #{indice + 1}:")
        print(f"Usuario eliminado: Nombre: {usuario_eliminado['nombre']}, Correo: {usuario_eliminado['correo']}")
        base_de_datos_usuarios.pop(indice)
        imprimir_usuarios()
        flash('Usuario eliminado con éxito.', 'success')
    else:
        flash('Índice inválido.', 'error')
    return redirect(url_for('usuarios'))

if __name__ == '__main__':
    import warnings
    warnings.filterwarnings("ignore", message="This is a development server.")
    app.run(debug=True)