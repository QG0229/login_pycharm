# app/routes.py
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user, login_required
from .forms import LoginForm, ChangePasswordForm
from .models import User
from . import db, login_manager

main = Blueprint('main', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            print("✅ 登录成功！")
            login_user(user)
            return redirect(url_for('main.home'))
        else:
            print("❌ 登录失败！")
            flash('邮箱或密码错误')
    return render_template('login.html', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))

@main.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        if current_user.check_password(form.old_password.data):
            current_user.set_password(form.new_password.data)
            try:
                db.session.commit()
                flash('密码修改成功！请重新登录~ ٩(๑•̀ω•́๑)۶')
                logout_user()
                return redirect(url_for('main.home'))  # 返回未登录首页
            except Exception as e:
                db.session.rollback()
                flash('密码修改失败，请稍后再试')
        else:
            flash('原密码错误')
    return render_template('change_password.html', form=form)
