from flask import Blueprint, jsonify, request, current_app
from .models import User, News, Category, Engagement, Notification
from . import db, bcrypt
from flask_login import login_user, current_user

api = Blueprint('api', __name__)

@api.route("/news", methods=["GET"])
def get_news():
    """Fetches news articles based on category or keyword search."""
    category_name = request.args.get("category")
    keyword = request.args.get("search")
    news_query = News.query

    if category_name:
        category = Category.query.filter_by(name=category_name).first()
        if category:
            news_query = news_query.filter_by(category_id=category.id)
        else:
            current_app.logger.warning(f"No category found for {category_name}")
            return jsonify({"error": "Category not found"}), 404

    if keyword:
        news_query = news_query.filter(News.title.contains(keyword) | News.content.contains(keyword))

    news_list = news_query.all()
    return jsonify([{"title": news.title, "content": news.content} for news in news_list])

@api.route("/engage", methods=["POST"])
def engage():
    """Records user engagement on news (e.g., likes, comments)."""
    data = request.get_json()
    engagement = Engagement(
        user_id=current_user.id,
        news_id=data['news_id'],
        type=data['type'],
        content=data.get('content', '')
    )
    db.session.add(engagement)
    db.session.commit()
    return jsonify({"message": "Engagement recorded"}), 201

@api.route("/notifications", methods=["GET"])
def get_notifications():
    """Fetches unread notifications for the user."""
    notifications = Notification.query.filter_by(user_id=current_user.id, is_read=False).all()
    return jsonify([{"message": n.message, "is_read": n.is_read} for n in notifications])

@api.route("/notifications/mark_read", methods=["POST"])
def mark_notifications_read():
    """Marks all notifications as read for the user."""
    notifications = Notification.query.filter_by(user_id=current_user.id, is_read=False).all()
    for n in notifications:
        n.is_read = True
    db.session.commit()
    return jsonify({"message": "Notifications marked as read"})
