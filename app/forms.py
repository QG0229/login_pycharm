from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
import re  # 导入re模块，用于正则表达式
from flask_login import current_user  # 导入 current_user

class LoginForm(FlaskForm):
    email = StringField('邮箱', validators=[DataRequired(), Email()])
    password = PasswordField('密码', validators=[DataRequired()])
    submit = SubmitField('登录')

class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('旧密码', validators=[DataRequired()])
    new_password = PasswordField('新密码', validators=[DataRequired()])
    confirm_password = PasswordField('确认新密码', validators=[
        DataRequired(),
        EqualTo('new_password', message='两次密码输入不一致')
    ])
    submit = SubmitField('修改密码')

    # 原密码的验证
    def validate_old_password(self, field):
        if not current_user.check_password(field.data):  # 验证原密码是否正确
            raise ValidationError('原密码错误')

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
