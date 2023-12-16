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




def register_questionnaire_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_questionnaire_call,
                                       lambda call: call.data == "questionnaire")
    dp.register_callback_query_handler(winter_call,
                                       lambda call: call.data == "winter")
    dp.register_callback_query_handler(summer_call,
                                       lambda call: call.data == "summer")





