from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import ValidationError, DataRequired
from wtforms.widgets import html5

class InputForm(FlaskForm):
    x = IntegerField('First Integer', validators=[DataRequired()], widget=html5.NumberInput())
    y = IntegerField('Second Integer', validators=[DataRequired()], widget=html5.NumberInput())
    submit = SubmitField('Calculate')