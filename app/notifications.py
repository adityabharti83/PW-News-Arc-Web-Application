import requests
from flask import current_app

API_KEY = "pub_587319bcec44a314b9b38b40d5d5af6b5ccb3"  # Use the provided API key

def send_notification(user_id, message):
    """Sends a push notification to a user using Firebase Cloud Messaging (FCM)."""
    fcm_endpoint = "https://fcm.googleapis.com/fcm/send"
    headers = {
        "Authorization": f"key={API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "to": f"/topics/user_{user_id}",
        "notification": {
            "title": "NewsArc Notification",
            "body": message
        }
    }

    response = requests.post(fcm_endpoint, headers=headers, json=payload)
    if response.status_code == 200:
        current_app.logger.info("Notification sent successfully.")
    else:
        current_app.logger.error(f"Failed to send notification: {response.text}")
