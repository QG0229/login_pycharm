from app import create_app, db
from app.models import User

app = create_app()
with app.app_context():
    db.create_all()

    # 添加测试用户
    if not User.query.filter_by(email='2608333463@qq.com').first():
        user = User(username='sunguangxu', email='2608333463@qq.com')
        user.set_password('123456')
        db.session.add(user)
        db.session.commit()
        print("数据库和测试用户创建成功")
    else:
        print("用户已存在")