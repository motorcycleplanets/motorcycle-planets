from app import app, db

with app.app_context():
    db.create_all()

if _name_ == '_main_':
    app.run(debug=True)
