# 🌤️ Weather Bot Telegram

A Telegram weather bot built with Python and Aiogram.

The bot allows users to check current weather information and 3-day forecasts for any city using WeatherAPI.

## 🚀 Features

- 🌤️ Current weather information
- 📅 3-day weather forecast
- 🌍 Supports cities worldwide
- ❌ Handles invalid city names
- 🔐 Uses environment variables for API keys

## 🛠️ Technologies Used

- Python
- Aiogram
- WeatherAPI
- Requests
- Telegram Bot API

## 📂 Project Structure

```text
WeatherBot/
│
├── main.py
├── weather.py
├── keyboards.py
├── states.py
├── config.py
├── requirements.txt
├── .env             # Not included in GitHub
└── .env.example     # Example environment variables
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Nahom-Girmay/WeatherBot---Telegram.git
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Create environment variables

Create a file named `.env` in the project folder:

```text
BOT_TOKEN=your_telegram_bot_token
WEATHER_API_KEY=your_weather_api_key
```

### 6. Run the bot

```bash
python main.py
```

## 👨‍💻 Author

**Nahom Girmay**

Built with Python, Aiogram, and WeatherAPI.