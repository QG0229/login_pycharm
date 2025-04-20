# 此代码 用于添加用户使用
# 这个弃用，使用createdb.py进行创建
from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    # 创建用户
    user = User(username="sunguangxu", email="2608333463@qq.com")
    user.set_password("123456")  # 密码加密
    db.session.add(user)
    db.session.commit()
    print("测试用户添加成功！")
