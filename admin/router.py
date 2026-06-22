from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from config import ADMIN_IDS
from database import fetchall_query, fetchone_query, execute_query
import keyboards as kb

import re
import asyncio

router = Router()





TEXT = """
⚡️ <b>ОБНОВЛЕНИЕ XIT MUSIC BOT</b> ⚡️

🌐 <b>Мультиязычность</b>
 - Теперь бот поддерживает 2 языка — <b>RU / EN</b>.
 - Меню, тексты и кнопки полностью переведены и синхронизированы.

🚀 <b>Оптимизация и скорость</b>
 - Обновлены внутренние алгоритмы.
 - Бот работает в <b>5 раз быстрее</b>.
 - Отправка треков происходит за миллисекунды.

🎶 <b>Новые функции</b>
 - Приветственное сообщение стало ярче и понятнее.
 - Добавлено <b>30 страниц новинок</b> — актуальные треки месяца.
 - Возможность <b>добавлять</b> или <b>убирать</b> треки из плейлиста.
 - Новая функция <b>«Мой плейлист»</b> — показывает все добавленные песни и позволяет сразу отправить любую из них.
 - Полностью переработанное меню — стильные кнопки, адаптация под два языка, плавные анимации.

💬 <b>Обновлён переход в чат</b>
 - Текст для приглашения в закрытый вайб-чат стал ещё привлекательнее — мотивирует вступать и быть в теме всех новинок!

🔍 <b>Поиск стал умнее</b>
 - Улучшены механизмы поиска по артистам и названиям песен — бот теперь находит нужные треки моментально.

/start
"""




#  TEST FORWARD MESSAGE
@router.message(Command('test'))
async def test(message: Message, bot: Bot):
    if message.from_user.id in ADMIN_IDS:
        await bot.send_message(
            chat_id = message.from_user.id,
            text = TEXT,
            reply_markup=kb.ru_menu)





#  FORWARD MESSAGE
@router.message(Command('forward'))
async def forward(message: Message, bot: Bot):
    if message.from_user.id in ADMIN_IDS:
        data = await fetchall_query('SELECT user_id, language FROM user_data')
        all_users = await fetchone_query('SELECT COUNT(user_id) FROM user_data')
        total = 0
        number = 0

        for users in data:
            user_id, language = users

            try:
                await bot.send_message(
                    chat_id = user_id,
                    text = TEXT,
                    reply_markup=kb.ru_menu)

                total += 1
                number += 1
                print(f'{number}) ✅ [{users[0]}] ({users[1]}): получил сообщение.')

            except Exception as e:
                number += 1
                print(f'{number}) ❌ [{users[0]}] ({users[1]}): заблокировал бота. {e}')

            await asyncio.sleep(0.1)

        else:
            blocked_users = all_users[0] - total
            
            await bot.send_message(
                chat_id=message.from_user.id,
                text=f'<b>👥 Количество пользователей:</b>  {all_users[0]}'
                     f'\n\n<b>✅ Успешно получили:</b> {total}'
                     f'\n<b>❌ Заблокировавшие:</b> {blocked_users}')





@router.message(F.photo)
async def get_photo_id(message: Message):
    if message.chat.id in ADMIN_IDS:
        photo = message.photo[-1]
        file_id = photo.file_id
        await message.answer(f"<code>{file_id}</code>")






