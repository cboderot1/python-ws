from datetime import datetime
from app.extensions import db

class Category(db.Model):
    __tablename__ = 'categorias'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    fecha_creacion = db.Column(db.DateTime, default=datetime.now)  # Fecha de creación

    productos = db.relationship('Product', backref='categoria_obj', lazy=True)

    def __repr__(self):
        return f'<Categoria {self.nombre}>'
