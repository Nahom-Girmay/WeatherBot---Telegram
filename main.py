import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from config import BOT_TOKEN
from keyboards import menu
from states import WeatherState
from weather import get_forecast, get_weather


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# --------------------
# Command Handlers
# --------------------

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "🌤️ Welcome to Weather Bot!\n\n"
        "Version 1.0\n"
        "Built by: Nahomx",
        reply_markup=menu
    )


# --------------------
# Callback Handlers
# --------------------

@dp.callback_query()
async def button_handler(callback: CallbackQuery, state: FSMContext):

    if callback.data == "current":

        await callback.message.answer(
            "🌍 Please enter a city name:"
        )

        await state.set_state(WeatherState.waiting_for_city)

        await callback.answer()

    elif callback.data == "forecast":

        await callback.message.answer(
            "🌍 Please enter a city name for forecast:"
        )

        await state.set_state(
            WeatherState.waiting_for_forecast_city
        )

        await callback.answer()

    elif callback.data == "help":

        await callback.message.answer(
            "ℹ️ How to use Weather Bot:\n\n"
            "🌤️ Current Weather\n"
            "Get the current weather of any city.\n\n"
            "📅 Forecast\n"
            "Get a 3-day weather forecast.\n\n"
            "Choose an option, then enter the city name."
        )

        await callback.answer()


# --------------------
# Message Handlers
# --------------------

@dp.message(WeatherState.waiting_for_city)
async def receive_city(message: Message, state: FSMContext):

    city = message.text.strip()

    try:

        weather = get_weather(city)

        if weather is None:
            await message.answer(
                "❌ City not found. Please check the spelling."
            )
            await state.clear()
            return

        text = (
            f"🌤️ Weather in {weather['city']}, {weather['country']}\n\n"
            f"🌡️ Temperature: {weather['temperature']}°C\n"
            f"☁️ Condition: {weather['condition']}\n"
            f"💧 Humidity: {weather['humidity']}%\n"
            f"💨 Wind: {weather['wind']} km/h"
        )

        await message.answer(text)

    except Exception:
        await message.answer(
            "⚠️ Something went wrong. Please try again later."
        )

    await state.clear()


@dp.message(WeatherState.waiting_for_forecast_city)
async def receive_forecast_city(message: Message, state: FSMContext):

    city = message.text.strip()

    try:

        forecast = get_forecast(city)

        if forecast is None:
            await message.answer(
                "❌ City not found. Please check the spelling."
            )
            await state.clear()
            return

        text = f"📅 Forecast for {city.title()}\n\n"

        for day in forecast:
            text += (
                f"📆 {day['date']}\n"
                f"🌡️ Temperature: {day['temperature']}°C\n"
                f"☁️ {day['condition']}\n\n"
            )

        await message.answer(text)

    except Exception:
        await message.answer(
            "⚠️ Something went wrong. Please try again later."
        )

    await state.clear()


# --------------------
# Main
# --------------------

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())