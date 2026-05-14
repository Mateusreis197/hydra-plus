# 💧 Hydra+

> Assistente de hidratação e autocuidado via linha de comando.

![CI](https://github.com/Mateusreis197/hydra-plus/actions/workflows/ci.yml/badge.svg)

🌐 **Deploy:** https://hydra-plus.onrender.com

## 🎯 Problema Real

Milhões de pessoas esquecem de beber água diariamente — especialmente estudantes, trabalhadores e idosos com rotinas intensas. A desidratação causa fadiga, dificuldade de concentração e problemas de saúde a longo prazo.

## 💡 Proposta de Solução

O **Hydra+** é uma aplicação CLI simples que ajuda o usuário a definir e acompanhar sua meta diária de hidratação, registrar o consumo de água e visualizar o progresso em tempo real. Integra com a API Open-Meteo para recomendar hidratação com base na temperatura local.

## 👥 Público-alvo

Estudantes, trabalhadores, idosos e qualquer pessoa que deseja criar o hábito de se hidratar melhor.

## ⚙️ Funcionalidades

- Definir meta diária de consumo de água (em ml)
- Registrar consumo ao longo do dia
- Visualizar progresso com barra gráfica
- Ver histórico do dia
- Frases motivacionais ao registrar consumo
- Recomendação de hidratação baseada na temperatura local (API Open-Meteo)
- Dados persistidos em arquivo JSON

## 🛠️ Tecnologias

- Python 3.10+
- pytest
- ruff
- GitHub Actions
- Open-Meteo API

## 📦 Instalação

```bash
git clone https://github.com/Mateusreis197/hydra-plus.git
cd hydra-plus
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## ▶️ Execução

```bash
python -m src.hydra
```

## 🧪 Testes

```bash
pytest tests/
```

## 🔍 Lint

```bash
ruff check src/
```

## 📌 Versão

1.1.0

## 👤 Autor

Mateus de Andrade Rodrigues Reis

## 🔗 Repositório

https://github.com/Mateusreis197/hydra-plus