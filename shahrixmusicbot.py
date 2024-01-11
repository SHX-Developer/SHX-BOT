from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext

import asyncio
import sqlite3
import datetime
from time import sleep

from config import token
import reply_markups
import inline_markups



#  VARIABLES OF LIBRARIES

db = sqlite3.connect('ShaHriXMusicBot.db', check_same_thread = False)
sql = db.cursor()

storage = MemoryStorage()

date_time = datetime.datetime.now().date()

bot = Bot(token)
dp = Dispatcher(bot, storage = MemoryStorage())

class SearchState(StatesGroup):
    search = State()

class CountryState(StatesGroup):
    country = State()


#  DATABASE

sql.execute('CREATE TABLE IF NOT EXISTS user_data (id INTEGER, username TEXT, firstname TEXT, lastname TEXT, country TEXT, date DATE)')
db.commit()





#  START

@dp.message_handler(commands = ['start'])
async def start_command(message: types.Message):

    sql.execute('SELECT id FROM user_data WHERE id = ?', (message.chat.id,))
    user_id = sql.fetchone()

    if user_id is None:

        sql.execute('INSERT INTO user_data (id, username, firstname, lastname, country, date) VALUES (?, ?, ?, ?, ?, ?)',
        (message.chat.id, message.from_user.username, message.from_user.first_name, message.from_user.last_name, "-", date_time))
        db.commit()

        await bot.send_message(message.from_user.id, '<b> Пожалуйста, выберите вашу страну: </b>', parse_mode = 'html', reply_markup = reply_markups.countries_reply)
        await CountryState.country.set()

    else:

        await bot.send_message(message.chat.id, "<b> 📍  Главное меню: </b>", parse_mode = 'html', reply_markup = reply_markups.menu_reply)



#  COUNTRY

@dp.message_handler(state = CountryState.country)
async def get_country(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['country'] = message.text

    if message.text == '🇷🇺  Россия' or message.text == '🇺🇦  Украина' or message.text == '🇺🇿  Узбекистан' or message.text == '🇰🇿  Казахстан' or message.text == '🌐  Другая':

        sql.execute('UPDATE user_data SET country = ? WHERE id = ?', (message.text, message.chat.id))
        db.commit()
        await state.finish()

        await bot.send_message(message.from_user.id,    f'<b> {message.from_user.full_name}'
                                                        f'\n\nДобро пожаловать  👋 </b>', parse_mode = 'html', reply_markup = reply_markups.menu_reply)

        await bot.send_message('@jcv0894R', f"New User ⚠" + "\n\n" +
                                            f"User ID:  " + str(message.chat.id) +
                                            f"\nUsername:  @" + str(message.from_user.username) +
                                            f"\nFirst Name:  " + str(message.from_user.first_name) +
                                            f"\nLast Name:  " + str(message.from_user.last_name) +
                                            f"\nCountry:  " + str(message.text))

    else:

        await bot.send_message(message.from_user.id, '<b> Пожалуйста, выберите вашу страну: </b>', parse_mode = 'html', reply_markup = reply_markups.countries_reply)







#  FORWARD TEXT

@dp.message_handler(commands = ['forward'])
async def forward_command(message: types.Message):
    if message.chat.id == 284929331:
        total = 0

        data = sql.execute('SELECT * FROM user_data').fetchall()
        all_users = sql.execute('SELECT COUNT(id) FROM user_data').fetchone()[0]

        for row in data:
            try:
                with open('Course Video (1080).mp4', 'rb') as video:
                    await bot.send_video(
                        chat_id = row[0],
                        video = video,
                        caption =
                        '<b> Хочешь создавать такие ремиксы ? 🎶 </b>'
                        '<i> \n\nПолучи бесплатные пробные уроки 👇 </i>',
                        parse_mode = 'html',
                        reply_markup = inline_markups.chat_inline)

                print(f'{row[0]}:  Получил сообщение  ✅')
                total += 1
            except:
                print(f'{row[0]}:  Заблокировал бота  ❌')
    else:
        blocked_users = all_users - total
        await bot.send_message(
            chat_id = message.chat.id,
            text =
            f'<b>📊  Количество пользователей:</b>  {all_users}'
            f'<b>\n\n✅  Успешно получили:</b> {total}'
            f'<b>\n❌  Заблокировавшие:</b> {blocked_users}',
            parse_mode = 'html',
            reply_markup = None)





#  FORWARD 2

@dp.message_handler(commands = ['forward_2'])
async def forward_command(message: types.Message):
    if message.chat.id == 284929331:
        total = 0

        data = sql.execute('SELECT * FROM user_data').fetchall()
        all_users = sql.execute('SELECT COUNT(id) FROM user_data').fetchone()[0]

        for row in data:
            try:
                await bot.send_message(
                    chat_id = row[0],
                    text =
                    '<b>🎉 Приглашаю всех желающих на свой учебный курс по созданию ремиксов с нуля !</b>'
                    '\n\n<b>📖  Описание курса:</b>'
                    '\nВ этом курсе вы научитесь создавать ремиксы с полного нуля.'
                    '\nОзнакомитесь с программой, структурой ремиксов, добавлением и обработкой звуков, сведением, мастерингом и продвижением ремиксов.'
                    '\n\n<b>📈  Цель курса:</b>'
                    '\nНаучить людей создавать ремиксы в своем стиле, качественно обрабатывать звуки и эффективно продвигать свои работы.'
                    '\n\n<b>🤔  Кому подходит:</b>'
                    '\nКурс предназначен для всех, независимо от их уровня подготовки. Для прохождения курса не требуется никакого музыкального образования или опыта создания музыки.'
                    '\n\n<b>📆 Продолжительность:</b>'
                    '\nКурс состоит из 42 уроков и длится 14 дней, каждый из которых длится около 5 минут.'
                    '\n\n<b>🎥  Тип обучения:</b>'
                    '\nВ курс входят видеоуроки, практические задания, дополнительные ресурсы а также обучение по Discord.'
                    '\n\n<b>🎁  Бонусы при приобретении курса:</b>'
                    '\n1. Мой основной Сэмпл Пак "SHX REMIX SAMPLE PACK".'
                    '\n2. Мой собственный и готовый "TEMPLATE" для ремиксов.'
                    '\n3. Плагины и Пресеты из данного курса.'
                    '\n4. Сэмпл паки разных жанров музыки.'
                    '\n5. Постоянная поддержка и чат со всеми учениками.'
                    '\n6. Методы заработка.'
                    '\n\n<b><i>📲 Желающие, пишем сюда - @ShaHriXMusic</i></b>',
                    parse_mode = 'html',
                    reply_markup = inline_markups.course_inline)

                print(f'{row[0]}:  Получил сообщение  ✅')
                total += 1
            except:
                print(f'{row[0]}:  Заблокировал бота  ❌')
        else:
            blocked_users = all_users - total
            await bot.send_message(
                chat_id = message.chat.id,
                text =
                f'<b>📊  Количество пользователей:</b>  {all_users}'
                f'<b>\n\n✅  Успешно получили:</b> {total}'
                f'<b>\n❌  Заблокировавшие:</b> {blocked_users}',
                parse_mode = 'html',
                reply_markup = None)






#  FORWARD AUDIO

@dp.message_handler(content_types = ['audio'])
async def forward_audio(message: types.Message):
    if message.chat.id == 284929331:
        total = 0

        data = sql.execute('SELECT * FROM user_data').fetchall()
        all_users = sql.execute('SELECT COUNT(id) FROM user_data').fetchone()[0]

        for row in data:
            try:
                await bot.send_audio(chat_id = row[0], audio = message.audio.file_id, caption = '<a href = "http://t.me/ShaHriX_Music"> 🎶 Наш официальный канал с ремиксами </a>', parse_mode = 'html')
                print(f'{row[0]}:  Получил сообщение  ✅')
                total += 1
            except:
                print(f'{row[0]}:  Заблокировал бота  ❌')
        else:
            blocked_users = all_users - total
            await bot.send_message(
                chat_id = message.chat.id,
                text =
                f'<b>📊  Количество пользователей:</b>  {all_users}'
                f'<b>\n\n✅  Успешно получили:</b> {total}'
                f'<b>\n❌  Заблокировавшие:</b> {blocked_users}',
                parse_mode = 'html',
                reply_markup = None)






#  ADMIN

@dp.message_handler(commands = ['admin'])
async def admin_command(message):
    if message.chat.id == 284929331:
        await bot.send_message(message.chat.id, "<b> Выберите действие: </b>", parse_mode = "html", reply_markup = reply_markups.admin_reply)



#  HELP

@dp.message_handler(commands = ['help'])
async def help_command(message: types.Message):
    await bot.send_message(
        chat_id = message.chat.id,
        text =
        "<b>/start  -  Запустить бота"
        "\n/course  -  Крус создание ремиксов"
        "\n/help  -  Список команд"
        "\n/support  -  Обратная связь</b>",
        parse_mode = 'html',
        reply_markup = reply_markups.menu_reply)


#  COURSE

@dp.message_handler(commands = ['course'])
async def help_command(message: types.Message):
    await bot.send_message(
        chat_id = message.chat.id,
        text =
        '<b>🎉 Приглашаю всех желающих на свой учебный курс по созданию ремиксов с нуля !</b>'
        '\n\n<b>📖  Описание курса:</b>'
        '\nВ этом курсе вы научитесь создавать ремиксы с полного нуля.'
        '\nОзнакомитесь с программой, структурой ремиксов, добавлением и обработкой звуков, сведением, мастерингом и продвижением ремиксов.'
        '\n\n<b>📈  Цель курса:</b>'
        '\nНаучить людей создавать ремиксы в своем стиле, качественно обрабатывать звуки и эффективно продвигать свои работы.'
        '\n\n<b>🤔  Кому подходит:</b>'
        '\nКурс предназначен для всех, независимо от их уровня подготовки. Для прохождения курса не требуется никакого музыкального образования или опыта создания музыки.'
        '\n\n<b>📆 Продолжительность:</b>'
        '\nКурс состоит из 42 уроков и длится 14 дней, каждый из которых длится около 5 минут.'
        '\n\n<b>🎥  Тип обучения:</b>'
        '\nВ курс входят видеоуроки, практические задания, дополнительные ресурсы а также обучение по Discord.'
        '\n\n<b>🎁  Бонусы при приобретении курса:</b>'
        '\n1. Мой основной Сэмпл Пак "SHX REMIX SAMPLE PACK".'
        '\n2. Мой собственный и готовый "TEMPLATE" для ремиксов.'
        '\n3. Плагины и Пресеты из данного курса.'
        '\n4. Сэмпл паки разных жанров музыки.'
        '\n5. Постоянная поддержка и чат со всеми учениками.'
        '\n6. Методы заработка.'
        '\n\n<b><i>📲 Желающие, пишем сюда - @ShaHriXMusic</i></b>',
        parse_mode = 'html',
        reply_markup = inline_markups.course_inline)



#  SUPPORT

@dp.message_handler(commands = ['support'])
async def support_command(message: types.Message):
    with open('photo/connect.jpg', 'rb') as photo:
        await bot.send_photo(
        chat_id = message.chat.id,
        photo = photo,
        caption = "<b>"
        "По поводу: <i>"
        "\n\n-  Сотрудничества"
        "\n-  Рекламы"
        "\n-  Заказов"
        "\n-  Предложений"
        "\n-  Других вопросов </i> </b>"
        "\n\n<em><a href='https://t.me/ShaHriXMusic'>Напишите нам в личные сообщения</a> 👇 </em>",
        parse_mode = 'html',
        reply_markup = inline_markups.connect_inline)










#  TEXT

@dp.message_handler()
async def text(message: types.Message):

#  USER ID

    user_id = message.from_user.id

#  TOP

    if message.text == "🚀  Топ":
        await bot.send_message(message.chat.id, "<b> Выберите топ: </b>", parse_mode = "html", reply_markup = reply_markups.top_reply)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "🎧  Топ Ремиксы":
        await bot.send_message(message.chat.id, "<b> Топ 10 ремиксов по статистикам: </b>", parse_mode = "html", reply_markup = inline_markups.top_remixes_inline)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)


    elif message.text == "🎼  Топ Новинки":
        await bot.send_message(message.chat.id, "<b> Топ 10 последних ремиксов: </b>", parse_mode = "html", reply_markup = inline_markups.new_remixes_inline)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)




#  REMIXES

    elif message.text == "🔥  Ремиксы":
        await bot.send_message(message.chat.id, "<b> Выберите язык: </b>", parse_mode='html', reply_markup = reply_markups.remix_language_reply)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "🇷🇺  Русские":
        await bot.send_message(message.chat.id, "<b> Выберите артиста: </b>", parse_mode='html', reply_markup = reply_markups.russian_artists_reply)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "🇺🇸  Английские":
        await bot.send_message(message.chat.id, "<b> Выберите артиста: </b>", parse_mode='html', reply_markup = reply_markups.english_artists_reply)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)



#  OFFICIAL TRACKS

    elif message.text == "🎶  Авторские Треки":
        await bot.send_message(message.chat.id, "<b> Выберите трек: </b>", parse_mode = 'html', reply_markup = inline_markups.official_tracks_inline)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)



#  SEARCH

    elif message.text == "🔍  Поиск":
        await bot.send_message(message.chat.id, "<b> Введите название песни или артиста: </b>", parse_mode = 'html', reply_markup = reply_markups.cancel_search_reply)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)
        await SearchState.search.set()



#  SOCIAL NETWORKS

    elif message.text == "🔔 Социальные Сети":
        with open('photo/social_networks.jpg', 'rb') as photo:
            await bot.send_photo(
                chat_id = message.chat.id,
                photo = photo,
                caption = "<b> Подпишитесь на все наши каналы, чтобы не пропускать <em> <a href='https://t.me/ShaHriX_Music'>новинки </a> </em> 🎧 🎵 </b>",
                parse_mode = 'html',
                reply_markup = inline_markups.social_networks_inline)
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)



#  SUPPORT

    elif message.text == "🆘  Обратная Связь":
        with open('photo/connect.jpg', 'rb') as photo:
            await bot.send_photo(
                chat_id = message.chat.id,
                photo = photo,
                caption = """
                <b>По поводу: <i>
                \n\n-  Сотрудничества
                \n-  Рекламы
                \n-  Заказов
                \n-  Предложений
                \n-  Других вопросов </i> </b>
                \n\n<em><a href='https://t.me/ShaHriXMusic'>Напишите нам в личные сообщения</a> 👇 </em>""",
                parse_mode = 'html',
                reply_markup = inline_markups.connect_inline)
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)



#  COURSE

    elif message.text == "🎶  Курс - создание ремиксов с нуля":
        await bot.send_message(
        chat_id = message.chat.id,
        text =
        '<b>🎉 Приглашаю всех желающих на свой учебный курс по созданию ремиксов с нуля !</b>'
        '\n\n<b>📖  Описание курса:</b>'
        '\nВ этом курсе вы научитесь создавать ремиксы с полного нуля.'
        '\nОзнакомитесь с программой, структурой ремиксов, добавлением и обработкой звуков, сведением, мастерингом и продвижением ремиксов.'
        '\n\n<b>📈  Цель курса:</b>'
        '\nНаучить людей создавать ремиксы в своем стиле, качественно обрабатывать звуки и эффективно продвигать свои работы.'
        '\n\n<b>🤔  Кому подходит:</b>'
        '\nКурс предназначен для всех, независимо от их уровня подготовки. Для прохождения курса не требуется никакого музыкального образования или опыта создания музыки.'
        '\n\n<b>📆 Продолжительность:</b>'
        '\nКурс состоит из 42 уроков и длится 14 дней, каждый из которых длится около 5 минут.'
        '\n\n<b>🎥  Тип обучения:</b>'
        '\nВ курс входят видеоуроки, практические задания, дополнительные ресурсы а также обучение по Discord.'
        '\n\n<b>🎁  Бонусы при приобретении курса:</b>'
        '\n1. Мой основной Сэмпл Пак "SHX REMIX SAMPLE PACK".'
        '\n2. Мой собственный и готовый "TEMPLATE" для ремиксов.'
        '\n3. Плагины и Пресеты из данного курса.'
        '\n4. Сэмпл паки разных жанров музыки.'
        '\n5. Постоянная поддержка и чат со всеми учениками.'
        '\n6. Методы заработка.'
        '\n\n<b><i>📲 Желающие, пишем сюда - @ShaHriXMusic</i></b>',
        parse_mode = 'html',
        reply_markup = inline_markups.course_inline)



#  BACK BUTTONS

    elif message.text == "⬅   Назад":
        await bot.send_message(message.chat.id, "<b> Выберите язык: </b>", parse_mode = 'html', reply_markup = reply_markups.remix_language_reply)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "🏠  Главное меню":
        await bot.send_message(message.chat.id, "<b> 📍  Главное меню: </b>", parse_mode = 'html', reply_markup = reply_markups.menu_reply)

    elif message.text == "⬅   Нaзад":
        await bot.send_message(message.chat.id, "<b> Выберите артиста: </b>", parse_mode = 'html', reply_markup = reply_markups.russian_artists_reply)


    elif message.text == "⬅   Назaд":
        await bot.send_message(message.chat.id, "<b> Выберите артиста: </b>", parse_mode = 'html', reply_markup = reply_markups.english_artists_reply)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)














#  ADMIN PANNEL

#  STATISTICS

    elif message.text == "Статистика":

        if message.chat.id == 284929331:

            sql.execute('SELECT COUNT(id) FROM user_data')
            all_users = sql.fetchone()[0]

            sql.execute('SELECT COUNT(country) FROM user_data WHERE country = ?', ("🇺🇿  Узбекистан",))
            uzbekistan_users = sql.fetchone()[0]

            sql.execute('SELECT COUNT(country) FROM user_data WHERE country = ?', ("🇷🇺  Россия",))
            russia_users = sql.fetchone()[0]

            sql.execute('SELECT COUNT(country) FROM user_data WHERE country = ?', ("🇺🇦  Украина",))
            ukraine_users = sql.fetchone()[0]

            sql.execute('SELECT COUNT(country) FROM user_data WHERE country = ?', ("🇰🇿  Казахстан",))
            kazakhstan_users = sql.fetchone()[0]

            await bot.send_message(message.chat.id,
            f"<b>📊  Общая статистика - SHX BOT  📊</b>"
            f"\n\n👥  Количество пользователей:  <b>{all_users}</b>"
            f"\n\n<b>🌐  <u>Страны аудитории:</u></b>"
            f"\n\n🇷🇺  Россия:  <b>{russia_users} </b>"
            f"\n🇺🇦  Украина:  <b>{ukraine_users} </b>"
            f"\n🇺🇿  Узбекистан:  <b>{uzbekistan_users} </b>"
            f"\n🇰🇿  Казахстан:  <b>{kazakhstan_users} </b>"
            f"\n\n<b>📈  <u>Приходы по месяцам:</u></b>"
            f"\n\n<b>🗓  <u>2022:</u></b>"
            f"\n\nОктябрь:  <b>38</b>"
            f"\nНоябрь:  <b>3</b>"
            f"\nДекабрь:  <b>2</b>"
            f"\n\n<b>🗓  <u>2023:</u></b>"
            f"\n\nЯнварь:  <b>11</b>"
            f"\nФевраль:  <b>23</b>"
            f"\nМарт:  <b>16</b>"
            f"\nАпрель:  <b>17</b>"
            f"\nМай:  <b>41</b>"
            f"\nИюнь:  <b>16</b>"
            f"\nИюль:  <b>50</b>"
            f"\nАвгуст:  <b>23</b>"
            f"\nСентябрь:  <b>20</b>"
            f"\nОктябрь:  <b>32</b>"
            f"\nНоябрь:  <b>8</b> (в процессе)",
            parse_mode="html")

#  USERS COUNT

    elif message.text == "Количество пользователей":
        if message.chat.id == 284929331:

            sql.execute('SELECT COUNT(id) FROM user_data')
            all_users = sql.fetchone()[0]

            await bot.send_message(message.chat.id, f"Количество пользователей:  <b>{all_users}</b>", parse_mode="html")

#  FORWARD TEXT

    elif message.text == "Рассылка текста":
        if message.chat.id == 284929331:
            await bot.send_message(message.chat.id, "<b> Введите текст: </b>", parse_mode="html", reply_markup=reply_markups.admin_cancel_reply)

    elif message.text == "Рассылка трека":
        if message.chat.id == 284929331:
            await bot.send_message(message.chat.id, "<b> Отправьте трек: </b>", parse_mode="html", reply_markup=reply_markups.admin_cancel_reply)

    elif message.text == "Рассылка каналов":
        if message.chat.id == 284929331:
            await bot.send_message(message.chat.id, "<b> Рассылка началась  ✅ </b>", parse_mode="html", reply_markup=reply_markups.menu_reply)

            sql.execute('SELECT * FROM user_data')
            data = sql.fetchall()

            sql.execute('SELECT COUNT(id) FROM user_data')
            all_users = sql.fetchone()[0]

            total = 0

            for users in data:

                try:

                    with open('photo/social_networks.jpg', 'rb') as photo:
                        await bot.send_photo(
                            chat_id = users[0],
                            photo = photo,
                            caption = "<b> Подпишитесь на все наши каналы, чтобы не пропускать <em> <a href='https://t.me/ShaHriX_Music'>новинки </a> </em> 🎧 🎵 </b>",
                            parse_mode = 'html',
                            reply_markup = inline_markups.social_networks_inline)

                        total += 1
                        print(f"[{users[0]}]: получил сообщение  ✅")

                except:

                    print(f"[{users[0]}]: заблокировал бота  ❌")

            else:

                blocked_users = all_users - total

                await bot.send_message(message.chat.id, f"<b>✅  Ваше сообщение успешно отправлено:  {total}  пользователям из:  {all_users - 1}   </b>", parse_mode="html", reply_markup=None)
                await bot.send_message(message.chat.id, f"<b>❌  Заблокировавшие пользователи:  {blocked_users} </b>", parse_mode="html", reply_markup=None)




















#  RUSSIAN REMIXES

#  ALEKS ATAMAN

    elif message.text == "Aleks Ataman":
        await bot.send_message(message.chat.id, "<b> Выберите песню: </b>", parse_mode='html', reply_markup=reply_markups.AleksAtamanRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Диалоги Тет-а-тет":
        with open('Remix/Russian/ALEKS ATAMAN/Диалоги Тет-а-тет (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "ОЙОЙОЙ (ТЫ ГОВОРИЛА)":
        with open('Remix/Russian/ALEKS ATAMAN/ОЙОЙОЙ (ТЫ ГОВОРИЛА) (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  ANNA ASTI

    elif message.text == "Anna Asti":
        await bot.send_message(message.chat.id, "<b> Выберите песню: </b>", parse_mode='html', reply_markup=reply_markups.AnnaAstiRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Царица":
        with open('Remix/Russian/ANNA ASTI/Царица (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  ANDRO

    elif message.text == "Andro":
        await bot.send_message(message.chat.id, "<b> Выберите песню: </b>", parse_mode='html', reply_markup=reply_markups.AndroRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "X.O":
        with open('Remix/Russian/ANDRO/X.O (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Другому":
        with open('Remix/Russian/ANDRO/Другому (ShaHriX ft. Aibek Berkimbaev Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  ANDY PANDA

    elif message.text == "Andy Panda":
        await bot.send_message(message.chat.id, "<b> Выберите песню: </b>", parse_mode='html', reply_markup=reply_markups.AndyPandaRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

#  AVG

    elif message.text == "AVG":
        await bot.send_message(message.chat.id, "<b> Выберите песню: </b>", parse_mode='html', reply_markup=reply_markups.AVGRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Я плачу":
            with open('Remix/Russian/AVG/Я плачу (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Она Кайф":
        with open('Remix/Russian/AVG/Она Кайф (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Платина":
        with open('Remix/Russian/AVG/Платина (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "С Тобой":
        with open('Remix/Russian/AVG/С тобой (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "25 Кадр":
        with open('Remix/Russian/AVG/25 кадр (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  BAKR

    elif message.text == "Bakr":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.BakrRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "За Любовь":
        with open('Remix/Russian/BAKR/За Любовь (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  BRANYA

    elif message.text == "Branya":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.BranyaRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

#  BY INDIA

    elif message.text == "By Индия":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.ByIndiaRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Ещё Хуже":
        with open('Remix/Russian/BY ИНДИЯ/Еще хуже (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "money":
        with open('Remix/Russian/BY ИНДИЯ/Money (ShaHriX & Gloumir Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  CVETOCEK7

    elif message.text == "Cvetocek7":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.Cvetocek7RemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Седая Ночь":
        with open('Remix/Russian/CVETOCEK7/Седая Ночь (Cvetocek7 Cover) (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Все ссоры надоели":
        with open('Remix/Russian/CVETOCEK7/Все ссоры надоели (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  DAREEM

    elif message.text == "Dareem":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.DareemRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Новый Год":
        with open('Remix/Russian/DAREEM/Новый Год (ShaHriX & TheBlvcks & NRG Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  ELMAN

    elif message.text == "Elman":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.ElmanRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Чёрная Любовь":
        with open('Remix/Russian/ELMAN/Чёрная Любовь (ShaHriX Remix) (2).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  ESCAPE

    elif message.text == "Escape":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.EscapeRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

#  FINIK

    elif message.text == "Finik":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.FinikRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

#  GAFUR

    elif message.text == "Gafur":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.GafurRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Атом":
        with open('Remix/Russian/GAFUR/Атом (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "OK":
        with open('Remix/Russian/GAFUR/Ok (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Морозы":
        with open('Remix/Russian/GAFUR/Gafur & Elman - Морозы (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  GIDAYYAT

    elif message.text == "Gidayyat":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.GidayyatRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Лунная":
        with open('Remix/Russian/GIDAYYAT/Лунная Лейла (ShaHriX & Amalee Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  GUMA

    elif message.text == "Guma":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.GumaRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Стеклянная":
        with open('Remix/Russian/GUMA/Стеклянная (ShaHriX & Demirow Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  HENSY

    elif message.text == "Hensy":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.HensyRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Костёр":
        with open('Remix/Russian/HENSY/Hensy & Klava Koka - Костёр (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  ILETRE

    elif message.text == "Iletre":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.IletreRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Седая Ночь":
        with open('Remix/Russian/ILETRE/Седая Ночь (Iletre Cover) (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  IMANBEK

    elif message.text == "Imanbek":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.ImanbekRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

#  JAKOMO

    elif message.text == "Jakomo":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.JakomoRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

#  JAMIK

    elif message.text == "Jamik":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.JamikRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

#  JANAGA

    elif message.text == "Janaga":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.JanagaRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

#  JONY

    elif message.text == "Jony":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.JonyRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Небесные Розы":
        with open('Remix/Russian/JONY/Небесные Розы (Amalee & ShaHrix Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Ты Пари":
        with open('Remix/Russian/JONY/Ты Пари (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Балкон":
        with open('Remix/Russian/JONY/Балкон (Amalee & ShaHrix Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Камнепад":
        with open('Remix/Russian/JONY/Камнепад (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Наверно Ты Меня Не Помнишь":
        with open('Remix/Russian/JONY/Наверное Ты Меня Не Помнишь (ShaHriX & Sergey Meliksetyan Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Уйдёшь":
        with open('Remix/Russian/JONY/Уйдёшь (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  KAMBULAT

    elif message.text == "Kambulat":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.KambulatRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Письма":
        with open('Remix/Russian/KAMBULAT/Письма (ShaHriX & Rene Various Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Душа Устала":
        with open('Remix/Russian/KAMBULAT/Душа Устала (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Выпей Меня":
        with open('Remix/Russian/KAMBULAT/Выпей Меня (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Звездопад":
        with open('Remix/Russian/KAMBULAT/Звездопад (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  KONFUZ

    elif message.text == "Konfuz":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.KonfuzRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Ратата":
        with open('Remix/Russian/KONFUZ/РаТаТа (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Война":
        with open('Remix/Russian/KONFUZ/Война (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Выше":
        with open('Remix/Russian/KONFUZ/Выше (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Не Смотри":
        with open('Remix/Russian/KONFUZ/Не Смотри (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Касаюсь":
        with open('Remix/Russian/KONFUZ/Касаюсь (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Очень Очень":
        with open('Remix/Russian/KONFUZ/Очень Очень (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Пропал Интерес":
        with open('Remix/Russian/KONFUZ/Пропал Интерес (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Сказка":
        with open('Remix/Russian/KONFUZ/Сказка (ShaHriX & MELIX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Рокстар":
        with open('Remix/Russian/KONFUZ/Рокстар (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Аккорды":
        with open('Remix/Russian/KONFUZ/Аккорды (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  LIMBA

    elif message.text == "Limba":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.LimbaRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Секрет":
        with open('Remix/Russian/LIMBA/Секрет (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  LXE

    elif message.text == "Lxe":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.LxeRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Девочка Наркотик":
        with open('Remix/Russian/LXE/Девочка Наркотик (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  MACAN

    elif message.text == "Macan":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.MacanRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Поспешили":
            with open('Remix/Russian/MACAN/Поспешили (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Asphalt 8":
        with open('Remix/Russian/MACAN/ASPHALT 8 (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "IVL":
        with open('Remix/Russian/MACAN/IVL (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Пополам":
        with open('Remix/Russian/MACAN/Пополам (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  MAKSIM

    elif message.text == "Maksim":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.MakSimRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

#  MARKUL

    elif message.text == "Markul":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.MarkulRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Стрелы":
        with open('Remix/Russian/MARKUL/Стрелы (ShaHriX Remix) (2).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  MIYAGI

    elif message.text == "Miyagi":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.MiyagiRemixesButton)

    elif message.text == "All The Time":
        with open('Remix/Russian/MIYAGI/All The Time (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Патрон":
        with open('Remix/Russian/MIYAGI/Патрон (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Санавабич":
        with open('Remix/Russian/MIYAGI/Санавабич (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Там Ревели Горы":
        with open('Remix/Russian/MIYAGI/Там Ревели Горы (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Angel":
        with open('Remix/Russian/MIYAGI/Angel (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Marmelade":
        with open('Remix/Russian/MIYAGI/Marmelade (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  MONA

    elif message.text == "Mona":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.MonaRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Зари":
        with open("Remix/Russian/ANDRO/Зари (ShaHriX Remix).mp3", "rb") as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  MONEYKEN

    elif message.text == "Moneyken":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.MoneykenRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Она Не Любит Вино":
        with open('Remix/Russian/MONEYKEN/Она Не Любит Вино Remix.mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  MORGENSHTERN

    elif message.text == "Morgenshtern":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.MorgenshternRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Cristal Моёт":
        with open('Remix/Russian/MORGENSHTERN/Cristal Моёт (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Family":
        with open('Remix/Russian/MORGENSHTERN/Morgenshtern & Yung Trappa - Family (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Leck":
        with open('Remix/Russian/MORGENSHTERN/Leck (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Show":
        with open('Remix/Russian/MORGENSHTERN/SHOW (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  NEKI

    elif message.text == "Neki":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.NekiRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Огни":
        with open('Remix/Russian/NEKI/Огни (ShaHriX & Fridrikh Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  NLO

    elif message.text == "Nlo":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.NloRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Не Грусти":
        with open('Remix/Russian/NLO/Не Грусти (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  PUSSYKILLER

    elif message.text == "Pussykiller":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.PussyKillerRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Одним выстрелом":
            with open('Remix/Russian/PUSSYKILLER/Одним выстрелом (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Франция":
        with open('Remix/Russian/PUSSYKILLER/Франция (ShaHriX & JustBlack$ Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  RAIKAHO

    elif message.text == "Raikaho":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.RaikahoRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

#  RAKHIM

    elif message.text == "Rakhim":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.RakhimRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Синий Lamborghini":
        with open('Remix/Russian/RAKHIM/Синий Lamborghini (ShaHriX & Camron Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  RAMIL

    elif message.text == "Ramil":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.RamilRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Сияй":
        with open('Remix/Russian/RAMIL/Сияй (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Аромат":
        with open('Remix/Russian/RAMIL/Аромат (ShaHriX Remix.mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Сон":
        with open('Remix/Russian/RAMIL/Сон (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Дождь":
        with open('Remix/Russian/RAMIL/Дождь (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Маяк":
        with open('Remix/Russian/RAMIL/Маяк (ShaHriX & FriDrix Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Просто Лети":
        with open('Remix/Russian/RAMIL/Просто Лети (ShaHriX Remix) (2).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Увидимся":
        with open('Remix/Russian/RAMIL/Увидимся (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Mp3":
        with open('Remix/Russian/RAMIL/Mp3 (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  RAUF FAIK

    elif message.text == "Rauf & Faik":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.RaufFaikRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Я Люблю Тебя Давно":
        with open('Remix/Russian/RAUF & FAIK/Я Люблю Тебя Давно (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Деньги и Счастье":
        with open('Remix/Russian/RAUF & FAIK/Деньги и Счастье (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "5 Минут":
        with open('Remix/Russian/RAUF & FAIK/5 Минут (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  REAL GIRL

    elif message.text == "Real Girl":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.RealGirlRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Всё Для Тебя (Cover)":
        with open('Remix/Russian/REAL GIRL/Всё для тебя (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Все Решено":
        with open('Remix/Russian/REAL GIRL/Все решено (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Девушка Мечты (Short Version)":
        with open('Remix/Russian/REAL GIRL/Девушка Мечты (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Вино и Сигареты":
        with open('Remix/Russian/REAL GIRL/Вино и Сигареты (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Сектор Газа (Cover)":
        with open('Remix/Russian/REAL GIRL/Сектор Газа (Real Girl Cover) (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Девушка Мечты (Trap Version)":
        with open('Remix/Russian/REAL GIRL/Девушка_Мечты_Real_Girl_Cover_ShaHriX_Trap_Remix.mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Послала (Cover)":
        with open('Remix/Russian/REAL GIRL/Послала как и обещала (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Девушка Мечты (Full Version)":
        with open('Remix/Russian/REAL GIRL/Девушка_Мечты_ShaHriX_Remix_Real_Girl_Cover_Full_Version.mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Девушка Мечты (Original Cover)":
        with open('Remix/Russian/REAL GIRL/Девушка_Мечты_ShaHriX_Remix_Real_Girl_Original_Cover.mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Отпускаю (Cover)":
        with open('Remix/Russian/REAL GIRL/Отпускаю (Real Girl Cover) (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  SCIRENA

    elif message.text == "Scirena":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.ScirenaRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

#  SLAVA MARLOW

    elif message.text == "Slava Marlow":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.SlavaMarlowRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Ты Горишь Как Огонь":
        with open('Remix/Russian/SLAVA MARLOW/Ты Горишь Как Огонь (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Кому Это Надо":
        with open('Remix/Russian/SLAVA MARLOW/Кому Это Надо (ShaHriX & Muzaffaroff Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  SLAVIK POGOSOV

    elif message.text == "Slavik Pogosov":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.SlavikPogosovRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Монро":
        with open('Remix/Russian/SLAVIK POGOSOV/Монро (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  HAMMALI NAVAI

    elif message.text == "Hammali & Navai":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.HammaliNavaiRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Не Люби Меня":
        with open('Remix/Russian/XAMMALI & NAVAI/Не Люби Меня HammAli & Navai (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Где Ты Была":
        with open('Remix/Russian/XAMMALI & NAVAI/Где Ты была (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "А Если Это Любовь":
        with open('Remix/Russian/XAMMALI & NAVAI/Hammali_&_Navai_А_Если_Это_Любовь_Amalee_&_Shahrix_Remix.mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Девочка Танцуй":
        with open('Remix/Russian/XAMMALI & NAVAI/Девочка Танцуй (ShaHriX & Saurbaev Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Птичка":
        with open('Remix/Russian/XAMMALI & NAVAI/Птичка (ShaHriX & Orkenoff Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  XASSA

    elif message.text == "Xassa":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.XassaRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Дикари":
        with open('Remix/Russian/XASSA/Дикари (ShaHriX & Demirow Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  XCHO

    elif message.text == "Xcho":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.XchoRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Мысли":
        with open('Remix/Russian/XCHO/Мысли (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Музыка В Ночи":
        with open('Remix/Russian/XCHO/Музыка в Ночи (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Поэт":
        with open('Remix/Russian/XCHO/Поэт (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Memories":
        with open('Remix/Russian/XCHO/MACAN & Xcho - Memories (Amalee & ShaHrix Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "All Right":
        with open('Remix/Russian/XCHO/All Right (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  АМУРА

    elif message.text == "Амура":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.AmuraRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Как Дела":
        with open('Remix/Russian/AMURA/Как Дела (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Минимум":
        with open('Remix/Russian/AMURA/Минимум (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Спрячься":
        with open('Remix/Russian/AMURA/Спрячься (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Хотелось Бросить":
        with open('Remix/Russian/AMURA/Хотелось бросить (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)



#  АНЕТ САЙ

    elif message.text == "Анет Сай":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.AnetSayRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Слёзы":
        with open('Remix/Russian/АНЕТ САЙ/Слёзы (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  АРКАЙДА

    elif message.text == "Аркайда":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.ArkaydaRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Дай Дыма Брат":
        with open('Remix/Russian/АРКАЙДА/Дай Дыма Брат (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  ДЖАРАХОВ

    elif message.text == "Джарахов":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.DjarahovRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Я в моменте":
        with open('Remix/Russian/ДЖАРАХОВ/Я в моменте (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  ЕГОР КРИД

    elif message.text == "Егор Крид":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.EgorKreedRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "(Не) Идеальна":
        with open('Remix/Russian/ЕГОР КРИД/(Не)Идеальна (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Отпускаю":
        with open('Remix/Russian/ЕГОР КРИД/Отпускаю (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "We Gotta Get Love":
        with open('Remix/Russian/ЕГОР КРИД/We Gotta Get Love (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  КАНГИ

    elif message.text == "Канги":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.KangiRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Голова":
        with open('Remix/Russian/КАНГИ/Голова (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Возьми Сердце Моё":
        with open('Remix/Russian/КАНГИ/Возьми Сердце Моё (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Жить Не Запретишь":
        with open('Remix/Russian/КАНГИ/Жить Не Запретишь (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Эйя":
        with open('Remix/Russian/КАНГИ/Эйя (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  КАСПИЙСКИЙ ГРУЗ

    elif message.text == "Каспийский Груз":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.KaspiyskiyGruzRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "На белом":
        with open('Remix/Russian/КАСПИЙСКИЙ ГРУЗ/На белом (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  КЛАВА КОКА

    elif message.text == "Клава Кока":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.KlavaKokaRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

#  КОСТА ЛАКОСТА

    elif message.text == "Коста Лакоста":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.KostaLakostaRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

#  КРИСПИ

    elif message.text == "Криспи":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.KrispiRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Целуй":
        with open('Remix/Russian/КРИСПИ/Целуй (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  КУЧЕР

    elif message.text == "Кучер":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.KucherRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "По Щекам Слёзы":
        with open('Remix/Russian/КУЧЕР/По Щекам Слёзы (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Се Ля Ви":
        with open('Remix/Russian/КУЧЕР/Се Ля Ви (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  РАЙДА

    elif message.text == "Райда":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.RaydaRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

#  СКРИПТОНИТ

    elif message.text == "Скриптонит":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.SkriptonitRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Чистый":
        with open('Remix/Russian/СКРИПТОНИТ/Чистый (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Baby Mama":
        with open('Remix/Russian/СКРИПТОНИТ/Baby Mama (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  СУЛТАН ЛАГУЧЕВ

    elif message.text == "Султан Лагучев":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.SultanLaguchevRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Горький Вкус":
        with open('Remix/Russian/СУЛТАН ЛАГУЧЕВ/Горький Вкус (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Не Души":
        with open('Remix/Russian/СУЛТАН ЛАГУЧЕВ/Не Души (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  ЭЛДЖЕЙ

    elif message.text == "Элджей":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.EldjeyRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Бронежилет":
        with open('Remix/Russian/ЭЛДЖЕЙ/Бронежилет (ShaHriX Remix) (2).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Harakiri":
        with open('Remix/Russian/ЭЛДЖЕЙ/Harakiri (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)
#  ЭНШПИЛЬ

    elif message.text == "Эндшпиль":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.EndshpilRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

#  10AGE

    elif message.text == "10Age":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.IOAgeRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Нету Интереса":
        with open('Remix/Russian/10AGE/Нету Интереса (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Пушка":
        with open('Remix/Russian/10AGE/Пушка (ShaHriX & Olzhas Serikov Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Паровозик":
        with open('Remix/Russian/10AGE/Паровозик (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)










#  ENGLISH REMIXES

#  BLACKBEAR

    elif message.text == "Blackbear":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.BlackbearRemixesButton)
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "IDFC":
        with open('Remix/English/BLACKBEAR/blackbear - idfc [aibek berkimbaev & shahrix remix].mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  CASSETTE

    elif message.text == "Cassette":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.CassetteRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "My Way":
        with open('Remix/English/CASSETTE/My Way (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  DAFT PUNK

    elif message.text == "Daft Punk":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.DaftPunkRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)


    elif message.text == "Get Lucky":
        with open('Remix/English/DAFT PUNK/Get Lucky (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  DUA LIPA

    elif message.text == "Dua Lipa":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.SeanPaulRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "No Lie":
        with open('Remix/English/DUA LIPA/No Lie (ShaHriX & Camron Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  FOUSHEE

    elif message.text == "Foushee":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.FousheeRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Deep End":
        with open('Remix/English/FOUSHEE/Deep End (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  G-EASY

    elif message.text == "G-Easy":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.GEasyRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Him & I":
        with open('Remix/English/G-EASY/Him & I (ShaHriX & Melix Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)
#  GHOSTLY KISSES

    elif message.text == "Ghostly Kisses":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.GhostlyKissesRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Empty Note":
        with open('Remix/English/GHOSTLY KISSES/Ghostly_Kisses_Empty_Note_Aibek_Berkimbaev_&_ShaHriX_remix.mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  HALSEY

    elif message.text == "Halsey":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.HalseyRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

#  IAN STORM

    elif message.text == "Ian Storm":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.IanStormRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Run Away":
        with open('Remix/English/IAN STORM/Run Away (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  INNA

    elif message.text == "Inna":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.InnaRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Lonely":
        with open('Remix/English/INNA/Lonely (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif message.text == "Solo":
        with open('Remix/English/INNA/Solo (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)
#  JVLA

    elif message.text == "Jvla":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.JvlaRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Such A Whore":
        with open('Remix/English/JVLA/Such A Whole Remix.mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  KENYA GRACE

    elif message.text == "Kenya Grace":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.KenyaGraceRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Strangers":
        with open('Remix/English/KENYA GRACE/Strangers (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  KINA

    elif message.text == "Kina":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.KinaRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Get You The Moon":
        with open('Remix/English/KINA/Kina - Get You The Moon (ShaHriX & Amalee Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  LADY GAGA

    elif message.text == "Lady Gaga":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.LadyGagaRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Bloody Mary":
        with open('Remix/English/LADY GAGA/Bloody Mary (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  LISA

    elif message.text == "Lisa":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.LisaRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Money":
        with open('Remix/English/LISA/Money (ShaHriX & TheBlvcks  Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  MINELLI

    elif message.text == "Minelli":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.MinelliRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Rampampam":
        with open('Remix/English/MINELLI/Rampampam (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  MISHLAWI

    elif message.text == "Mishlawi":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.MishlawiRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "All Night":
        with open('Remix/English/MISHLAWI/All Night (ShaHriX & JustBlack$ Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  NBSPLV

    elif message.text == "Nbsplv":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.NbsplvRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "The Lost Soul Down":
        with open('Remix/English/NBSPLV/The Lost Soul Down (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  OLIVER TREE

    elif message.text == "Oliver Tree":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.OliverTreeRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Cowboys Don't Cry":
        with open('Remix/English/OLIVER TREE/Cowboys Dont Cry (ShaHriX & UNPY Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  PHARELL WILLIAMS

    elif message.text == "Pharell Williams":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.PharellWilliamsRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

#  SEAN PAUL

    elif message.text == "Sean Paul":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.SeanPaulRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Go Down Deh":
        with open('Remix/English/SEAN PAUL/Go Down Deh (ShaHriX & TheBlvcks Remix) (2).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  SELENA GOMEZ

    elif message.text == "Selena Gomez":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.TrevorDanielRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Past Life":
        with open('Remix/English/SELENA GOMEZ/Trevor Daniel & Selena Gomez - Past Life (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  SPICE

    elif message.text == "Spice":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.SpiceRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

#  SQUID GAME

    elif message.text == "Squid Game":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.SquidGameRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Pink Soldiers":
        with open('Remix/English/SQUID GAME/Pink Soldiers (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  SZA

    elif message.text == "SZA":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.SZARemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Big Boy":
        with open('Remix/English/SZA/Big Boy (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  TIESTO

    elif message.text == "Tiesto":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.TiestoRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "The Business":
        with open('Remix/English/TIESTO/The Business (ShaHriX Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

#  TREVOR DANIEL

    elif message.text == "Trevor Daniel":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.TrevorDanielRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

#  XXXTENTACION

    elif message.text == "Xxxtentacion":
        await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.XXXTentacionRemixesButton)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id)
        await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)

    elif message.text == "Bad":
        with open('Remix/English/XXXTENTACION/Bad (ShaHriX & JustBlack$ Remix).mp3', 'rb') as remix:
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)




















#  SEARCH

@dp.message_handler(state = SearchState.search)
async def search_audio(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['search'] = message.text
        message.text = str.title(message.text)
        user_id = message.from_user.id

    #  CANCEL

        if message.text == "Отменить":
            await bot.send_message(message.chat.id, '<b> Поиск отменён. </b>', parse_mode = 'html', reply_markup = reply_markups.menu_reply)
            await bot.delete_message(chat_id = message.chat.id, message_id = message.message_id)
            await bot.delete_message(chat_id = message.chat.id, message_id = message.message_id - 1)
            await state.finish()

    #  ALEKS ATAMAN

        elif message.text == "Aleks Ataman":
            await bot.send_message(message.chat.id, "<b> Выберите песню: </b>", parse_mode='html', reply_markup=reply_markups.AleksAtamanRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Диалоги Тет-а-тет":
            with open('Remix/Russian/ALEKS ATAMAN/Диалоги Тет-а-тет (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "ОЙОЙОЙ (ТЫ ГОВОРИЛА)":
            with open('Remix/Russian/ALEKS ATAMAN/ОЙОЙОЙ (ТЫ ГОВОРИЛА) (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  ANNA ASTI

        elif message.text == "Anna Asti":
            await bot.send_message(message.chat.id, "<b> Выберите песню: </b>", parse_mode='html', reply_markup=reply_markups.AnnaAstiRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Царица":
            with open('Remix/Russian/ANNA ASTI/Царица (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  ANDRO

        elif message.text == "Andro":
            await bot.send_message(message.chat.id, "<b> Выберите песню: </b>", parse_mode='html', reply_markup=reply_markups.AndroRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "X.O":
            with open('Remix/Russian/ANDRO/X.O (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Другому":
            with open('Remix/Russian/ANDRO/Другому (ShaHriX ft. Aibek Berkimbaev Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  ANDY PANDA

        elif message.text == "Andy Panda":
            await bot.send_message(message.chat.id, "<b> Выберите песню: </b>", parse_mode='html', reply_markup=reply_markups.AndyPandaRemixesButton)
            await delete_message_2(message)
            await state.finish()

    #  AVG

        elif message.text == "AVG":
            await bot.send_message(message.chat.id, "<b> Выберите песню: </b>", parse_mode='html', reply_markup=reply_markups.AVGRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Я плачу":
            with open('Remix/Russian/AVG/Я плачу (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Она Кайф":
            with open('Remix/Russian/AVG/Она Кайф (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Платина":
            with open('Remix/Russian/AVG/Платина (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "С Тобой":
            with open('Remix/Russian/AVG/С тобой (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "25 Кадр":
            with open('Remix/Russian/AVG/25 кадр (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  BAKR

        elif message.text == "Bakr":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.BakrRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "За Любовь":
            with open('Remix/Russian/BAKR/За Любовь (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  BRANYA

        elif message.text == "Branya":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.BranyaRemixesButton)
            await delete_message_2(message)
            await state.finish()

    #  BY INDIA

        elif message.text == "By Индия":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.ByIndiaRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Ещё Хуже":
            with open('Remix/Russian/BY ИНДИЯ/Еще хуже (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "money":
            with open('Remix/Russian/BY ИНДИЯ/Money (ShaHriX & Gloumir Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  CVETOCEK7

        elif message.text == "Cvetocek7":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.Cvetocek7RemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Седая Ночь":
            with open('Remix/Russian/CVETOCEK7/Седая Ночь (Cvetocek7 Cover) (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Все ссоры надоели":
            with open('Remix/Russian/CVETOCEK7/Все ссоры надоели (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  DAREEM

        elif message.text == "Dareem":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.DareemRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Новый Год":
            with open('Remix/Russian/DAREEM/Новый Год (ShaHriX & TheBlvcks & NRG Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  ELMAN

        elif message.text == "Elman":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.ElmanRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Чёрная Любовь":
            with open('Remix/Russian/ELMAN/Чёрная Любовь (ShaHriX Remix) (2).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  ESCAPE

        elif message.text == "Escape":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.EscapeRemixesButton)
            await delete_message_2(message)
            await state.finish()

    #  FINIK

        elif message.text == "Finik":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.FinikRemixesButton)
            await delete_message_2(message)
            await state.finish()

    #  GAFUR

        elif message.text == "Gafur":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.GafurRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Атом":
            with open('Remix/Russian/GAFUR/Атом (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "OK":
            with open('Remix/Russian/GAFUR/Ok (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Морозы":
            with open('Remix/Russian/GAFUR/Gafur & Elman - Морозы (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  GIDAYYAT

        elif message.text == "Gidayyat":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.GidayyatRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Лунная":
            with open('Remix/Russian/GIDAYYAT/Лунная Лейла (ShaHriX & Amalee Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  GUMA

        elif message.text == "Guma":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.GumaRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Стеклянная":
            with open('Remix/Russian/GUMA/Стеклянная (ShaHriX & Demirow Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  HENSY

        elif message.text == "Hensy":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.HensyRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Костёр":
            with open('Remix/Russian/HENSY/Hensy & Klava Koka - Костёр (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  ILETRE

        elif message.text == "Iletre":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.IletreRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Седая Ночь":
            with open('Remix/Russian/ILETRE/Седая Ночь (Iletre Cover) (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  IMANBEK

        elif message.text == "Imanbek":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.ImanbekRemixesButton)
            await delete_message_2(message)
            await state.finish()

    #  JAKOMO

        elif message.text == "Jakomo":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.JakomoRemixesButton)
            await delete_message_2(message)
            await state.finish()

    #  JAMIK

        elif message.text == "Jamik":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.JamikRemixesButton)
            await delete_message_2(message)
            await state.finish()

    #  JANAGA

        elif message.text == "Janaga":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.JanagaRemixesButton)
            await delete_message_2(message)
            await state.finish()

    #  JONY

        elif message.text == "Jony":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.JonyRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Небесные Розы":
            with open('Remix/Russian/JONY/Небесные Розы (Amalee & ShaHrix Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Ты Пари":
            with open('Remix/Russian/JONY/Ты Пари (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Балкон":
            with open('Remix/Russian/JONY/Балкон (Amalee & ShaHrix Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Камнепад":
            with open('Remix/Russian/JONY/Камнепад (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Наверно Ты Меня Не Помнишь":
            with open('Remix/Russian/JONY/Наверное Ты Меня Не Помнишь (ShaHriX & Sergey Meliksetyan Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Уйдёшь":
            with open('Remix/Russian/JONY/Уйдёшь (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  KAMBULAT

        elif message.text == "Kambulat":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.KambulatRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Письма":
            with open('Remix/Russian/KAMBULAT/Письма (ShaHriX & Rene Various Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Душа Устала":
            with open('Remix/Russian/KAMBULAT/Душа Устала (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Выпей Меня":
            with open('Remix/Russian/KAMBULAT/Выпей Меня (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Звездопад":
            with open('Remix/Russian/KAMBULAT/Звездопад (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  KONFUZ

        elif message.text == "Konfuz":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.KonfuzRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Ратата":
            with open('Remix/Russian/KONFUZ/РаТаТа (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Война":
            with open('Remix/Russian/KONFUZ/Война (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Выше":
            with open('Remix/Russian/KONFUZ/Выше (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Не Смотри":
            with open('Remix/Russian/KONFUZ/Не Смотри (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Касаюсь":
            with open('Remix/Russian/KONFUZ/Касаюсь (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Очень Очень":
            with open('Remix/Russian/KONFUZ/Очень Очень (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Пропал Интерес":
            with open('Remix/Russian/KONFUZ/Пропал Интерес (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Сказка":
            with open('Remix/Russian/KONFUZ/Сказка (ShaHriX & MELIX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Рокстар":
            with open('Remix/Russian/KONFUZ/Рокстар (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Аккорды":
            with open('Remix/Russian/KONFUZ/Аккорды (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  LIMBA

        elif message.text == "Limba":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.LimbaRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Секрет":
            with open('Remix/Russian/LIMBA/Секрет (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  LXE

        elif message.text == "Lxe":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.LxeRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Девочка Наркотик":
            with open('Remix/Russian/LXE/Девочка Наркотик (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  MACAN

        elif message.text == "Macan":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.MacanRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Поспешили":
            with open('Remix/Russian/MACAN/Поспешили (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Asphalt 8":
            with open('Remix/Russian/MACAN/ASPHALT 8 (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "IVL":
            with open('Remix/Russian/MACAN/IVL (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Пополам":
            with open('Remix/Russian/MACAN/Пополам (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  MAKSIM

        elif message.text == "Maksim":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.MakSimRemixesButton)
            await delete_message_2(message)
            await state.finish()

    #  MARKUL

        elif message.text == "Markul":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.MarkulRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Стрелы":
            with open('Remix/Russian/MARKUL/Стрелы (ShaHriX Remix) (2).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  MIYAGI

        elif message.text == "Miyagi":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.MiyagiRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "All The Time":
            with open('Remix/Russian/MIYAGI/All The Time (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Патрон":
            with open('Remix/Russian/MIYAGI/Патрон (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Санавабич":
            with open('Remix/Russian/MIYAGI/Санавабич (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Там Ревели Горы":
            with open('Remix/Russian/MIYAGI/Там Ревели Горы (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Angel":
            with open('Remix/Russian/MIYAGI/Angel (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Marmelade":
            with open('Remix/Russian/MIYAGI/Marmelade (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  MONA

        elif message.text == "Mona":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.MonaRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Зари":
            with open("Remix/Russian/ANDRO/Зари (ShaHriX Remix).mp3", "rb") as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  MONEYKEN

        elif message.text == "Moneyken":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.MoneykenRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Она Не Любит Вино":
            with open('Remix/Russian/MONEYKEN/Она Не Любит Вино Remix.mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  MORGENSHTERN

        elif message.text == "Morgenshtern":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.MorgenshternRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Cristal Моёт":
            with open('Remix/Russian/MORGENSHTERN/Cristal Моёт (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Family":
            with open('Remix/Russian/MORGENSHTERN/Morgenshtern & Yung Trappa - Family (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Leck":
            with open('Remix/Russian/MORGENSHTERN/Leck (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Show":
            with open('Remix/Russian/MORGENSHTERN/SHOW (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  NEKI

        elif message.text == "Neki":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.NekiRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Огни":
            with open('Remix/Russian/NEKI/Огни (ShaHriX & Fridrikh Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  NLO

        elif message.text == "Nlo":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.NloRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Не Грусти":
            with open('Remix/Russian/NLO/Не Грусти (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  PUSSYKILLER

        elif message.text == "Pussykiller":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.PussyKillerRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Одним выстрелом":
            with open('Remix/Russian/PUSSYKILLER/Одним выстрелом (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Франция":
            with open('Remix/Russian/PUSSYKILLER/Франция (ShaHriX & JustBlack$ Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  RAIKAHO

        elif message.text == "Raikaho":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.RaikahoRemixesButton)
            await delete_message_2(message)
            await state.finish()

    #  RAKHIM

        elif message.text == "Rakhim":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.RakhimRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Синий Lamborghini":
            with open('Remix/Russian/RAKHIM/Синий Lamborghini (ShaHriX & Camron Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  RAMIL

        elif message.text == "Ramil":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.RamilRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Сияй":
            with open('Remix/Russian/RAMIL/Сияй (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Аромат":
            with open('Remix/Russian/RAMIL/Аромат (ShaHriX Remix.mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Сон":
            with open('Remix/Russian/RAMIL/Сон (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Дождь":
            with open('Remix/Russian/RAMIL/Дождь (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Маяк":
            with open('Remix/Russian/RAMIL/Маяк (ShaHriX & FriDrix Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Просто Лети":
            with open('Remix/Russian/RAMIL/Просто Лети (ShaHriX Remix) (2).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Увидимся":
            with open('Remix/Russian/RAMIL/Увидимся (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Mp3":
            with open('Remix/Russian/RAMIL/Mp3 (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  RAUF FAIK

        elif message.text == "Rauf & Faik":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.RaufFaikRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Я Люблю Тебя Давно":
            with open('Remix/Russian/RAUF & FAIK/Я Люблю Тебя Давно (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Деньги и Счастье":
            with open('Remix/Russian/RAUF & FAIK/Деньги и Счастье (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "5 Минут":
            with open('Remix/Russian/RAUF & FAIK/5 Минут (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  REAL GIRL

        elif message.text == "Real Girl":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.RealGirlRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Девушка Мечты (Short Version)":
            with open('Remix/Russian/REAL GIRL/Девушка Мечты (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Все Решено":
            with open('Remix/Russian/REAL GIRL/Все решено (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Всё Для Тебя (Cover)":
            with open('Remix/Russian/REAL GIRL/Всё для тебя (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Вино и Сигареты":
            with open('Remix/Russian/REAL GIRL/Вино и Сигареты (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Сектор Газа (Cover)":
            with open('Remix/Russian/REAL GIRL/Сектор Газа (Real Girl Cover) (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Девушка Мечты (Trap Version)":
            with open('Remix/Russian/REAL GIRL/Девушка_Мечты_Real_Girl_Cover_ShaHriX_Trap_Remix.mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Послала (Cover)":
            with open('Remix/Russian/REAL GIRL/Послала как и обещала (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Девушка Мечты (Full Version)":
            with open('Remix/Russian/REAL GIRL/Девушка_Мечты_ShaHriX_Remix_Real_Girl_Cover_Full_Version.mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Девушка Мечты (Original Cover)":
            with open('Remix/Russian/REAL GIRL/Девушка_Мечты_ShaHriX_Remix_Real_Girl_Original_Cover.mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Отпускаю (Cover)":
            with open('Remix/Russian/REAL GIRL/Отпускаю (Real Girl Cover) (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  SCIRENA

        elif message.text == "Scirena":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.ScirenaRemixesButton)
            await delete_message_2(message)
            await state.finish()

    #  SLAVA MARLOW

        elif message.text == "Slava Marlow":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.SlavaMarlowRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Ты Горишь Как Огонь":
            with open('Remix/Russian/SLAVA MARLOW/Ты Горишь Как Огонь (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Кому Это Надо":
            with open('Remix/Russian/SLAVA MARLOW/Кому Это Надо (ShaHriX & Muzaffaroff Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  SLAVIK POGOSOV

        elif message.text == "Slavik Pogosov":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.SlavikPogosovRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Монро":
            with open('Remix/Russian/SLAVIK POGOSOV/Монро (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  HAMMALI NAVAI

        elif message.text == "Hammali & Navai":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.HammaliNavaiRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Не Люби Меня":
            with open('Remix/Russian/XAMMALI & NAVAI/Не Люби Меня HammAli & Navai (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Где Ты Была":
            with open('Remix/Russian/XAMMALI & NAVAI/Где Ты была (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "А Если Это Любовь":
            with open('Remix/Russian/XAMMALI & NAVAI/Hammali_&_Navai_А_Если_Это_Любовь_Amalee_&_Shahrix_Remix.mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Девочка Танцуй":
            with open('Remix/Russian/XAMMALI & NAVAI/Девочка Танцуй (ShaHriX & Saurbaev Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Птичка":
            with open('Remix/Russian/XAMMALI & NAVAI/Птичка (ShaHriX & Orkenoff Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  XASSA

        elif message.text == "Xassa":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.XassaRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Дикари":
            with open('Remix/Russian/XASSA/Дикари (ShaHriX & Demirow Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  XCHO

        elif message.text == "Xcho":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.XchoRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Мысли":
            with open('Remix/Russian/XCHO/Мысли (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Музыка В Ночи":
            with open('Remix/Russian/XCHO/Музыка в Ночи (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Поэт":
            with open('Remix/Russian/XCHO/Поэт (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Memories":
            with open('Remix/Russian/XCHO/MACAN & Xcho - Memories (Amalee & ShaHrix Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "All Right":
            with open('Remix/Russian/XCHO/All Right (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  АМУРА

        elif message.text == "Амура":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.AmuraRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Как Дела":
            with open('Remix/Russian/AMURA/Как Дела (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Минимум":
            with open('Remix/Russian/AMURA/Минимум (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Спрячься":
            with open('Remix/Russian/AMURA/Спрячься (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Хотелось Бросить":
            with open('Remix/Russian/AMURA/Хотелось бросить (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  АНЕТ САЙ

        elif message.text == "Анет Сай":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.AnetSayRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Слёзы":
            with open('Remix/Russian/АНЕТ САЙ/Слёзы (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  АРКАЙДА

        elif message.text == "Аркайда":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.ArkaydaRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Дай Дыма Брат":
            with open('Remix/Russian/АРКАЙДА/Дай Дыма Брат (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  ДЖАРАХОВ

        elif message.text == "Джарахов":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.DjarahovRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Я в моменте":
            with open('Remix/Russian/ДЖАРАХОВ/Я в моменте (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  ЕГОР КРИД

        elif message.text == "Егор Крид":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.EgorKreedRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "(Не) Идеальна":
            with open('Remix/Russian/ЕГОР КРИД/(Не)Идеальна (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Отпускаю":
            with open('Remix/Russian/ЕГОР КРИД/Отпускаю (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "We Gotta Get Love":
            with open('Remix/Russian/ЕГОР КРИД/We Gotta Get Love (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  КАНГИ

        elif message.text == "Канги":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.KangiRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Голова":
            with open('Remix/Russian/КАНГИ/Голова (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Возьми Сердце Моё":
            with open('Remix/Russian/КАНГИ/Возьми Сердце Моё (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Жить Не Запретишь":
            with open('Remix/Russian/КАНГИ/Жить Не Запретишь (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Эйя":
            with open('Remix/Russian/КАНГИ/Эйя (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  КАСПИЙСКИЙ ГРУЗ

        elif message.text == "Каспийский Груз":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.KaspiyskiyGruzRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "На белом":
            with open('Remix/Russian/КАСПИЙСКИЙ ГРУЗ/На белом (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  КЛАВА КОКА

        elif message.text == "Клава Кока":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.KlavaKokaRemixesButton)
            await delete_message_2(message)
            await state.finish()

    #  КОСТА ЛАКОСТА

        elif message.text == "Коста Лакоста":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.KostaLakostaRemixesButton)
            await delete_message_2(message)
            await state.finish()

    #  КРИСПИ

        elif message.text == "Криспи":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.KrispiRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Целуй":
            with open('Remix/Russian/КРИСПИ/Целуй (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  КУЧЕР

        elif message.text == "Кучер":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.KucherRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "По Щекам Слёзы":
            with open('Remix/Russian/КУЧЕР/По Щекам Слёзы (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Се Ля Ви":
            with open('Remix/Russian/КУЧЕР/Се Ля Ви (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  РАЙДА

        elif message.text == "Райда":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.RaydaRemixesButton)
            await delete_message_2(message)
            await state.finish()

    #  СКРИПТОНИТ

        elif message.text == "Скриптонит":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.SkriptonitRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Чистый":
            with open('Remix/Russian/СКРИПТОНИТ/Чистый (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Baby Mama":
            with open('Remix/Russian/СКРИПТОНИТ/Baby Mama (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  СУЛТАН ЛАГУЧЕВ

        elif message.text == "Султан Лагучев":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.SultanLaguchevRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Горький Вкус":
            with open('Remix/Russian/СУЛТАН ЛАГУЧЕВ/Горький Вкус (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Не Души":
            with open('Remix/Russian/СУЛТАН ЛАГУЧЕВ/Не Души (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  ЭЛДЖЕЙ

        elif message.text == "Элджей":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.EldjeyRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Бронежилет":
            with open('Remix/Russian/ЭЛДЖЕЙ/Бронежилет (ShaHriX Remix) (2).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Harakiri":
            with open('Remix/Russian/ЭЛДЖЕЙ/Harakiri (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)
    #  ЭНШПИЛЬ

        elif message.text == "Эндшпиль":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.EndshpilRemixesButton)
            await delete_message_2(message)
            await state.finish()

    #  10AGE

        elif message.text == "10Age":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.IOAgeRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Нету Интереса":
            with open('Remix/Russian/10AGE/Нету Интереса (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Пушка":
            with open('Remix/Russian/10AGE/Пушка (ShaHriX & Olzhas Serikov Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Паровозик":
            with open('Remix/Russian/10AGE/Паровозик (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)










    #  ENGLISH REMIXES

    #  BLACKBEAR

        elif message.text == "Blackbear":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.BlackbearRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "IDFC":
            with open('Remix/English/BLACKBEAR/blackbear - idfc [aibek berkimbaev & shahrix remix].mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  CASSETTE

        elif message.text == "Cassette":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.CassetteRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "My Way":
            with open('Remix/English/CASSETTE/My Way (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  DAFT PUNK

        elif message.text == "Daft Punk":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.DaftPunkRemixesButton)
            await delete_message_2(message)
            await state.finish()


        elif message.text == "Get Lucky":
            with open('Remix/English/DAFT PUNK/Get Lucky (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  DUA LIPA

        elif message.text == "Dua Lipa":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.SeanPaulRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "No Lie":
            with open('Remix/English/DUA LIPA/No Lie (ShaHriX & Camron Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  FOUSHEE

        elif message.text == "Foushee":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.FousheeRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Deep End":
            with open('Remix/English/FOUSHEE/Deep End (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  G-EASY

        elif message.text == "G-Easy":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.GEasyRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Him & I":
            with open('Remix/English/G-EASY/Him & I (ShaHriX & Melix Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)
    #  GHOSTLY KISSES

        elif message.text == "Ghostly Kisses":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.GhostlyKissesRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Empty Note":
            with open('Remix/English/GHOSTLY KISSES/Ghostly_Kisses_Empty_Note_Aibek_Berkimbaev_&_ShaHriX_remix.mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  HALSEY

        elif message.text == "Halsey":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.HalseyRemixesButton)
            await delete_message_2(message)
            await state.finish()

    #  IAN STORM

        elif message.text == "Ian Storm":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.IanStormRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Run Away":
            with open('Remix/English/IAN STORM/Run Away (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  INNA

        elif message.text == "Inna":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.InnaRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Lonely":
            with open('Remix/English/INNA/Lonely (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        elif message.text == "Solo":
            with open('Remix/English/INNA/Solo (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)
    #  JVLA

        elif message.text == "Jvla":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.JvlaRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Such A Whore":
            with open('Remix/English/JVLA/Such A Whole Remix.mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  KENTA GRACE

        elif message.text == "Kenya Grace":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.KenyaGraceRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Strangers":
            with open('Remix/English/KENYA GRACE/Strangers (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  KINA

        elif message.text == "Kina":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.KinaRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Get You The Moon":
            with open('Remix/English/KINA/Kina - Get You The Moon (ShaHriX & Amalee Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  LADY GAGA

        elif message.text == "Lady Gaga":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.LadyGagaRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Bloody Mary":
            with open('Remix/English/LADY GAGA/Bloody Mary (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  LISA

        elif message.text == "Lisa":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.LisaRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Money":
            with open('Remix/English/LISA/Money (ShaHriX & TheBlvcks  Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  MINELLI

        elif message.text == "Minelli":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.MinelliRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Rampampam":
            with open('Remix/English/MINELLI/Rampampam (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  MISHLAWI

        elif message.text == "Mishlawi":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.MishlawiRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "All Night":
            with open('Remix/English/MISHLAWI/All Night (ShaHriX & JustBlack$ Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  NBSPLV

        elif message.text == "Nbsplv":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.NbsplvRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "The Lost Soul Down":
            with open('Remix/English/NBSPLV/The Lost Soul Down (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  OLIVER TREE

        elif message.text == "Oliver Tree":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.OliverTreeRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Cowboys Don't Cry":
            with open('Remix/English/OLIVER TREE/Cowboys Dont Cry (ShaHriX & UNPY Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  PHARELL WILLIAMS

        elif message.text == "Pharell Williams":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.PharellWilliamsRemixesButton)
            await delete_message_2(message)
            await state.finish()

    #  SEAN PAUL

        elif message.text == "Sean Paul":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.SeanPaulRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Go Down Deh":
            with open('Remix/English/SEAN PAUL/Go Down Deh (ShaHriX & TheBlvcks Remix) (2).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  SELENA GOMEZ

        elif message.text == "Selena Gomez":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.TrevorDanielRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Past Life":
            with open('Remix/English/SELENA GOMEZ/Trevor Daniel & Selena Gomez - Past Life (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  SPICE

        elif message.text == "Spice":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.SpiceRemixesButton)
            await bot.delete_message(chat_id = user_id, message_id = message.message_id)
            await bot.delete_message(chat_id = user_id, message_id = message.message_id - 1)
            await state.finish()

    #  SQUID GAME

        elif message.text == "Squid Game":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.SquidGameRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Pink Soldiers":
            with open('Remix/English/SQUID GAME/Pink Soldiers (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  SZA

        elif message.text == "SZA":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.SZARemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Big Boy":
            with open('Remix/English/SZA/Big Boy (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  TIESTO

        elif message.text == "Tiesto":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.TiestoRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "The Business":
            with open('Remix/English/TIESTO/The Business (ShaHriX Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    #  TREVOR DANIEL

        elif message.text == "Trevor Daniel":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.TrevorDanielRemixesButton)
            await delete_message_2(message)
            await state.finish()

    #  XXXTENTACION

        elif message.text == "Xxxtentacion":
            await bot.send_message(message.chat.id, "<b> Выберите Песню: </b>", parse_mode='html', reply_markup=reply_markups.XXXTentacionRemixesButton)
            await delete_message_2(message)
            await state.finish()

        elif message.text == "Bad":
            with open('Remix/English/XXXTENTACION/Bad (ShaHriX & JustBlack$ Remix).mp3', 'rb') as remix:
                await bot.delete_message(chat_id = user_id, message_id = message.message_id)
                text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
                await asyncio.sleep(0.5)
                await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
                await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
                await bot.delete_message(chat_id = user_id, message_id = text.message_id)

        else:

            await bot.send_message(message.chat.id, "<b> Ничего не нашлось  🙁 </b>", parse_mode = 'html')
            await bot.send_message(message.chat.id, "<b> Убедитесь о правильности названия песни или имени артиста ❗️ </b>", parse_mode = 'html')
            await bot.delete_message(chat_id = message.chat.id, message_id = message.message_id)



#  DELETE MESSAGES

#  DELETE MESSAGE 1
async def delete_message_1(message):
    try:
        await bot.delete_message(chat_id = message.chat.id, message_id = message.message_id)
    except:
        pass

#  DELETE MESSAGE 2
async def delete_message_2(message):
    try:
        await bot.delete_message(chat_id = message.chat.id, message_id = message.message_id)
        await bot.delete_message(chat_id = message.chat.id, message_id = message.message_id - 1)
    except:
        pass

#  DELETE MESSAGE 3
async def delete_message_3(message):
    try:
        await bot.delete_message(chat_id = message.chat.id, message_id = message.message_id)
        await bot.delete_message(chat_id = message.chat.id, message_id = message.message_id - 1)
        await bot.delete_message(chat_id = message.chat.id, message_id = message.message_id - 2)
    except:
        pass












#  SEND MESSAGE
async def send_message(message):

    if message.text == "Отмена":
        await bot.send_message(message.chat.id, f"<b> Отменено ❗ </b>", parse_mode = "html", reply_markup = reply_markups.admin_reply)

    else:

        await bot.send_message(message.chat.id, "<b> Рассылка началась  ✅ </b>", parse_mode = "html", reply_markup = reply_markups.menu_reply)

        sql.execute('SELECT * FROM user_data')
        data = sql.fetchall()

        sql.execute('SELECT COUNT(id) FROM user_data')
        all_users = sql.fetchone()[0]

        total = 0

        for users in data:
            try:

                await bot.send_message(users[0], message.text, parse_mode = "html")

                total += 1
                print(f"[{users[0]}]: получил сообщение  ✅")

            except:

                print(f"[{users[0]}]: заблокировал бота  ❌")

        else:

            blocked_users = all_users - total

            await bot.send_message(message.chat.id, f"<b>✅  Ваше сообщение успешно отправлено:  {total}  пользователям из:  {all_users - 1}   </b>", parse_mode="html", reply_markup = None)
            await bot.send_message(message.chat.id, f"<b>❌  Заблокировавшие пользователи:  {blocked_users - 1} </b>", parse_mode="html", reply_markup = None)






#  SEND MUSIC
async def send_music(message):

    if message.text == "Отмена":
        await bot.send_message(message.chat.id, f"<b> Отменено ❗ </b>", parse_mode = "html", reply_markup = reply_markups.admin_reply)

    else:

        await bot.send_message(message.chat.id, "<b> Рассылка началась  ✅ </b>", parse_mode = "html", reply_markup = reply_markups.menu_reply)

        sql.execute('SELECT * FROM user_data')
        data = sql.fetchall()

        sql.execute('SELECT COUNT(id) FROM user_data')
        all_users = sql.fetchone()[0]

        total = 0

        file_info = bot.get_file(message.audio.file_id)
        file = bot.download_file(file_info.file_path)

        with open(f"Music/{message.audio.title}", "wb") as new_file:
            new_file.write(file)

            for users in data:
                try:

                    with open(f"Music/{message.audio.title}", "rb") as audio:
                        await bot.send_audio(users[0], audio)

                        total += 1
                        print(f"[{users[0]}]: получил сообщение  ✅")

                except:

                    print(f"[{users[0]}]: заблокировал бота  ❌")

            else:

                blocked_users = all_users - total

                await bot.send_message(message.chat.id, f"<b>✅  Ваш трек успешно отправлен:  {total}  пользователям из:  {all_users - 1}   </b>", parse_mode="html", reply_markup = None)
                await bot.send_message(message.chat.id, f"<b>❌  Заблокировавшие пользователи:  {blocked_users - 1} </b>", parse_mode="html", reply_markup = None)


















#  CALLBACK QUERY

@dp.callback_query_handler(lambda call: True)
async def callbacks(call: types.CallbackQuery):

#  USER ID

    user_id = call.message.chat.id

#  TRACKS

    if call.data == "track_1":
        with open('Music/Young And In Love.mp3', 'rb') as track:
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, track, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif call.data == "track_2":
        with open('Music/Fade Away.mp3', 'rb') as track:
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, track, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)





#  TOP REMIXES

    elif call.data == "top_remix_1":
        with open('Remix/Russian/REAL GIRL/Девушка_Мечты_ShaHriX_Remix_Real_Girl_Cover_Full_Version.mp3', 'rb') as remix:
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif call.data == "top_remix_2":
        with open('Remix/Russian/KONFUZ/РаТаТа (ShaHriX Remix).mp3', 'rb') as remix:
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif call.data == "top_remix_3":
        with open('Remix/Russian/LXE/Девочка Наркотик (ShaHriX Remix).mp3', 'rb') as remix:
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif call.data == "top_remix_4":
        with open('Remix/Russian/MIYAGI/Санавабич (ShaHriX Remix).mp3', 'rb') as remix:
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif call.data == "top_remix_5":
        with open('Remix/English/LISA/Money (ShaHriX & TheBlvcks  Remix).mp3', 'rb') as remix:
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif call.data == "top_remix_6":
        with open('Remix/Russian/MACAN/ASPHALT 8 (ShaHriX Remix).mp3', 'rb') as remix:
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif call.data == "top_remix_7":
        with open('Remix/English/SZA/Big Boy (ShaHriX Remix).mp3', 'rb') as remix:
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif call.data == "top_remix_8":
        with open('Remix/Russian/REAL GIRL/Всё для тебя (ShaHriX Remix).mp3', 'rb') as remix:
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif call.data == "top_remix_9":
        with open('Remix/Russian/ELMAN/Зари (ShaHriX Remix).mp3', 'rb') as remix:
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif call.data == "top_remix_10":
        with open('Remix/Russian/CVETOCEK7/Седая Ночь (Cvetocek7 Cover) (ShaHriX Remix).mp3', 'rb') as remix:
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)





#  NEW REMIXES

    elif call.data == "new_remix_1":
        with open('Remix/English/KENYA GRACE/Strangers (ShaHriX Remix).mp3', 'rb') as remix:
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif call.data == "new_remix_2":
        with open('Remix/Russian/PUSSYKILLER/Одним выстрелом (ShaHriX Remix).mp3', 'rb') as remix:
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif call.data == "new_remix_3":
        with open('Remix/Russian/AVG/Я плачу (ShaHriX Remix).mp3', 'rb') as remix:
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif call.data == "new_remix_4":
        with open('Remix/Russian/MACAN/Поспешили (ShaHriX Remix).mp3', 'rb') as remix:
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif call.data == "new_remix_5":
        with open('Remix/Russian/AMURA/Минимум (ShaHriX Remix).mp3', 'rb') as remix:
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif call.data == "new_remix_6":
        with open('Remix/Russian/ANNA ASTI/Царица (ShaHriX Remix).mp3', 'rb') as remix:
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif call.data == "new_remix_7":
        with open('Remix/Russian/BY ИНДИЯ/Money (ShaHriX & Gloumir Remix).mp3', 'rb') as remix:
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif call.data == "new_remix_8":
        with open('Remix/Russian/REAL GIRL/Все решено (ShaHriX Remix).mp3', 'rb') as remix:
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif call.data == "new_remix_9":
        with open('Remix/Russian/XCHO/Музыка в Ночи (ShaHriX Remix).mp3', 'rb') as remix:
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)

    elif call.data == "new_remix_10":
        with open('Remix/Russian/BY ИНДИЯ/Еще хуже (ShaHriX Remix).mp3', 'rb') as remix:
            text = await bot.send_message(chat_id = user_id, text = "<b> Отправляется . </b>", parse_mode='html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . </b>", parse_mode = 'html')
            await asyncio.sleep(0.5)
            await bot.edit_message_text(chat_id = user_id, message_id = text.message_id, text = "<b> Отправляется . . . </b>", parse_mode = 'html')
            await bot.send_audio(user_id, remix, reply_markup = inline_markups.channel_inline)
            await bot.delete_message(chat_id = user_id, message_id = text.message_id)













#  ON START UP
async def start_bot(_):
    await bot.send_message(284929331, 'Бот успешно включён !')




#  LAUNCH
if __name__ == '__main__':
    try:
        executor.start_polling(dp, skip_updates = True, on_startup = start_bot)
    except Exception as e:
        print(e)



