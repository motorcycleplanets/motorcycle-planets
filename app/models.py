from app import db

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    telefono = db.Column(db.String(20))

class Moto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(100))
    modelo = db.Column(db.String(100))
    placa = db.Column(db.String(50))

    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))

class Servicio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(200))
    precio = db.Column(db.Float)

    moto_id = db.Column(db.Integer, db.ForeignKey('moto.id'))
