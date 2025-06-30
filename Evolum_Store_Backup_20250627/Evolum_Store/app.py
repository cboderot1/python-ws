from flask import Flask, render_template, url_for, abort, session, redirect, flash, request

app = Flask(__name__)
# ¡IMPORTANTE! Esta clave secreta es VITAL para que las sesiones funcionen correctamente.
# Debe ser una cadena Larga, Aleatoria y, sobre todo, PERMANENTE (no cambiar cada vez).
# CAMBIA 'tu_clave_secreta_super_segura_y_unica_aqui_para_evolum_store_2025_ABCD' por una TUYA propia.
app.config['SECRET_KEY'] = '1000ton'

# --- Datos de los Productos ---
productos = [
    {
        'id': 'ligas-ejercicio', 
        'nombre': 'Set de Ligas para Ejercicio',
        'precio_actual': 27.00,
        'precio_anterior': 60.00,
        'imagen': 'producto_ligas.png',
        'descripcion_corta': 'Entrena con estilo, Kit de Bandas de resistencias variadas para entrenar, ejercita brazos, piernas, glúteos, abdomen, entre otros, con estas bandas para ejercicios logra ejercitar esa parte de tu cuerpo que mas necesites.',
        'descripcion_larga': [
            'Estas ligas son muy eficaces ya que puedes usar el peso óptimo para el entrenamiento, puedes usarlas juntas o por separado dependiendo de la intensidad de fuerza que quieras aplicar en el entrenamiento.',
            'Perfecto para utilizar en casa o en el gimnasio.',
            'Niveles de resistencia: Amarillo (Extra ligero), Verde (Ligero), Rojo (Medio), Azul (Fuerte), Negro (Extra Fuerte).',
            'Combinación de Resistencia hasta de 100 Libras (colocando todas las manijas juntas).',
            'Incluye: Mosquetón Metálico, Tubo de látex 100%, Correas de tobillo, Anclaje para puerta, 5 elásticos tubulares con manillas de alta calidad, Ebook Guía de Ejercicios.',
            'Fácil de transportar y usar para ejercicios variados.',
            'Medidas (Aprox.): Negro: 5x11x1200mm, Verde: 4x8x1200mm, Azul: 5x10x1200mm, Rojo: 5x9x1200mm, Amarillo: 5x8x1200mm.'
        ],
        'preguntas_frecuentes': [
            {'pregunta': '¿Qué son las ligas para ejercicio?', 'respuesta': 'También conocidas como bandas de resistencia, son herramientas de entrenamiento hechas de látex o goma para ejercicios de resistencia.'},
            {'pregunta': '¿Cuáles son los beneficios de usar ligas para ejercicio?', 'respuesta': 'Versatilidad, portabilidad, ajuste de intensidad, y menor riesgo de lesiones en comparación con pesas tradicionales.'},
            {'pregunta': '¿Cómo elegir la liga adecuada para mí?', 'respuesta': 'Considera tu nivel de resistencia (principiante, ligero) y el tipo de ejercicio. Las ligas más largas son ideales para cuerpo completo.'},
            {'pregunta': '¿Puedo usar ligas para ejercicio en lugar de pesas?', 'respuesta': 'Sí, son una excelente alternativa, especialmente para principiantes o para un entrenamiento más suave en las articulaciones.'},
            {'pregunta': '¿Cómo debo cuidar mis ligas para ejercicio?', 'respuesta': 'Guárdalas en un lugar fresco y seco, límpialas con un paño húmedo y revisa regularmente el desgaste.'},
            {'pregunta': '¿Con qué frecuencia debo usar ligas para ejercicio?', 'respuesta': 'Depende de tus objetivos, pero generalmente se recomienda 2 a 4 veces por semana, con tiempo de recuperación.'},
        ]
    },
    {
        'id': 'combo-perfumes', 
        'nombre': 'Combo 3 Perfumes de Inspiración',
        'precio_actual': 59.00,
        'precio_anterior': 200.00,
        'imagen': 'producto_perfumes.png',
        'descripcion_corta': 'Huele rico, fragancias perfectas para la conquista.',
        'descripcion_larga': [
            'Nunca fue más fácil oler rico, recibe 3 Perfumes de Inspiración perfectos para la conquista.',
            'Fragancias disponibles: One Million, Sauvage, Invictus.',
            'Fragancias Importadas desde Francia, asegurando alta calidad y autenticidad en las fragancias.',
            'La fragancia es idéntica a las versiones originales, por lo que tendrás la misma experiencia sensorial que los perfumes de marca.'
        ],
        'preguntas_frecuentes': [
            {'pregunta': '¿Vienen los perfumes con frasco original?', 'respuesta': 'No, vienen con frascos genéricos, pero la fragancia es idéntica a la versión original.'},
            {'pregunta': '¿De dónde provienen los perfumes?', 'respuesta': 'Los perfumes son importados desde Francia, asegurando alta calidad y autenticidad en las fragancias.'},
            {'pregunta': '¿Cuáles son las fragancias disponibles?', 'respuesta': 'Las fragancias disponibles son One Million, Sauvage e Invictus.'},
            {'pregunta': '¿La fragancia es igual a la original?', 'respuesta': 'Sí, la fragancia es idéntica a las versiones originales.'},
            {'pregunta': '¿En qué presentaciones están disponibles los perfumes?', 'respuesta': 'Están disponibles en presentaciones con frascos genéricos, cuyo tamaño varía según la disponibilidad.'},
            {'pregunta': '¿Son los perfumes aptos para uso diario?', 'respuesta': 'Sí, son perfectos para usar a diario, ideales para ocasiones especiales o para el día a día.'},
        ]
    }
]

# --- Definición de Rutas ---

# RUTA PARA LAS PÁGINAS DE PRODUCTO INDIVIDUALES
@app.route('/producto/<string:product_id>')
def product_page(product_id):
    # DEBUG: Para verificar qué ID de producto se está buscando
    print(f"DEBUG (product_page): Intentando cargar producto con ID: '{product_id}'")
    
    producto = next((p for p in productos if p['id'] == product_id), None)
    
    # DEBUG: Para ver si se encontró el producto o es None
    print(f"DEBUG (product_page): Objeto producto encontrado: {producto}")
    
    if producto is None:
        print(f"DEBUG (product_page): Producto con ID '{product_id}' NO ENCONTRADO. Abortando 404.")
        abort(404) # Muestra una página 404 si el producto no existe
    return render_template('product.html', producto=producto)

# RUTA PARA AÑADIR PRODUCTOS AL CARRITO
@app.route('/add_to_cart/<string:product_id>')
def add_to_cart(product_id):
    producto = next((p for p in productos if p['id'] == product_id), None)
    if producto is None:
        flash('El producto no existe.', 'error')
        return redirect(url_for('home'))

    # DEBUG: Mostrar contenido de la sesión ANTES de añadir
    print(f"DEBUG (add_to_cart): Sesión de carrito ANTES de añadir: {session.get('cart', {})}")

    if 'cart' not in session:
        session['cart'] = {}

    if product_id in session['cart']:
        session['cart'][product_id]['cantidad'] += 1
    else:
        # Copiamos solo la información relevante del producto para no guardar todo el objeto
        # (descripcion_larga y preguntas_frecuentes no son necesarias en el carrito)
        product_info_copy = {k: v for k, v in producto.items() if k not in ['descripcion_larga', 'preguntas_frecuentes']}
        session['cart'][product_id] = {'cantidad': 1, 'producto_info': product_info_copy}
    
    # DEBUG: Mostrar contenido de la sesión DESPUÉS de añadir
    print(f"DEBUG (add_to_cart): Sesión de carrito DESPUÉS de añadir: {session['cart']}")
    
    session.modified = True # ¡Indica a Flask que la sesión ha sido modificada para que la guarde!
    
    flash(f'{producto["nombre"]} añadido al carrito!', 'success')
    return redirect(url_for('cart')) # Redirigir al carrito después de añadir

# RUTA: ACTUALIZAR CANTIDAD DE UN PRODUCTO EN EL CARRITO
@app.route('/update_cart_item/<string:product_id>', methods=['POST'])
def update_cart_item(product_id):
    if 'cart' not in session or product_id not in session['cart']:
        flash('Producto no encontrado en el carrito.', 'error')
        return redirect(url_for('cart'))

    try:
        new_quantity = int(request.form.get('quantity'))
        
        # DEBUG: Mostrar cantidad ANTES de actualizar
        print(f"DEBUG (update_cart_item): Cantidad anterior de '{product_id}': {session['cart'][product_id]['cantidad']}")

        if new_quantity <= 0:
            del session['cart'][product_id]
            flash('Producto eliminado del carrito.', 'success')
            print(f"DEBUG (update_cart_item): Producto '{product_id}' eliminado.")
        else:
            session['cart'][product_id]['cantidad'] = new_quantity
            flash('Cantidad actualizada.', 'success')
            print(f"DEBUG (update_cart_item): Cantidad de '{product_id}' actualizada a {new_quantity}.")
        
        session.modified = True # ¡Indica a Flask que la sesión ha sido modificada!
        # DEBUG: Mostrar contenido de la sesión DESPUÉS de actualizar
        print(f"DEBUG (update_cart_item): Sesión de carrito DESPUÉS de actualizar: {session['cart']}")

    except ValueError:
        flash('Cantidad inválida.', 'error')
        print(f"DEBUG (update_cart_item): Error: Cantidad inválida para '{product_id}'.")
    
    return redirect(url_for('cart'))

# RUTA: ELIMINAR UN PRODUCTO DEL CARRITO
@app.route('/remove_from_cart/<string:product_id>')
def remove_from_cart(product_id):
    # DEBUG: Mostrar contenido de la sesión ANTES de eliminar
    print(f"DEBUG (remove_from_cart): Sesión de carrito ANTES de eliminar: {session.get('cart', {})}")

    if 'cart' in session and product_id in session['cart']:
        del session['cart'][product_id]
        session.modified = True # ¡Indica a Flask que la sesión ha sido modificada!
        flash('Producto eliminado del carrito.', 'success')
        print(f"DEBUG (remove_from_cart): Producto '{product_id}' eliminado.")
    else:
        flash('El producto no se pudo eliminar del carrito.', 'error')
        print(f"DEBUG (remove_from_cart): No se pudo eliminar el producto '{product_id}'. No encontrado en el carrito.")
    
    # DEBUG: Mostrar contenido de la sesión DESPUÉS de eliminar
    print(f"DEBUG (remove_from_cart): Sesión de carrito DESPUÉS de eliminar: {session.get('cart', {})}")
    return redirect(url_for('cart'))

# RUTA PARA MOSTRAR EL CONTENIDO DEL CARRITO
@app.route('/cart')
def cart():
    cart_items = session.get('cart', {})
    # DEBUG: Mostrar contenido de la sesión al cargar la página del carrito
    print(f"DEBUG (cart): Contenido del carrito al cargar la página: {cart_items}")
    
    total = sum(item['cantidad'] * item['producto_info']['precio_actual'] for item in cart_items.values())
    return render_template('cart.html', cart_items=cart_items, total=total)

# RUTA PARA LA PÁGINA DE INICIO
@app.route('/')
def home():
    return render_template('index.html', productos=productos)


# --- Inicio de la Aplicación ---
if __name__ == '__main__':
    app.run(debug=True, port=5002)