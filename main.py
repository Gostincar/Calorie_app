from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template
from flask import request
from calorie import Calorie
from temperature import Temperature

app = Flask(__name__)
# Genereting home page for the app
class HomePage(MethodView):
    def get(self):
        return render_template('index.html')

class CaloriesFromPage(MethodView):
    # get method is displaying the form ( caloriesForm )  into the page
    def get(self):
        calories_form = CaloriesForm()
        return render_template('calories_form_page.html', caloriesform = calories_form )


# post method is providing results by pressing the button on the webpage.
    def post(self):
        calories_form = CaloriesForm(request.form)
# initializing the temperature class
        temperature = Temperature( country= calories_form.country.data, city=calories_form.city.data).get()
# initializing the calorie class
        calorie = Calorie( weight= float(calories_form.weight.data),
                           height = float(calories_form.height.data),
                           age = float(calories_form.age.data),
                           temperature= temperature )

        calories = calorie.calculate()



        return  render_template('calories_form_page.html',
                                caloriesform = calories_form,
                                calories = calories,
                                temperature = temperature,
                                result = True )


class CaloriesForm(Form):
    weight = StringField("Weight: ", default=70)
    height = StringField("Height: ",default=175)
    age = StringField("Age: ", default=32)
    country =StringField("Country: ", default="serbia")
    city = StringField("City: ", default="belgrade")
    button = SubmitField("Calculate")

# when user visits the home page, HomePage class will be initialised
app.add_url_rule('/',
                 view_func= HomePage.as_view('home_page'))
# when the user visits the CaloriesForm, this page will be initialized
app.add_url_rule('/calories_form',
                 view_func=CaloriesFromPage.as_view('calories_form_page'))

app.run(debug=True)
