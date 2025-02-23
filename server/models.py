from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from app import db

class Song(db.Model, SerializerMixin):
    __tablename__ = "songs"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    artist = db.Column(db.String, nullable=False)
    song_url = db.Column(db.String, nullable=False)

    comments = db.relationship("Comment", back_populates="song", cascade="delete, delete-orphan")

    serialize_rules = ("comments", "-comments.song")

class Comment(db.Model, SerializerMixin):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey("songs.id"), nullable=False)
    user_name = db.Column(db.String, nullable=False)
    comment_content = db.Column(db.String, nullable=False)

    song = db.relationship("Song", back_populates="comments")

    serialize_rules = ("song", "-song.comments")