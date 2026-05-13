"""Testes automatizados do Hydra+."""

import pytest
from src.hydra import add_consumption, get_progress, set_goal


def make_data():
    """Cria um dicionário de dados base para testes."""
    return {"goal_ml": 2000, "records": {}}


def test_set_goal_valid():
    """Testa se a meta é definida corretamente."""
    data = make_data()
    data = set_goal(data, 3000)
    assert data["goal_ml"] == 3000


def test_set_goal_invalid():
    """Testa se valor negativo lança erro."""
    data = make_data()
    with pytest.raises(ValueError):
        set_goal(data, -500)


def test_set_goal_zero():
    """Testa se meta zero lança erro."""
    data = make_data()
    with pytest.raises(ValueError):
        set_goal(data, 0)


def test_add_consumption_valid():
    """Testa registro de consumo válido."""
    data = make_data()
    data = add_consumption(data, 300)
    progress = get_progress(data)
    assert progress["consumed"] == 300


def test_add_consumption_invalid():
    """Testa se valor negativo lança erro."""
    data = make_data()
    with pytest.raises(ValueError):
        add_consumption(data, -100)


def test_add_consumption_accumulates():
    """Testa se consumo acumula corretamente."""
    data = make_data()
    data = add_consumption(data, 300)
    data = add_consumption(data, 500)
    progress = get_progress(data)
    assert progress["consumed"] == 800


def test_progress_percentage():
    """Testa cálculo correto do progresso."""
    data = make_data()
    data = add_consumption(data, 1000)
    progress = get_progress(data)
    assert progress["percentage"] == 50.0


def test_progress_max_100():
    """Testa se progresso não passa de 100%."""
    data = make_data()
    data = add_consumption(data, 5000)
    progress = get_progress(data)
    assert progress["percentage"] == 100.0