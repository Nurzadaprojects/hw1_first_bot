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




