from flask import Flask, jsonify, request
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
    
#POST/ comments/<int:id> : Allows users to comment on a specific song 
#(Tested with Postman)

@app.post("/comments/<int:id>")
def post_comment(id):
    song = Song.query.where(Song.id == id).first()
    if not song:
        return jsonify({"error": "Song not found."}), 404
    data = request.json
    user_name = data.get("user_name")
    comment_content = data.get("comment_content")

    if not user_name or not comment_content:
        return jsonify({"error": "User name and comment are required fields."}), 400
    
    new_comment = Comment(song_id=id, user_name=user_name, comment_content=comment_content)

    try:
        db.session.add(new_comment)
        db.session.commit()
        return jsonify(new_comment.to_dict()), 201
    except Exception as exception:
        return jsonify({"error": str(exception)}), 500
    
#GET/ Guestbook : retrieves all guestbook entries to display on home page on load
#(Tested via Postman)

@app.get("/guestbook")
def get_guestbook_entries():
    try:
        entries = Guestbook.query.all()
        return jsonify([entry.to_dict() for entry in entries])
    except Exception as exception:
        return jsonify({"error": str(exception)}), 500
    
# POST/Guestbook : Allows users to post an entry in the “Guestbook” on the home page, this is separate from the comments which will be located on the Songs page and tied to a specific song.

@app.post("/guestbook")
def post_guestbook_entry():
    data = request.json
    #debugging
    print("Request JSON:", data)

    if data is None:
        return jsonify({"error": "Invalid JSON formatting"}), 400
    user_name = data.get("user_name")
    entry_content = data.get("entry_content")

    #debugging
    print(f"user_name: {user_name}, entry_content: {entry_content}")

    if not user_name or not entry_content:
        return jsonify({"error" : " User name and Guestbook entry are required fields"}), 400
    
    new_entry = Guestbook(user_name=user_name, entry_content=entry_content)

    #debugging

    print("Session dirty:", db.session.dirty)
    print("Session new:", db.session.new)
    print("New entry object:", new_entry.__dict__)
    try:
        db.session.add(new_entry)
        db.session.commit()
        return jsonify(new_entry.to_dict()), 201
    except Exception as exception:
        db.session.rollback()
        #debugging:
        print("Database Error:", str(exception))
        return jsonify({"error": str(exception)}), 500

    


if __name__ == "__main__":
    app.run(debug=True)