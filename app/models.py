from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(125), nullable=False, unique=True)
    email = db.Column(db.String(125), nullable=False, unique=True)
    password_hash = db.Column(db.String(512), nullable=False)  # 确保这里的字段名是password_hash

    def set_password(self, password):
        """设置密码，使用哈希加盐加密"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """检查密码是否匹配"""
        return check_password_hash(self.password_hash, password)
