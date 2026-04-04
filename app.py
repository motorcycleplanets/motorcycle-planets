
# MOTORCYCLE PLANETS V14 FINAL

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Motorcycle Planets V14 FINAL - Sistema listo para producción</h1>"

if __name__ == "__main__":
    app.run()
