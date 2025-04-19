import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost/user_login?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
