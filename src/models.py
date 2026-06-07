
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), nullable=False)
    first_name = db.Column(db.String(250), nullable=False)
    last_name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)

    posts = db.relationship("Post", backref="user", lazy=True)
    comments = db.relationship("Comment", backref="author", lazy=True)

    followers_from = db.relationship(
        "Follower",
        foreign_keys="Follower.user_from_id",
        backref="user_from",
        lazy=True,
    )
    followers_to = db.relationship(
        "Follower",
        foreign_keys="Follower.user_to_id",
        backref="user_to",
        lazy=True,
    )


class Follower(db.Model):
    __tablename__ = "follower"

    id = db.Column(db.Integer, primary_key=True)
    user_from_id = db.Column(
        db.Integer, db.ForeignKey("user.id"), nullable=False)
    user_to_id = db.Column(
        db.Integer, db.ForeignKey("user.id"), nullable=False)


class Post(db.Model):
    __tablename__ = "post"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    media = db.relationship("Media", backref="post", lazy=True)
    comments = db.relationship("Comment", backref="post", lazy=True)


class Media(db.Model):
    __tablename__ = "media"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(250), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=False)


class Comment(db.Model):
    __tablename__ = "comment"

    id = db.Column(db.Integer, primary_key=True)
    comment_text = db.Column(db.String(250), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=False)
