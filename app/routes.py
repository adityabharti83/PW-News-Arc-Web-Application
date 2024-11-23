from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from .models import News, Category, User
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    """Homepage route."""
    return render_template("index.html")

@main.route('/feed')
@login_required
def feed():
    """User's personalized news feed based on preferences."""
    preferences = current_user.preferences.split(',') if current_user.preferences else []
    news_feed = News.query.join(Category).filter(Category.name.in_(preferences)).order_by(News.date_posted.desc()).all()
    return render_template("feed.html", news_feed=news_feed)

@main.route('/categories')
def categories():
    """Displays available news categories."""
    categories = Category.query.all()
    return render_template("categories.html", categories=categories)

@main.route('/profile')
@login_required
def profile():
    """Displays the user profile and preferences."""
    return render_template("profile.html", user=current_user)
