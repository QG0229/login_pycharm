from app import create_app, db  # 从 app 包导入应用工厂函数和数据库对象
from app.models import User  # 导入用户模型

app = create_app()  # 创建 Flask 应用实例
with app.app_context():  # 进入应用上下文，确保可以操作数据库等应用资源
    db.create_all()  # 创建数据库中的所有表（如果尚未创建）

    # 添加测试用户（如果该邮箱用户不存在）
    if not User.query.filter_by(email='2608333463@qq.com').first():
        user = User(username='sunguangxu', email='2608333463@qq.com')  # 创建用户实例
        user.set_password('123456')  # 设置用户密码（加密）
        db.session.add(user)  # 添加用户到数据库会话
        db.session.commit()  # 提交会话保存到数据库
        print("数据库和测试用户创建成功")  # 控制台输出提示
    else:
        print("用户已存在")  # 如果用户已存在，输出提示信息
