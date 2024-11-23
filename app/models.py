from . import db
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    """Load user by ID for Flask-Login."""
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    """User model to store user details and preferences."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    preferences = db.Column(db.String(200))  # Preferences for personalized feed

class Category(db.Model):
    """Category model to organize news by category."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

class News(db.Model):
    """News model to store news articles and associated categories."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref='news')
    date_posted = db.Column(db.DateTime, default=db.func.current_timestamp())

class Engagement(db.Model):
    """Engagement model to track user interactions (e.g., likes, comments)."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    news_id = db.Column(db.Integer, db.ForeignKey('news.id'))
    type = db.Column(db.String(50))  # 'like', 'comment', 'bookmark'
    content = db.Column(db.Text)  # Comment content

class Notification(db.Model):
    """Notification model to track notifications sent to users."""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    message = db.Column(db.String(255))
    is_read = db.Column(db.Boolean, default=False)
