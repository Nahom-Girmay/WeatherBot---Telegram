from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🌤️ Current Weather",
                callback_data="current"
            )
        ],
        [
            InlineKeyboardButton(
                text="📅 Forecast",
                callback_data="forecast"
            )
        ],
        [
            InlineKeyboardButton(
                text="ℹ️ Help",
                callback_data="help"
            )
        ]
    ]
)