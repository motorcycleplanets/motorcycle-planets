
from flask import Flask

app = Flask(_ _name_ _)

@app.route('/')
def home():
    return """
    <h1>Motorcycle Planets V14 PRO</h1>
    <p>Sistema funcionando correctamente 🚀</p>
    """

if _name_ == '_main_':
    app.run()
