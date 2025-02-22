from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.exc import IntegrityError
from sqlalchemy_serializer import SerializerMixin

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:Dubspot8320!@localhost/db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['JSON_COMPACT'] = False

@app.route('/')
def home():
    return "Testing!"

db = SQLAlchemy(app)
migrate = Migrate(app,db)

if __name__ == "__main__":
    app.run(debug=True)