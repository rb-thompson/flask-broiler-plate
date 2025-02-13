import os
from dotenv import load_dotenv
load_dotenv()

# Application configuration

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret')

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False