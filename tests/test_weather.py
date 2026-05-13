"""Testes de integração do módulo de clima."""

from unittest.mock import patch, MagicMock
import json

from src.weather import get_temperature, get_water_recommendation


def test_get_temperature_success():
    """Testa se a temperatura é retornada corretamente da API."""
    mock_response = MagicMock()
    mock_response.read.return_value = json.dumps({
        "current_weather": {"temperature": 32.5}
    }).encode()
    mock_response.__enter__ = lambda s: s
    mock_response.__exit__ = MagicMock(return_value=False)

    with patch("urllib.request.urlopen", return_value=mock_response):
        temp = get_temperature(-15.78, -47.93)
        assert temp == 32.5


def test_get_temperature_failure():
    """Testa se retorna None quando a API falha."""
    with patch("urllib.request.urlopen", side_effect=Exception("timeout")):
        temp = get_temperature(-15.78, -47.93)
        assert temp is None


def test_recommendation_extreme_heat():
    """Testa recomendação para calor extremo."""
    rec = get_water_recommendation(36.0)
    assert rec["extra_ml"] == 1000


def test_recommendation_hot():
    """Testa recomendação para dia quente."""
    rec = get_water_recommendation(30.0)
    assert rec["extra_ml"] == 500


def test_recommendation_mild():
    """Testa recomendação para temperatura agradável."""
    rec = get_water_recommendation(24.0)
    assert rec["extra_ml"] == 200


def test_recommendation_cold():
    """Testa recomendação para dia frio."""
    rec = get_water_recommendation(15.0)
    assert rec["extra_ml"] == 0
    