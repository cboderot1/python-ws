from datetime import datetime
from app.extensions import db

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    precio = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False) 
    fecha_creacion = db.Column(db.DateTime, default=datetime.now)
    imagen = db.Column(db.String(255))
   
    def __repr__(self):
        return f'<Product {self.nombre}>'