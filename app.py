
from flask import Flask
import os

app = Flask(_ _name_ _)

@app.route('/')
def home():
    return "<h1>Motorcycle Planets V14 PRO</h1><p>Sistema funcionando correctamente</p>"

if _ _name_ _ == "_ _main_ _":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
