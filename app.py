
from flask import Flask

app = Flask(_name_)

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>Motorcycle Planets V14 PRO</title>
        <style>
            body {
                background-color: #0d0d0d;
                color: #00ff99;
                font-family: Arial;
                text-align: center;
            }
            .card {
                background: #1a1a1a;
                margin: 20px;
                padding: 20px;
                border-radius: 10px;
            }
            .btn {
                display: inline-block;
                padding: 10px 20px;
                background: #00ff99;
                color: black;
                text-decoration: none;
                border-radius: 5px;
            }
        </style>
    </head>
    <body>

        <h1>Motorcycle Planets V14 PRO</h1>
        <p>Sistema profesional de gestión</p>

        <div class="card">
            <h2>Clientes</h2>
            <p>Gestión completa de clientes</p>
            <a class="btn">Entrar</a>
        </div>

        <div class="card">
            <h2>Ventas</h2>
            <p>Control de ventas del día</p>
            <a class="btn">Entrar</a>
        </div>

        <div class="card">
            <h2>Inventario</h2>
            <p>Control de productos</p>
            <a class="btn">Entrar</a>
        </div>

    </body>
    </html>
    """

if _name_ == '_main_':
    app.run()