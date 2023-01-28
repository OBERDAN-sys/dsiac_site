from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
import email_validator

# csrf = CSRFProtect()

class ContactForm(FlaskForm):
    name = StringField(label='Nome', validators=[DataRequired('Nome não pode ficar vazio')])
    email = StringField(label='Email', validators=[DataRequired('Email não pode ficar vazio'),
                                              Email('Informe um email válido')])
    subject = StringField(label='Assunto', validators=[DataRequired('Assunto não pode ficar vazio')])
    message = TextAreaField(label='Mensagem', validators=[DataRequired('Mensagem não pode ficar vazio')])
    submit = SubmitField(label="Enviar")