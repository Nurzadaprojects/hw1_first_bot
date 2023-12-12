from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def start_menu_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Click question",
        callback_data="questionnaire"

    )

    markup.add(questionnaire_button)
    return markup

async def start_questionnaire_keyboard():
    markup = InlineKeyboardMarkup()
    winter_button = InlineKeyboardButton(
        "Winter",
        callback_data="winter"
    )
    summer_button = InlineKeyboardButton(
        "Summer",
        callback_data="summer"

    )

    markup.add(winter_button)
    markup.add(summer_button)
    return markup


async def start_menu_color_keyboard():
    markup = InlineKeyboardMarkup()
    color_button = InlineKeyboardButton(
        "Color",
        callback_data="color"

    )

    markup.add(color_button)
    return markup

async def start_color_keyboard():
    markup = InlineKeyboardMarkup()
    white_button = InlineKeyboardButton(
        "White",
        callback_data="white"
    )
    green_button = InlineKeyboardButton(
        "Green",
        callback_data="green"

    )

    markup.add(white_button)
    markup.add(green_button)
    return markup

