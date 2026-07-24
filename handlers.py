from aiogram import F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from bot import dp
from keyboards import menu
from states import WeatherState
from weather import get_weather, get_forecast


@dp.message(Command("start"))
async def start(message: Message):

    await message.answer(
        "🌤️ Welcome to Weather Bot!\n\n"
        "Version 1.0\n"
        "built by : Nahomx",
        reply_markup=menu
    )


@dp.callback_query()
async def button_handler(callback: CallbackQuery, state: FSMContext):

    if callback.data == "current":

        await callback.message.answer(
            "🌍 Please enter a city name:"
        )

        await state.set_state(
            WeatherState.waiting_for_city
        )


    elif callback.data == "forecast":

        await callback.message.answer(
            "🌍 Please enter a city name for forecast:"
        )

        await state.set_state(
            WeatherState.waiting_for_forecast_city
        )


    elif callback.data == "help":

        await callback.message.answer(
            "ℹ️ How to use Weather Bot:\n\n"
            "🌤️ Current Weather:\n"
            "Get current weather of any city.\n\n"
            "📅 Forecast:\n"
            "Get a 3-day forecast.\n\n"
            "Choose an option and enter a city name."
        )

    await callback.answer()



@dp.message(WeatherState.waiting_for_city)
async def receive_city(message: Message, state: FSMContext):

    city = message.text

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


    except Exception as e:
        await message.answer(
            f"Error: {e}"
        )


    await state.clear()



@dp.message(WeatherState.waiting_for_forecast_city)
async def receive_forecast_city(message: Message, state: FSMContext):

    city = message.text

    try:

        forecast = get_forecast(city)

        if forecast is None:

            await message.answer(
                "❌ City not found. Please check the spelling."
            )

            await state.clear()
            return


        text = f"📅 Forecast for {city}\n\n"

        for day in forecast:

            text += (
                f"📆 {day['date']}\n"
                f"🌡️ Temperature: {day['temperature']}°C\n"
                f"☁️ {day['condition']}\n\n"
            )


        await message.answer(text)


    except Exception as e:

        await message.answer(
            f"Error: {e}"
        )


    await state.clear()