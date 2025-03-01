from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from flask_migrate import Migrate
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.exc import IntegrityError
from flask_cors import CORS
import requests


app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://apple:Dubspot8320!@localhost/db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['JSON_COMPACT'] = False
CLIENT_ID = "88e3f8b8ba3f44d5bd49f2caf86d0f00"
CLIENT_SECRET = "0554e796355b42f99e31a4be2905cc0d"


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
  

    if data is None:
        return jsonify({"error": "Invalid JSON formatting"}), 400
    user_name = data.get("user_name")
    entry_content = data.get("entry_content")

   

    if not user_name or not entry_content:
        return jsonify({"error" : " User name and Guestbook entry are required fields"}), 400
    
    new_entry = Guestbook(user_name=user_name, entry_content=entry_content)

    try:
        db.session.add(new_entry)
        db.session.commit()
        return jsonify(new_entry.to_dict()), 201
    except Exception as exception:
        db.session.rollback()
        return jsonify({"error": str(exception)}), 500
    

# Function to retrieve a Spotify authentication token

def get_token():
    response = requests.post("https://accounts.spotify.com/api/token", 
        data={
            "grant_type": "client_credentials",
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET
        }, headers={
            "Content-Type": "application/x-www-form-urlencoded",
        })
       
    if response.ok:
        return response.json().get("access_token")
    else:
        raise Exception("Failed to retrieve access token")
    
#GET/search will be used to retrieve track search results from Spotify's API

@app.get("/search")
def search_spotify_tracks():
    query = request.args.get("q")
    if not query:
        return jsonify({"error": "No search query provided"}), 400
    
    token = get_token()
    if not token:
        return jsonify({"error": "Failed to get token for access"})
    
    url = f"https://api.spotify.com/v1/search?q={query}%20artist%3ADaniel%20Oshima&type=track"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)

    if response.ok:
        return jsonify(response.json())
    else:
        return jsonify({"error": "API request failed"})



if __name__ == "__main__":
    app.run(debug=True)