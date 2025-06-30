from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.secret_key = '1000ton' # IMPORTANT: Keep this consistent and ideally more complex for production!

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///evolum_store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Product Data (Crucial: Ensure this structure is maintained precisely)
productos = {
    'ligas-ejercicio': {
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
            {'pregunta': '¿Con qué frecuencia debo usar ligas para ejercicio?', 'respuesta': 'Depende de tus objetivos, pero generalmente se recomienda 2 a 4 veces por semana, con tiempo de recuperación.'}
        ]
    },
    'combo-perfumes': {
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
            {'pregunta': '¿Son los perfumes aptos para uso diario?', 'respuesta': 'Sí, son perfectos para usar a diario, ideales para ocasiones especiales o para el día a día.'}
        ]
    }
}


@app.route('/')
def home():
    # Adding debug print statements here to confirm the 'productos' type
    print("--- DEBUG START: Verifying 'productos' structure ---")
    print(f"Type of 'productos' dictionary: {type(productos)}")
    for product_id, product_info in productos.items():
        print(f"  Product ID: '{product_id}', Type of product_info: {type(product_info)}")
        if not isinstance(product_info, dict):
            print(f"  !!!!! ALERT: product_info for '{product_id}' is NOT a dictionary. Its value is: {product_info}")
        elif 'imagen' not in product_info:
            print(f"  !!!!! ALERT: 'imagen' key missing for product '{product_id}'. Product info: {product_info}")
        elif 'nombre' not in product_info:
            print(f"  !!!!! ALERT: 'nombre' key missing for product '{product_id}'. Product info: {product_info}")
    print("--- DEBUG END: 'productos' structure verification ---")

    return render_template('index.html', productos=productos)

@app.route('/producto/<product_id>')
def product_page(product_id):
    producto = productos.get(product_id)
    if producto:
        return render_template('product.html', producto=producto)
    return "Producto no encontrado", 404

@app.route('/add_to_cart/<product_id>', methods=['POST'])
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = {}

    product_info = productos.get(product_id)

    if product_info:
        if product_id in session['cart']:
            session['cart'][product_id]['quantity'] += 1
        else:
            session['cart'][product_id] = {
                'id': product_info['id'],
                'nombre': product_info['nombre'],
                'precio_actual': product_info['precio_actual'],
                'imagen': product_info['imagen'],
                'quantity': 1
            }
        flash(f'"{product_info["nombre"]}" ha sido añadido al carrito.', 'success')
    else:
        flash('Error: El producto no existe.', 'error')

    session.modified = True
    return redirect(url_for('cart'))

@app.route('/cart')
def cart():
    carrito = session.get('cart', {})
    total_carrito = 0
    for item_id, item_info in carrito.items():
        total_carrito += item_info['precio_actual'] * item_info['quantity']

    return render_template('cart.html', carrito=carrito, total_carrito=total_carrito)

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

if __name__ == '__main__':
    # If you are using Flask-Migrate, keep this line commented out.
    # db.create_all()
    app.run(debug=True, port=5002)