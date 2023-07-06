from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, DataRequired, EqualTo, Email, DataRequired, ValidationError
from mercado.models import User

class Cadastroform(FlaskForm):
    def validate_username(self, check_user):
        user = User.query.filter_by(usuario=check_user.data).first()
        if user:
            raise ValidationError('Usuário já existe! Cadastre outro usuário.')

    def validate_username(self, check_email):
        user = User.query.filter_by(usuario=check_email.data).first()
        if user:
            raise ValidationError('Usuário já existe! Cadastre outro e-mail.')
        
    def validate_senha(self, check_senha):
        user = User.query.filter_by(usuario=check_senha.data).first()
        if user:
            raise ValidationError('A senha já existe! Cadastre outra senha.')

    usuario = StringField(label="Username:", validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='E-mail:', validators=[Email(), DataRequired()])
    senhal = PasswordField(label='Senha:', validators=[Length(min=6), DataRequired()])
    senha2 = PasswordField(label='Confirmação de Senha:', validators=[EqualTo('senhal'), DataRequired()])
    submit = SubmitField(label='Cadastrar')

class Loginform(FlaskForm):
    usuario = StringField(label="Usuário", validators= [DataRequired()])
    senha = PasswordField(label="Senha:", validators= [DataRequired()])
    submit = SubmitField(label="Log In")