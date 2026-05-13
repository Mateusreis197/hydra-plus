"""Hydra+ — Assistente de Hidratação e Autocuidado."""

import json
import os
from datetime import date

from src.weather import get_temperature, get_water_recommendation

DATA_FILE = "data.json"

# Coordenadas padrão: Brasília, Brasil
DEFAULT_LATITUDE = -15.7801
DEFAULT_LONGITUDE = -47.9292

MOTIVATIONAL_PHRASES = [
    "💧 Cada gole conta! Continue assim!",
    "🌊 Seu corpo agradece pela hidratação!",
    "⚡ Água é energia! Você está indo bem!",
    "🏆 Ótimo hábito! Continue hidratado!",
    "🌿 Cuidar de si mesmo é o primeiro passo!",
]


def load_data() -> dict:
    """Carrega os dados do arquivo JSON."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"goal_ml": 2000, "records": {}}


def save_data(data: dict) -> None:
    """Salva os dados no arquivo JSON."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def get_today() -> str:
    """Retorna a data de hoje como string."""
    return str(date.today())


def set_goal(data: dict, goal_ml: int) -> dict:
    """Define a meta diária de consumo de água."""
    if goal_ml <= 0:
        raise ValueError("A meta deve ser maior que zero.")
    data["goal_ml"] = goal_ml
    return data


def add_consumption(data: dict, amount_ml: int) -> dict:
    """Registra consumo de água para hoje."""
    if amount_ml <= 0:
        raise ValueError("O valor deve ser maior que zero.")
    today = get_today()
    if today not in data["records"]:
        data["records"][today] = 0
    data["records"][today] += amount_ml
    return data


def get_progress(data: dict) -> dict:
    """Retorna o progresso do dia atual."""
    today = get_today()
    consumed = data["records"].get(today, 0)
    goal = data["goal_ml"]
    percentage = min((consumed / goal) * 100, 100)
    return {"consumed": consumed, "goal": goal, "percentage": round(percentage, 1)}


def show_menu(temperature: float | None = None) -> None:
    """Exibe o menu principal."""
    print("\n" + "=" * 30)
    print("       💧 HYDRA+ 💧")
    if temperature is not None:
        print(f"   🌡️  Temperatura atual: {temperature}°C")
    print("=" * 30)
    print("1 - Definir meta diária")
    print("2 - Registrar consumo de água")
    print("3 - Ver progresso do dia")
    print("4 - Histórico do dia")
    print("5 - Ver recomendação climática")
    print("6 - Sair")
    print("=" * 30)


def main() -> None:
    """Função principal do programa."""
    import random

    data = load_data()

    print("🌐 Buscando temperatura local...")
    temperature = get_temperature(DEFAULT_LATITUDE, DEFAULT_LONGITUDE)
    if temperature is not None:
        print(f"✅ Temperatura obtida: {temperature}°C")
    else:
        print("⚠️ Não foi possível obter a temperatura. Modo offline ativo.")

    while True:
        show_menu(temperature)
        choice = input("Escolha uma opção: ").strip()

        if choice == "1":
            try:
                goal = int(input("Digite sua meta diária em ml: "))
                data = set_goal(data, goal)
                save_data(data)
                print(f"✅ Meta definida: {goal}ml por dia!")
            except ValueError as e:
                print(f"❌ Erro: {e}")

        elif choice == "2":
            try:
                amount = int(input("Quantos ml você bebeu? "))
                data = add_consumption(data, amount)
                save_data(data)
                progress = get_progress(data)
                print(f"✅ Registrado! Total hoje: {progress['consumed']}ml")
                print(random.choice(MOTIVATIONAL_PHRASES))
                if progress["percentage"] >= 100:
                    print("🎉 Parabéns! Você atingiu sua meta diária!")
            except ValueError as e:
                print(f"❌ Erro: {e}")

        elif choice == "3":
            progress = get_progress(data)
            print("\n📊 Progresso de hoje:")
            print(f"   Consumido: {progress['consumed']}ml")
            print(f"   Meta:      {progress['goal']}ml")
            print(f"   Progresso: {progress['percentage']}%")
            bar = int(progress["percentage"] / 5)
            print(f"   [{'█' * bar}{'░' * (20 - bar)}]")

        elif choice == "4":
            today = get_today()
            consumed = data["records"].get(today, 0)
            print(f"\n📅 Histórico de hoje ({today}):")
            print(f"   Total consumido: {consumed}ml")

        elif choice == "5":
            if temperature is not None:
                rec = get_water_recommendation(temperature)
                print(f"\n{rec['message']}")
                if rec["extra_ml"] > 0:
                    print(f"   💡 Sugestão: beba +{rec['extra_ml']}ml além da sua meta.")
            else:
                print("⚠️ Temperatura indisponível. Verifique sua conexão.")

        elif choice == "6":
            print("👋 Até logo! Lembre-se de se hidratar!")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()