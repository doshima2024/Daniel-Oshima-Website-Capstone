from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from app.py import db

class Song(db.Model):
    __tablename__ = "songs"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    artist = db.Column(db.String, nullable=False)
    song_url = db.Column(db.String, nullable=False)

    