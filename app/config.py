import os
from datetime import timedelta

class Config:
    # Flask 的加密密钥，用于保护 session、表单等数据，自动生成 24 字节的随机密钥
    SECRET_KEY = os.urandom(24)

    # 数据库连接地址：使用 PyMySQL 连接本地 MySQL 数据库 user_login，编码为 utf8mb4
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost/user_login?charset=utf8mb4'

    # 是否追踪对象的修改并发送信号，关闭可以节省资源
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # “记住我”功能的 Cookie 有效期，设置为 7 天
    REMEMBER_COOKIE_DURATION = timedelta(days=7)
