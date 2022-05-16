from wtforms import SubmitField, BooleanField, StringField, PasswordField, validators
from flask_wtf import FlaskForm
    
class OTPForm(FlaskForm):
    email = StringField('Email Address', [validators.DataRequired(), validators.Email(), validators.Length(min=6, max=35)])
    submit = SubmitField('Submit')
    
class AuthenForm(FlaskForm):
    otp = StringField('OTP', [validators.DataRequired(), validators.Length(min=6, max=6)])
    submit = SubmitField('Submit')
    
class RegForm(FlaskForm):
    name_first = StringField('ชื่อ', [validators.DataRequired()])
    name_last = StringField('นามสกุล', [validators.DataRequired()])
    submit = SubmitField('Submit')    
    