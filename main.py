from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import csv
from cafe_form import CafeForm

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)




# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")

        print(form.cafe.data)
        print(form.opening_time.data)
        print(form.ratings.choices)

        print(form.data)

        data_string = ""
        for key, value in form.data.items():
            if key == "ratings":
                print(value)
                print(dict(form.ratings.choices).get(value))
                data_string += f"{dict(form.ratings.choices).get(value)},"
            elif key == "wifi_strength_rating":
                data_string += f"{dict(form.wifi_strength_rating.choices).get(value)},"
            elif key == "power_socket_availability":
                data_string += f"{dict(form.power_socket_availability.choices).get(value)},"
            elif key in ("cafe", "location", "opening_time", "closing_time"):
                data_string += f"{value},"

        print(data_string[:-1])
        final_string = data_string[:-1]
        with open("cafe-data.csv", "a", encoding="utf-8") as data_file:
            data_file.write(f"\n{final_string}")


    else:
        print("False")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)

    print(list_of_rows)
    print("https://goo.gl/maps/13Tjc36HuPWLELaSA"[0:5])
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
