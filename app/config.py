import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:122627@localhost/resgate_animal')
    SQLALCHEMY_TRACK_MODIFICATIONS = False