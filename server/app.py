from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from flask_migrate import Migrate
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.exc import IntegrityError


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://apple:Dubspot8320!@localhost/db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['JSON_COMPACT'] = False


db = SQLAlchemy(app)
migrate = Migrate(app,db)

from server.models import *

@app.route('/')
def home():
    return "Testing!"

if __name__ == "__main__":
    app.run(debug=True)