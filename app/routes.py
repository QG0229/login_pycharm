from flask import Blueprint, render_template, redirect, url_for, flash, request  # 导入 Flask 核心模块
from flask_login import login_user, logout_user, current_user, login_required  # 导入登录管理相关函数
from .forms import LoginForm, ChangePasswordForm  # 导入表单类
from .models import User  # 导入用户模型
from . import db, login_manager  # 导入数据库对象和登录管理器

# 创建一个名为 'main' 的蓝图，用于管理主路由
main = Blueprint('main', __name__)

# 注册用户加载回调函数，用于通过用户 ID 加载用户对象
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  # 根据用户ID从数据库查询用户

# 首页路由
@main.route('/')
def home():
    return render_template('index.html')  # 渲染首页模板

# 登录页面路由，支持 GET 和 POST 方法
@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()  # 创建登录表单实例
    if form.validate_on_submit():  # 如果表单提交并验证通过
        user = User.query.filter_by(email=form.email.data).first()  # 查询邮箱对应的用户
        if user and user.check_password(form.password.data):  # 验证密码正确
            # ✅ 如果用户未勾选“记住我”，先清除已有的持久登录状态
            if not form.remember.data:
                logout_user()
            login_user(user, remember=form.remember.data)  # 登录用户，设置 remember_me 状态
            return redirect(url_for('main.home'))  # 跳转到首页
        else:
            flash('邮箱或密码错误')  # 提示登录失败
    return render_template('login.html', form=form)  # 渲染登录模板并传入表单

# 注销登录路由，必须已登录才能访问
@main.route('/logout')
@login_required
def logout():
    logout_user()  # 注销当前用户
    return redirect(url_for('main.login'))  # 重定向到登录页

# 修改密码页面路由，支持 GET 和 POST 方法
@main.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePasswordForm()  # 创建修改密码表单实例
    if form.validate_on_submit():  # 表单验证通过
        if current_user.check_password(form.old_password.data):  # 验证原密码是否正确
            current_user.set_password(form.new_password.data)  # 设置新密码
            try:
                db.session.commit()  # 提交数据库更改
                flash('密码修改成功！请重新登录~ ٩(๑•̀ω•́๑)۶')  # 成功提示
                logout_user()  # 强制退出登录
                return redirect(url_for('main.home'))  # 重定向到首页
            except Exception as e:
                db.session.rollback()  # 如果失败则回滚事务
                flash('密码修改失败，请稍后再试')  # 提示错误
        else:
            flash('原密码错误')  # 原密码错误提示
    return render_template('change_password.html', form=form)  # 渲染修改密码页面并传入表单

# 小组成员页面路由
@main.route('/members')
def members():
    return render_template('members.html')  # 渲染成员展示页面
