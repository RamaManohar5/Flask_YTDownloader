from app import app
from flask import Blueprint

app_bp = Blueprint(__file__)

app.register_blueprint(app_bp)

if __name__ == "__main__":
    app.run(debug=True)