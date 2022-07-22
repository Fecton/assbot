from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, CommandHelp

from loader import dp
from data.long_messages import long_messages
from data.config import USER_RATE_LIMIT
from utils.set_rate_limit import rate_limit


@rate_limit(USER_RATE_LIMIT)
@dp.message_handler(CommandStart())
async def send_start(message: types.Message):
    await message.answer(long_messages["start"])


@rate_limit(USER_RATE_LIMIT)
@dp.message_handler(CommandHelp())
async def send_help(message: types.Message):
    await message.answer(long_messages["help"])


@rate_limit(USER_RATE_LIMIT)
@dp.message_handler(commands="about")
async def send_about(message: types.Message):
    from keyboards.Inline import about_keyboard
    await message.answer(
        long_messages["links"]["text"], 
        disable_web_page_preview=True, 
        reply_markup=about_keyboard,
    )
