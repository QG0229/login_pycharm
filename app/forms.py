from flask_wtf import FlaskForm  # 导入 Flask-WTF 提供的表单基类
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError  # 导入字段验证器
import re  # 导入 re 模块，用于正则表达式操作
from flask_login import current_user  # 导入当前登录用户对象
from wtforms import StringField, PasswordField, BooleanField, SubmitField  # 导入表单字段类

# 登录表单类
class LoginForm(FlaskForm):
    # 邮箱输入框，要求必填且格式为邮箱
    email = StringField('邮箱', validators=[DataRequired(), Email()])
    # 密码输入框，要求必填
    password = PasswordField('密码', validators=[DataRequired()])
    # 记住我复选框（用于记住登录状态）
    remember = BooleanField('记住我')  # ✅ 新增
    # 登录按钮
    submit = SubmitField('登录')

# 修改密码表单类
class ChangePasswordForm(FlaskForm):
    # 旧密码输入框，要求必填
    old_password = PasswordField('旧密码', validators=[DataRequired()])
    # 新密码输入框，要求必填
    new_password = PasswordField('新密码', validators=[DataRequired()])
    # 确认新密码，要求必填且与新密码一致
    confirm_password = PasswordField('确认新密码', validators=[
        DataRequired(),
        EqualTo('new_password', message='两次密码输入不一致')
    ])
    # 修改密码按钮
    submit = SubmitField('修改密码')

    # 自定义验证方法：验证旧密码是否正确
    def validate_old_password(self, field):
        if not current_user.check_password(field.data):  # 验证原密码是否正确
            raise ValidationError('原密码错误')  # 抛出验证错误提示

    # 自定义验证方法：验证新密码的强度
    def validate_new_password(self, field):
        password = field.data
        if not 6 <= len(password) <= 12:
            raise ValidationError('密码长度必须在6到12位之间')

        # 至少包含两种字符类型：数字、大写字母、小写字母
        types = 0
        if re.search(r'\d', password):
            types += 1
        if re.search(r'[a-z]', password):
            types += 1
        if re.search(r'[A-Z]', password):
            types += 1
        if types < 2:
            raise ValidationError('密码必须包含数字、大写字母、小写字母中的至少两种')
