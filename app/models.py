from app import db

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)

class Moto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(100), nullable=False)
    modelo = db.Column(db.String(100), nullable=False)
    placa = db.Column(db.String(50), nullable=False)

    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)

class Servicio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(200), nullable=False)
    precio = db.Column(db.Float, nullable=False)

    moto_id = db.Column(db.Integer, db.ForeignKey('moto.id'), nullable=False)
