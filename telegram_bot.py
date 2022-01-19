from datetime import date
import logging
import os
import time
from aiogram import Bot, Dispatcher, executor, types
import asyncio
from os_handle import *
from config import *
# CHANNEL_ID = -1001309971567 #real shop
def init_bot():
    bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
    dp = Dispatcher(bot)
    messages(dp, bot)
    executor.start_polling(dp, skip_updates=True)    

def messages(dp, bot):
    CHANNEL_ID = -1001663830009 # test shop
    # CHANNEL_ID = -1001309971567 #real shop
    
    teleg_path = get_imgs_path("E:\Macys")
    @dp.message_handler(commands=['post'])
    async def send_welcome(message: types.Message):
        
        for idx, img in enumerate(get_listOfDirs(teleg_path)):
            time.sleep(1)
            img_path = get_img_path(teleg_path, img)
            brand = get_brand(teleg_path, img)
            with open(img_path, 'rb') as photo:
                await bot.send_photo(CHANNEL_ID, photo, caption=f"#{brand}\n🌍Для заказа <a href='https://wa.me/79061098570'>👉 Наталья🇺🇲</a>",)
                # await bot.send_photo(CHANNEL_ID, photo, caption=f"#{brand}\n🌍Для заказа https://wa.me/79061098570 👉 Наталья🇺🇲",)
            if (idx % 10) == 0 and idx != 0:
                time.sleep(30)
        
    

if __name__ == "__main__":
    init_bot() 




