def get_temperature_advice(temperature):
    """Return clothing advice based on temperature."""

    if temperature >= 25:
        return "Wear a T-shirt, shorts and light footwear."
    elif temperature >= 18:
        return "Wear a T-shirt with jeans or light trousers."
    elif temperature >= 10:
        return "Wear a jumper or a light jacket."
    elif temperature >= 5:
        return "Wear a warm jacket and consider layering."
    else:
        return "Wear a thick coat, warm layers, gloves and a scarf."


def get_weather_advice(description):
    """Return additional advice based on the weather description."""

    description = description.lower()
    advice = []

    if "rain" in description or "drizzle" in description:
        advice.append("Take an umbrella or wear a waterproof jacket.")

    if "snow" in description:
        advice.append("Wear waterproof shoes and take care on slippery surfaces.")

    if "thunderstorm" in description:
        advice.append("Avoid unnecessary outdoor activities where possible.")

    if "clear" in description:
        advice.append("Consider sunglasses if you are going outside.")

    return advice


def get_wind_advice(wind_speed):
    """Return additional advice based on wind speed."""

    if wind_speed >= 15:
        return "Wear a windproof outer layer and be careful in strong winds."
    elif wind_speed >= 8:
        return "A wind-resistant jacket may be useful."

    return None




def get_forecast_advice(forecast_summary):
    """Return advice based on weather expected later."""

    advice = []

    if forecast_summary["rain_expected"]:
        advice.append(
            "It may be dry now, but rain is expected later. "
            "Take an umbrella or waterproof jacket."
        )

    if forecast_summary["snow_expected"]:
        advice.append(
            "Snow is expected later, so wear warm and waterproof footwear."
        )

    if forecast_summary["strongest_wind"] >= 8:
        advice.append(
            "Wind speeds are expected to increase, so take a windproof layer."
        )

    return advice




def clothing_recommendation(
    temperature,
    description,
    wind_speed,
    forecast_summary=None
):
    recommendations = [
        get_temperature_advice(temperature)
    ]

    recommendations.extend(
        get_weather_advice(description)
    )

    wind_advice = get_wind_advice(wind_speed)

    if wind_advice:
        recommendations.append(wind_advice)

    if forecast_summary:
        recommendations.extend(
            get_forecast_advice(forecast_summary)
        )

    return recommendations



