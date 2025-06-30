from datetime import datetime
from app.extensions import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20))
    fecha_nacimiento = db.Column(db.Date)
    fecha_registro = db.Column(db.DateTime, default=datetime.now)
    
    def __repr__(self):
        return f'<User {self.nombre}>'