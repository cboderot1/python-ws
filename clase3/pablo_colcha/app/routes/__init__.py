def init_routes(app):
    from .index import bp as index_bp
    from .users import bp as users_bp
    from .products import bp as products_bp
    from .categorys import bp as categorys_bp
    
    
    app.register_blueprint(index_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(categorys_bp)
    
    from app.routes.users import bp as users_bp
    app.register_blueprint(users_bp)