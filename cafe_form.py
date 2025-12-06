from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    submit = SubmitField('Submit')