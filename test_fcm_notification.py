import requests
import json

# Firebase Cloud Messaging API endpoint
FCM_API_URL = "https://fcm.googleapis.com/fcm/send"
API_KEY = "pub_587319bcec44a314b9b38b40d5d5af6b5ccb3"  # Provided API key

# Set the headers including the API Key
headers = {
    "Authorization": f"key={API_KEY}",
    "Content-Type": "application/json"
}

# Payload with notification details
payload = {
    "to": "YOUR_FCM_TOKEN",  # Replace with actual FCM token
    "notification": {
        "title": "Test Notification",
        "body": "This is a test message sent via FCM",
        "click_action": "FLUTTER_NOTIFICATION_CLICK"  # Required for handling notifications in some cases
    },
    "priority": "high"
}

# Send the POST request to FCM API
response = requests.post(FCM_API_URL, headers=headers, json=payload)

# Output results
if response.status_code == 200:
    print("Notification sent successfully.")
    print("Response:", response.json())
else:
    print("Failed to send notification.")
    print("Status Code:", response.status_code)
    print("Response:", response.text)
