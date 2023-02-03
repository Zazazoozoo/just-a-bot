from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from config import API_TOKEN
from keyboard import kb, kb2, ikb
import os
import random
from random import randrange

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)
HELP_COMMAND = """
<b>/start</b> - запустить бота
<b>/help</b> - список команд
<b>/description</b> - описание бота
<b>/sticker</b> - отправка стикера
<b>/photo</b> - отправка фотографии
<b>/location</b> - отправка геолокации"""

async def on_startup(_):
    print("I have been started")

@dp.message_handler(commands=['start'])
async def get_start(message: types.Message):
    await message.answer(text="Добро пожаловать в наш чат-бот",
                                        reply_markup=kb)
    await message.delete()

@dp.message_handler(commands=['help'])
async def get_help(message: types.Message):
    await message.answer(text=HELP_COMMAND,
                                        parse_mode='HTML',
                                        reply_markup=kb2)
    await message.delete()


@dp.message_handler(commands=['description'])
async def get_descr(message: types.Message):
    await message.answer(text="<em>Это тестовый вариант бота. Сейчас он находится на стадии разработки.</em>",
                                        parse_mode='HTML')
    await message.delete()

@dp.message_handler(commands=['sticker'])
async def get_sticker(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                                            text="Посмотри, какой он милый :3")
    await bot.send_sticker(chat_id=message.from_user.id,
                                        sticker="CAACAgIAAxkBAAEHf0Rj1i6MiddHiz2cz2Z_CdtvaojisQACOwADO2AkFFKC45_2IelfLQQ")
    await message.delete()

@dp.message_handler(commands=['photo'])
async def get_photo(message: types.Message):
    photo=open('photo/' + random.choice(os.listdir('photo')), 'rb')
    await bot.send_photo(message.from_user.id, photo, caption='Нравится эта фотография?', reply_markup=ikb)

@dp.callback_query_handler()
async def vote_callback(callback: types.CallbackQuery):
    if callback.data == 'like':
        await callback.answer('Вам понравилась эта фотография!')
    elif  callback.data == 'dislike':
        await callback.answer('Вам не понравилась эта фотография.')
    elif callback.data == 'random':
        photo = open('photo/' + random.choice(os.listdir('photo')), 'rb')
        await callback.message.answer_photo(photo, caption='А как тебе эта?', reply_markup=ikb)
    elif callback.data == 'menu':
        await callback.message.answer(text=HELP_COMMAND,
                                        parse_mode='HTML',
                                        reply_markup=kb)

@dp.message_handler(commands=['location'])
async def get_loco(message: types.Message):
    await bot.send_location(message.from_user.id,
                                        longitude=randrange(1, 100),
                                        latitude=randrange(1, 100))
    await message.delete()


if __name__=="__main__":
    executor.start_polling(dispatcher=dp,
                            skip_updates=True,
                           on_startup=on_startup)