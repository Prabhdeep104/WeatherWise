from flask import Flask, render_template, request

from weather import get_weather
from clothing import get_clothing_recommendation


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    weather_data = None
    clothing_advice = None
    error = None

    if request.method == "POST":

        city = request.form.get("city")

        if city:
            weather_data = get_weather(city)

            if weather_data["success"]:
                clothing_advice = get_clothing_recommendation(weather_data)
            else:
                error = weather_data["message"]

        else:
            error = "Please enter a city name."


    return render_template(
        "index.html",
        weather=weather_data,
        clothing=clothing_advice,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)