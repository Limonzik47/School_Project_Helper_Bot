from aiogram.utils import executor
from create_bot import dp

from handlers import client, other

client.register_handlers_client(dp)

other.register_handlers_other(dp)

async def on_startup(_):
    print(f"\n''''''''''''''''''''''''''''''\n\nBot went ONLINE!\n\nБот вышел в ОНЛАЙН!\n\n''''''''''''''''''''''''''''''")



executor.start_polling(dp,skip_updates=True, on_startup=on_startup)



