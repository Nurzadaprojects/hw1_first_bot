import sqlite3

from aiogram import types, Dispatcher
from config import bot
from keyboards import inline_buttons


async def start_questionnaire_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Winter or Summer",
        reply_markup=await inline_buttons.start_questionnaire_keyboard()
    )

async def winter_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="You are right!",

    )
async def summer_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Summer will be soon!",

    )

async def start_color_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="White or Green",
        reply_markup=await inline_buttons.start_color_keyboard()
    )

async def white_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Winter is white!",

    )
async def green_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.from_user.id,
        text="Summer is green!",

    )


def register_questionnaire_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_questionnaire_call,
                                       lambda call: call.data == "questionnaire")
    dp.register_callback_query_handler(winter_call,
                                       lambda call: call.data == "winter")
    dp.register_callback_query_handler(summer_call,
                                       lambda call: call.data == "summer")
    dp.register_callback_query_handler(start_color_call,
                                       lambda call: call.data == "color")
    dp.register_callback_query_handler(white_call,
                                       lambda call: call.data == "white")
    dp.register_callback_query_handler(green_call,
                                       lambda call: call.data == "green")




