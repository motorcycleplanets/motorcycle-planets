from app import app, db
from flask import render_template, request, redirect
from app.models import Cliente

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/dashboard')
def dashboard():
    clientes = Cliente.query.all()
    return render_template('dashboard.html', clientes=clientes)


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


@app.route('/init_db')
def init_db():
    with app.app_context():
        db.create_all()
    return "Base de datos creada correctamente"
