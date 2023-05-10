from create_bot import dp
from aiogram import types
from aiogram.dispatcher import Dispatcher

@dp.message_handler()
async def empty(message : types.Message):
    await message.reply(f'Нет такого варианта ответа', parse_mode='html')
    await message.delete()

def register_handlers_other(dp : Dispatcher):
    dp.register_message_handler(empty)


###
##await callback.answer()


