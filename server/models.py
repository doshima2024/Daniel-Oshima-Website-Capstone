from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from server.app import db

class Song(db.Model, SerializerMixin):
    __tablename__ = "songs"



    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    artist = db.Column(db.String, nullable=False)
    song_url = db.Column(db.String, nullable=False)

    comments = db.relationship("Comment", back_populates="song", cascade="delete, delete-orphan")

    serialize_rules = ("comments", "-comments.song")

    @validates("title")
    def validate_title(self, key, value):
        if not value or not isinstance(value, str):
            raise TypeError("Title must exist and be a string")
        return value
    
    @validates("artist")
    def validate_artist(self, key, value):
        if not value or not isinstance(value, str):
            raise TypeError("Artist must exist and be a string")
        return value
    
    @validates("song_url")
    def validate_song_url(self, key, value):
        if not value or not isinstance(value, str):
            raise TypeError("Song URL must exist and be a string")
        return value

class Comment(db.Model, SerializerMixin):
    __tablename__ = "comments"
    
 
    
    id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column(db.Integer, db.ForeignKey("songs.id"), nullable=False)
    user_name = db.Column(db.String, nullable=False)
    comment_content = db.Column(db.String, nullable=False)

    song = db.relationship("Song", back_populates="comments")

    serialize_rules = ("song", "-song.comments")

    @validates("user_name")
    def validate_title(self, key, value):
        if not value or not isinstance(value, str):
            raise TypeError("Username must exist and be a string")
        return value
    
    @validates("comment_content")
    def validate_comment_content(self, key, value):
        if not value or not isinstance(value, str):
            raise TypeError("Comment must exist and be a string")
        if len(value) > 250:
            raise ValueError("Maximum characters for comment is 250")
        return value

class Guestbook(db.Model, SerializerMixin):
    __tablename__ = "guestbooks"
    
  
    
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String, nullable=False)
    entry_content = db.Column(db.String, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "entry_content": self.entry_content
        }

   # @validates("user_name")
    
  #  def validate_user_name(self, key, value):
        #debugging
  #      print(f"Validating user_name: {value}")
   #     if not value or not isinstance(value, str):
    #        raise TypeError("User name must exist and be a string")
  #      return value

  #  @validates("entry_content")
  #  def validate_entry_content(self, key, value):
        #debugging
  #      print(f"Validating entry_content: {value}")
  #      if not value or not isinstance(value, str):
  #          raise TypeError("Entry must exist and be a string")
  #      if len(value) > 250:
   #         raise ValueError("Entry must be less than 250 characters")
