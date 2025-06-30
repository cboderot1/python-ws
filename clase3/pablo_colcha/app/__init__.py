
from flask import Flask, render_template
from .extensions import db, migrate
from config import Config

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    
    from app.models.user import User
    from app.models.product import Product
    from app.models.category import Category
    
    from app.routes.users import bp as usuarios_bp
    from app.routes.products import bp as products_bp
    from app.routes.categorys import bp as categorys_bp

    app.register_blueprint(categorys_bp)

    app.register_blueprint(usuarios_bp)
    app.register_blueprint(products_bp)

    @app.route('/')
    def home():
        return render_template('home.html')

    
    return app
