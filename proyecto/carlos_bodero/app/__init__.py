from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    templates_dir = os.path.join(os.path.dirname(__file__), '..', 'templates')
    app = Flask(__name__, template_folder=templates_dir)

    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, '..', 'app.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes_productos import productos_bp
    from .routes_clientes import clientes_bp
    from .routes_ventas import ventas_bp

    app.register_blueprint(productos_bp)
    app.register_blueprint(clientes_bp)
    app.register_blueprint(ventas_bp)

    @app.route("/")
    def index():
        from .models import Producto
        productos = Producto.query.all()
        return render_template('index.html', productos=productos)

    from flask import render_template  # <- necesario para index

    return app
