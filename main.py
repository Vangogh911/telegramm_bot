import os
from aiogram import *
from pytube import *


bot = Bot('5729691741:AAEXnsajqlHexhSFY41pWhTLG01b0_D5ISg')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, "Я могу скачать видео с Youtube, если ты скинешь мне ссылку")


@dp.message_handler()
async def text_message(message: types.Message):
    chat_id = message.chat.id
    url = message.text
    yt = YouTube(url)
    if message.text.startswith == 'https://youtu.be/' or 'https://www.youtube.com/':
        await bot.send_message(chat_id, f"Скачиваю видео: {yt.title}")
        await download_yt_video(url, message, bot)


async def download_yt_video(url, message, bot):
    yt = YouTube(url)
    stream = yt.streams.filter(file_extension="mp4")
    stream.get_highest_resolution().download(f'{message.chat.id}', 'Video')
    await bot.send_video(message.chat.id, open(f"{message.chat.id}/Video", 'rb'), caption='Всегда к вашим услугам')
    os.remove(f"{message.chat.id}/Video")


if __name__ == '__main__':
    executor.start_polling(dp)
