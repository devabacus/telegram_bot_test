import logging
import os
import time
from aiogram import Bot, Dispatcher, executor, types
import asyncio
from os_handle import *
from config import *

base_path = "D:\Macys\\19-01-2022\\telegram\\"
teleg_path = pathlib.Path(base_path)
CHANNEL_ID = -1001663830009
def init_bot():
    bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
    dp = Dispatcher(bot)
    messages(dp, bot)
    executor.start_polling(dp, skip_updates=True)    

def messages(dp, bot):
    
    @dp.message_handler(commands=['post'])
    async def send_welcome(message: types.Message):
        
        for img in get_listOfDirs(base_path):
            img_path = get_img_path(teleg_path, img)
            brand = get_brand(teleg_path, img)
            with open(img_path, 'rb') as photo:
                await bot.send_photo(CHANNEL_ID, photo, caption=f"#{brand}\n🌍Для заказа <a href='https://wa.me/79061098570'>👉 Наталья🇺🇲</a>",)
                # await bot.send_photo(CHANNEL_ID, photo, caption=f"#{brand}\n🌍Для заказа https://wa.me/79061098570 👉 Наталья🇺🇲",)
        
    






