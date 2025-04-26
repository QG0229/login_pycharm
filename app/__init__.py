from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .config import Config

# 初始化扩展（尚未与 app 绑定）
db = SQLAlchemy()
login_manager = LoginManager()

# 应用工厂函数，用于创建并配置 Flask 应用实例
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # 初始化扩展，将其与当前 app 绑定
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'     # 设置未登录用户的默认跳转视图（登录页）

    # 注册蓝图
    from .routes import main
    app.register_blueprint(main)

    # 导入模型，防止循环导入
    from . import models

    return app