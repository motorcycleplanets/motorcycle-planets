from app import app, db
from app.models import Cliente, Moto, Servicio
from flask import render_template, request, redirect

@app.route('/')
def home():
    return redirect('/dashboard')

# -------------------------
# INIT DB (RESET TOTAL)
# -------------------------
@app.route('/init_db')
def init_db():
    db.drop_all()
    db.create_all()
    return "DB lista"

# -------------------------
# DASHBOARD (SEGURO)
# -------------------------
@app.route('/dashboard')
def dashboard():
    clientes = Cliente.query.all()
    return render_template('dashboard.html', clientes=clientes)

# -------------------------
# NUEVO CLIENTE
# -------------------------
@app.route('/nuevo_cliente', methods=['GET', 'POST'])
def nuevo_cliente():
    if request.method == 'POST':
        nombre = request.form['nombre']
        telefono = request.form['telefono']

        nuevo = Cliente(nombre=nombre, telefono=telefono)
        db.session.add(nuevo)
        db.session.commit()

        return redirect('/dashboard')

    return render_template('nuevo_cliente.html')
