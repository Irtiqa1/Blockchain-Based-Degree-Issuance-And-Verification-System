import os
from dotenv import load_dotenv

# Base directory
basedir = os.path.abspath(os.path.dirname(__file__))

# Agar tum local .env use karna chaho to uncomment kardo
# load_dotenv(os.path.join(basedir, '.env'))

class Config:
    # Secret key (session security ke liye)
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-very-secret-key-123')

    # Database URL ko fetch karo
    database_url = os.getenv('DATABASE_URL')

    # Compatibility fix: agar postgres:// se start hota hai to replace karo
    if database_url and database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)

    SQLALCHEMY_DATABASE_URI = database_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Project specific settings
    ADMIN_USERNAMES = ['admin1', 'admin2', 'admin3']
    BLOCKCHAIN_DIFFICULTY = 0

    # JSON blockchain storage path
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ''))
    JSON_STORAGE_PATH = os.path.join(BASE_DIR, 'data', 'blockchain.json')
