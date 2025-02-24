from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from flask_migrate import Migrate
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.exc import IntegrityError
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://apple:Dubspot8320!@localhost/db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['JSON_COMPACT'] = False


db = SQLAlchemy(app)
migrate = Migrate(app,db)

from server.models import *

#GET/songs : retrieves all songs from the backend for display on the songs page upon load.
#(Tested via Postman)

@app.get("/songs")
def get_songs():
    try:
        songs = Song.query.all()
        return jsonify([song.to_dict() for song in songs])
    except Exception as exception:
        return jsonify({"error": str(exception)}), 500
    
# GET /songs/search/<string:query> : Allows users to search for a song by name.
#(Tested via Postman)

@app.get("/songs/search/<string:query>")
def search_song(query):
    try:
        query = query.strip()
        songs = Song.query.filter(Song.title.ilike(f"%{query}%")).all()
        return jsonify([song.to_dict() for song in songs])
    except Exception as exception:
        return jsonify({"error": str(exception)}), 500
    
# GET/song/<int:id>/comments : Returns all comments for a specific song
#(Tested in Postman)

@app.get("/song/<int:id>/comments")
def get_comments(id):
    song = Song.query.where(Song.id == id).first()
    if song:
        return jsonify([comment.to_dict() for comment in song.comments]), 200
    else:
        return jsonify({"error": "That song doesn't exist."}), 404
    


if __name__ == "__main__":
    app.run(debug=True)