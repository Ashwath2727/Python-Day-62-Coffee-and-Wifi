from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField
from wtforms.fields.choices import SelectField
from wtforms.validators import DataRequired, URL


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired(message="This field is required")])

    location = StringField(
        label="Cafe Location on Google Maps (URL)",
        validators=[DataRequired(message="This field is required"), URL(message="Please enter a valid Google Maps URL")]
    )

    opening_time = StringField(label="Opening Time e.g. 8AM", validators=[DataRequired(message="This field is required")])

    closing_time = StringField(label="Closing Time e.g. 5:30PM", validators=[DataRequired(message="This field is required")])

    coffee_ratings_list = [("1", "✘")]
    coffee_ratings_list.extend([(str(i), ("☕"*(i-1) ) ) for i in range(2, 7)])
    print(coffee_ratings_list)
    ratings = SelectField(
        label="Coffee Ratings",
        validators=[DataRequired(message="This field is required")],
        choices=coffee_ratings_list
    )

    wifi_strength_rating_list = [("1", "✘")]
    wifi_strength_rating_list.extend([(str(i), ("💪"*(i-1) ) ) for i in range(2, 7)])
    wifi_strength_rating = SelectField(
        label="Wifi Strength Raating",
        validators=[DataRequired(message="This field is required")],
        choices=wifi_strength_rating_list
    )

    power_socket_availability_list = [("1", "✘")]
    power_socket_availability_list.extend([(str(i), ("🔌"*(i-1) ) ) for i in range(2, 7)])
    power_socket_availability = SelectField(
        label="Power Socket Availability",
        validators=[DataRequired()],
        choices=power_socket_availability_list
    )

    submit = SubmitField('Submit')