from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .config import Config

# 初始化扩展
db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # 初始化扩展
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'

    # 注册蓝图
    from .routes import main
    app.register_blueprint(main)

    # 导入模型，防止循环导入
    from . import models

    return app