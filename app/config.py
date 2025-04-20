import os
from datetime import timedelta

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost/user_login?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 记住我 cookie 的有效期
    REMEMBER_COOKIE_DURATION = timedelta(days=7)