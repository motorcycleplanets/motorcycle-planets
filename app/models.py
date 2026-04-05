from app import db

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    telefono = db.Column(db.String(20))

    motos = db.relationship('Moto', backref='cliente', lazy=True)


class Moto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(50))
    modelo = db.Column(db.String(50))
    placa = db.Column(db.String(20))

    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)

    servicios = db.relationship('Servicio', backref='moto', lazy=True)


class Servicio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(100))
    descripcion = db.Column(db.String(200))
    precio = db.Column(db.Float)

    moto_id = db.Column(db.Integer, db.ForeignKey('moto.id'), nullable=False)
