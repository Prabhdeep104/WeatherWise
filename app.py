from clothing import clothing_recommendation
from forecast import get_forecast, analyse_upcoming_weather
from flask import Flask, render_template, request
from weather import get_weather

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    recommendations = None
    error_message = None

    if request.method == "POST":
        city = request.form.get("city", "").strip()

        if not city:
            error_message = "Please enter a city."

        else:
            result = get_weather(city)

            if result["success"]:
                weather_data = result

                # Get the forecast
                forecast_result = get_forecast(city)
                forecast_summary = None

                if forecast_result["success"]:
                    forecast_summary = analyse_upcoming_weather(
                        forecast_result["forecasts"],
                        hours_ahead=12
                    )

                print("ICON:", weather_data["icon"])

                # Generate clothing recommendations
                recommendations = clothing_recommendation(
                    temperature=weather_data["temperature"],
                    description=weather_data["description"],
                    wind_speed=weather_data["wind"],
                    forecast_summary=forecast_summary
                )

            else:
                error_message = result["error"]

    print("RECOMMENDATIONS:", recommendations)

    return render_template(
        "index.html",
        weather=weather_data,
        recommendations=recommendations,
        error=error_message
    )


if __name__ == "__main__":
    app.run(debug=True)