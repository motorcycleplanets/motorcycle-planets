from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "<h1>Motorcycle Planets V14 PRO</h1><p>Sistema funcionando correctamente 🚀</p>"
