from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class ContactFrom(FlaskForm):
    name = StringField("Teste", validators=[DataRequired()])
    email = EmailField("Email")
    telephone = StringField("Telefone")
    subject = StringField("Assunto")
    message = TextAreaField("Mensagem")
    submit = SubmitField("Enviar")
