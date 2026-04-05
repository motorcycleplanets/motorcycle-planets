from flask import render_template, request, redirect
from app import app, db
from app.models import Cliente, Moto, Servicio

# -------------------------
# HOME
# -------------------------
@app.route('/')
def home():
    return render_template('index.html')

# -------------------------
# DASHBOARD (FIX ERROR 500)
# -------------------------
@app.route('/dashboard')
def dashboard():
    clientes = Cliente.query.all()
    motos = Moto.query.all()
    servicios = Servicio.query.all()

    return render_template(
        'dashboard.html',
        clientes=clientes,
        motos=motos,
        servicios=servicios
    )

# -------------------------
# CLIENTE
# -------------------------
@app.route('/nuevo_cliente', methods=['GET', 'POST'])
def nuevo_cliente():
    if request.method == 'POST':
        nuevo = Cliente(
            nombre=request.form['nombre'],
            telefono=request.form['telefono']
        )
        db.session.add(nuevo)
        db.session.commit()
        return redirect('/dashboard')

    return render_template('nuevo_cliente.html')

# -------------------------
# MOTO
# -------------------------
@app.route('/nueva_moto', methods=['GET', 'POST'])
def nueva_moto():
    clientes = Cliente.query.all()

    if request.method == 'POST':
        moto = Moto(
            marca=request.form['marca'],
            modelo=request.form['modelo'],
            placa=request.form['placa'],
            cliente_id=request.form['cliente_id']
        )
        db.session.add(moto)
        db.session.commit()
        return redirect('/dashboard')

    return render_template('nueva_moto.html', clientes=clientes)

# -------------------------
# SERVICIO
# -------------------------
@app.route('/nuevo_servicio', methods=['GET', 'POST'])
def nuevo_servicio():
    motos = Moto.query.all()

    if request.method == 'POST':
        servicio = Servicio(
            descripcion=request.form['descripcion'],
            precio=request.form['precio'],
            moto_id=request.form['moto_id']
        )
        db.session.add(servicio)
        db.session.commit()
        return redirect('/dashboard')

    return render_template('nuevo_servicio.html', motos=motos)

# -------------------------
# INIT DB
# -------------------------
@app.route('/init_db')
def init_db():
    with app.app_context():
        db.create_all()
    return "Base de datos creada correctamente"
