# config.py
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///newsarc.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOGGING_LEVEL = os.getenv('LOGGING_LEVEL', 'DEBUG')
