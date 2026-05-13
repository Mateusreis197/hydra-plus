"""Módulo de integração com a API Open-Meteo para dados climáticos."""

import urllib.request
import json


def get_temperature(latitude: float, longitude: float) -> float | None:
    """Busca a temperatura atual via API Open-Meteo."""
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}&longitude={longitude}"
        f"&current_weather=true"
    )
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            data = json.loads(response.read().decode())
            return data["current_weather"]["temperature"]
    except Exception:
        return None


def get_water_recommendation(temperature: float) -> dict:
    """Retorna recomendação de consumo baseada na temperatura."""
    if temperature >= 35:
        extra = 1000
        message = "🌡️ Calor extremo! Beba pelo menos 1L extra de água hoje."
    elif temperature >= 28:
        extra = 500
        message = "☀️ Dia quente! Recomenda-se 500ml extras de água."
    elif temperature >= 20:
        extra = 200
        message = "🌤️ Temperatura agradável. Beba 200ml extras por precaução."
    else:
        extra = 0
        message = "❄️ Dia fresco. Mantenha sua meta normal de hidratação."

    return {"extra_ml": extra, "message": message}