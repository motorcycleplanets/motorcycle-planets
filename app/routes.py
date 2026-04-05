from app import app, db
from flask import render_template, request, redirect
from app.models import Cliente

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
