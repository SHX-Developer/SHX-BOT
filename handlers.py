from aiogram import Bot, F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from database import fetchall_query, fetchone_query, execute_query, add_basic_data
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

from config import ADMIN_IDS
import keyboards as kb
import texts as txt
import constants as const

router = Router()
_language_cache: dict[int, str] = {}



class SearchState(StatesGroup):
    search_query = State()


async def get_user_language_row(user_id: int) -> tuple[str]:
    if user_id not in _language_cache:
        row = await fetchone_query('SELECT language FROM user_data WHERE user_id = ?', (user_id,))
        _language_cache[user_id] = row[0] if row else '-'
    return (_language_cache[user_id],)


async def set_user_language(user_id: int, language: str) -> None:
    await execute_query('UPDATE user_data SET language = ? WHERE user_id = ?', (language, user_id))
    _language_cache[user_id] = language







@router.message(Command('users_count'))
async def test(message: Message, bot: Bot):
    if message.chat.id in ADMIN_IDS:
        count = (await fetchone_query('SELECT COUNT(*) FROM user_data'))[0]
        await bot.send_message(
            chat_id=message.chat.id, 
            text=f'Количество пользователей:  <b>{count}</b>')






#  START COMMAND
@router.message(CommandStart())
async def command_start(message: Message, bot: Bot):
    user_id = message.from_user.id
    username = message.from_user.username
    firstname = message.from_user.first_name
    lastname = message.from_user.last_name
    fullname = message.from_user.full_name
    language = message.from_user.language_code
    chat_id = message.chat.id
    chat_type = message.chat.type
    is_premium = message.from_user.is_premium
    date = message.date.date().strftime('%Y-%m-%d')
    time = message.date.time().strftime('%H:%M:%S')

    if chat_type == 'private':
        search_id = await fetchone_query('SELECT user_id FROM user_access WHERE user_id = ?', (user_id,))

        if search_id is None:
            await add_basic_data(user_id, username, firstname, lastname, fullname, language, chat_id, chat_type, is_premium, date, time)
            await request_language(bot, user_id)

        else:
            language = await get_user_language_row(user_id)
            if language[0] == '-':
                await request_language(bot, user_id)
            
            else:
                await send_menu(bot, user_id)







#  CHANGE LANGUAGE
@router.message(Command(commands=['language']))
async def change_language(message: Message, bot: Bot):
    user_id = message.from_user.id
    await request_language(bot, user_id)
    await message.delete()




#  REQUEST LANGUAGE
async def request_language(bot, user_id):
    await bot.send_message(
        chat_id=user_id, 
        text=txt.choose_language_text,
        reply_markup=kb.language)






#  REGISTER LANGUAGE - RUSSIAN
@router.callback_query(F.data == 'russian')
async def russian(call: CallbackQuery, bot: Bot):
    await call.answer()
    user_id = call.from_user.id
    message_id = call.message.message_id
    await set_user_language(user_id, 'ru')

    await bot.delete_message(chat_id=user_id, message_id=message_id)
    await send_menu(bot, user_id)



#  REGISTER LANGUAGE - ENGLISH
@router.callback_query(F.data == 'english')
async def uzbek(call: CallbackQuery, bot: Bot):
    await call.answer()
    user_id = call.from_user.id
    message_id = call.message.message_id
    await set_user_language(user_id, 'en')

    await bot.delete_message(chat_id=user_id, message_id=message_id)    
    await send_menu(bot, user_id)







#  SEND MENU
async def send_menu(bot, user_id):
    language = await get_user_language_row(user_id)
    if language[0] == 'ru':
        text = txt.ru_greeting_text
        button = kb.ru_menu
    else:
        text = txt.en_greeting_text
        button = kb.en_menu
    
    await bot.send_message(
        chat_id=user_id, 
        text=text,
        reply_markup=button)














# #  NEW TRACKS
# @router.message(F.text.in_(["🎶 Новинки", "🎶 New"]))
# async def new_tracks(message: Message, bot: Bot):
#     user_id = message.from_user.id
#     message_id = message.message_id

#     current_month = const.CURRENT_MONTH
#     right = current_month - 1

#     language = await get_user_language_row(user_id)
#     if language[0] == 'ru':
#         next_text = txt.ru_next_page_text
#         title_text = txt.ru_title_text.format(current_month)
#     else:
#         next_text = txt.en_next_page_text
#         title_text = txt.en_title_text.format(current_month)

#     data = await fetchall_query('SELECT * FROM new WHERE month = ?', (current_month,))

#     keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=row[2], callback_data=row[3])] for row in data])
#     keyboard.inline_keyboard.append([InlineKeyboardButton(text=next_text, callback_data=f"display_page_{right}")])

#     await bot.send_message(
#         chat_id=user_id,
#         text=title_text,
#         reply_markup=keyboard)





# #  DISPLAY PAGE
# @router.callback_query(F.data.startswith('display_page_'))
# async def display_page(call: CallbackQuery, bot: Bot):
#     await call.answer()
#     user_id = call.from_user.id
#     message_id = call.message.message_id
#     month = int(call.data.split('_')[-1])
#     current_month = const.CURRENT_MONTH

#     right = month - 1
#     left = month + 1

#     language = await get_user_language_row(user_id)
#     if language[0] == 'ru':
#         next_text = txt.ru_next_page_text
#         prev_text = txt.ru_previous_page_text
#         title_text = txt.ru_title_text.format(current_month)
#     else:
#         next_text = txt.en_next_page_text
#         prev_text = txt.en_previous_page_text
#         title_text = txt.en_title_text.format(current_month)

#     data = await fetchall_query('SELECT * FROM new WHERE month = ?', (month,))

#     keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=row[2], callback_data=row[3])] for row in data])
#     nav_buttons = []
    
#     if month == current_month:
#         nav_buttons.append(InlineKeyboardButton(text=next_text, callback_data=f"display_page_{right}"))
#     elif month == 1:
#         nav_buttons.append(InlineKeyboardButton(text=prev_text, callback_data=f"display_page_{left}"))
#     else:
#         nav_buttons.append(InlineKeyboardButton(text=prev_text, callback_data=f"display_page_{left}"))
#         nav_buttons.append(InlineKeyboardButton(text=next_text, callback_data=f"display_page_{right}"))
    
#     if nav_buttons:
#         keyboard.inline_keyboard.append(nav_buttons)

#     await bot.edit_message_text(
#         chat_id=user_id,
#         message_id=message_id,
#         text=title_text,
#         reply_markup=keyboard)

# #  SEND TRACK
# @router.callback_query(F.data.startswith('track_'))
# async def send_track(call: CallbackQuery, bot: Bot):
#     await call.answer()
#     user_id = call.from_user.id
#     message_id = call.message.message_id

#     data = await fetchone_query('SELECT * FROM new WHERE callback = ?', (call.data,))
#     track_id = data[0]; name = data[2]; callback = data[3]; path = data[4]
    
#     ru_button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="❤️ Добавить в плейлист", callback_data=f"add_playlist_{callback}")]])
#     en_button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="❤️ Add to playlist", callback_data=f"add_playlist_{callback}")]])

#     language = await get_user_language_row(user_id)
#     if language[0] == 'ru':
#         text = txt.ru_links_text
#         not_found_text = txt.ru_no_track_found_text
#         button = ru_button
#     else:
#         text = txt.en_links_text
#         not_found_text = txt.en_no_track_found_text
#         button = en_button
    
#     await bot.send_audio(
#         chat_id=user_id,
#         audio=path,
#         caption=text,
#         reply_markup=button)



    
    

    





#  SEARCH
@router.message(F.text.in_(["🔍 Поиск", "🔍 Search"]))
async def search(message: Message, bot: Bot, state: FSMContext):
    user_id = message.from_user.id
    await state.set_state(SearchState.search_query)

    language = await get_user_language_row(user_id)
    if language[0] == 'ru':
        text = txt.ru_search_text
        button = kb.ru_cancel
    else:
        text = txt.en_search_text
        button = kb.en_cancel
    
    await bot.send_message(
        chat_id=user_id, 
        text=text, 
        reply_markup=button)

#  PROCESS SEARCH
@router.message(SearchState.search_query)
async def process_search(message: Message, bot: Bot, state: FSMContext):
    user_id = message.from_user.id
    query = message.text.strip()

    language = await get_user_language_row(user_id)
    if query == '🚫 Отменить поиск' or query == '🚫 Cancel search':
        await state.clear()
        
        if language[0] == 'ru':
            text = txt.ru_canceled_search_text
            button = kb.ru_menu
        else:
            text = txt.en_canceled_search_text
            button = kb.en_menu
    
        await bot.send_message(
            chat_id=user_id, 
            text=text,
            reply_markup=button)
        return
    

    if language[0] == 'ru':
        text = 'Трек или артист не найден. Пожалуйста, убедитесь в правильности написания и попробуйте снова.'
        found_text = '✅ Трек или артист найден!'
        menu_button = kb.ru_menu
    
    else:
        text = 'Track or artist not found. Please ensure correct spelling and try again.'
        found_text = '✅ Track or artist found!'
        menu_button = kb.en_menu

    russian = await fetchall_query('SELECT * FROM russian WHERE artist = ? OR name = ?', (query, query))
    if russian:
        for row in russian:
            ru_button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="❤️ Добавить в плейлист", callback_data=f"ru_add_playlist_{row[0]}")]])
            en_button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="❤️ Add to playlist", callback_data=f"ru_add_playlist_{row[0]}")]])
            path = row[3]

            if language[0] == 'ru':
                text = txt.ru_links_text
                button = ru_button
                
            else:
                text = txt.en_links_text
                button = en_button

            await bot.send_message(
                chat_id=user_id, 
                text=found_text,
                reply_markup=menu_button)

            await bot.send_audio(
                chat_id=user_id,
                audio=path,
                caption=text,
                reply_markup=button)
            await state.clear()
        return
    
    english = await fetchall_query('SELECT * FROM english WHERE artist = ? OR name = ?', (query, query))
    if english:
        for row in english:
            ru_button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="❤️ Добавить в плейлист", callback_data=f"en_add_playlist_{row[0]}")]])
            en_button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="❤️ Add to playlist", callback_data=f"en_add_playlist_{row[0]}")]])
            path = row[3]

            if language[0] == 'ru':
                text = txt.ru_links_text
                button = ru_button
            else:
                text = txt.en_links_text
                button = en_button

            await bot.send_message(
                chat_id=user_id, 
                text=found_text,
                reply_markup=menu_button)

            await bot.send_audio(
                chat_id=user_id,
                audio=path,
                caption=text,
                reply_markup=button)
            await state.clear()

        return
    
    await bot.send_message(
        chat_id=user_id,
        text=text)





#  REMIXES
@router.message(F.text.in_(["🎶 Ремиксы", "🎶 Remixes"]))
async def remixes(message: Message, bot: Bot):
    user_id = message.from_user.id
    message_id = message.message_id

    language = await get_user_language_row(user_id)
    if language[0] == 'ru':
        text = txt.ru_remixes_text
        button = kb.ru_remixes
    else:
        text = txt.en_remixes_text
        button = kb.en_remixes
    
    await bot.send_message(
        chat_id=user_id, 
        text=text,
        reply_markup=button)







# #  CHAT
# @router.message(F.text.in_(["💬 Чат", "💬 Chat"]))
# async def chat(message: Message, bot: Bot):
#     user_id = message.from_user.id
#     message_id = message.message_id

#     language = await get_user_language_row(user_id)
#     if language[0] == 'ru':
#         text = txt.ru_chat_text
#         button = kb.ru_chat
#     else:
#         text = txt.en_chat_text
#         button = kb.en_chat
    
#     await bot.send_message(
#         chat_id=user_id, 
#         text=text,
#         reply_markup=button)





#  PLAYLIST
@router.message(F.text.in_(["📲 Плейлист", "📲 Playlist"]))
async def playlist(message: Message, bot: Bot):
    user_id = message.from_user.id
    message_id = message.message_id

    language = await get_user_language_row(user_id)
    if language[0] == 'ru':
        text = txt.ru_playlist_text
        empty_text = txt.ru_empty_playlist_text
    else:
        text = txt.en_playlist_text
        empty_text = txt.en_empty_playlist_text
    
    data = await fetchall_query('SELECT * FROM playlists WHERE user_id = ?', (user_id,))
    if not data:
        await bot.send_message(
            chat_id=user_id, 
            text=empty_text)
        return
    
    button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text=row[2], callback_data=f'send_{row[0]}')] for row in data])
    await bot.send_message(
        chat_id=user_id, 
        text=text,
        reply_markup=button)



#  SEND PLAYLIST TRACK
@router.callback_query(F.data.startswith('send_'))
async def send_playlist_track(call: CallbackQuery, bot: Bot):
    await call.answer()
    user_id = call.from_user.id
    message_id = call.message.message_id
    track_id = int(call.data.split('send_')[-1])

    ru_button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="⛔️ Удалить с плейлиста", callback_data=f"remove_playlist_{track_id}")]])
    en_button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="⛔️ Delete from playlist", callback_data=f"remove_playlist_{track_id}")]])
    
    language = await get_user_language_row(user_id)
    if language[0] == 'ru':
        text = txt.ru_links_text
        button = ru_button
    else:
        text = txt.en_links_text
        button = en_button

    data = await fetchone_query('SELECT * FROM playlists WHERE id = ?', (track_id,))
    if data is None:
        if language[0] == 'ru':
            not_found_text = txt.ru_no_track_found_text
        else:
            not_found_text = txt.en_no_track_found_text
        
        await bot.send_message(
            chat_id=user_id,
            text=not_found_text)
        return
    
    path = data[3]
    await bot.send_audio(
        chat_id=user_id,
        audio=path,
        caption=text,
        reply_markup=button)



#  ADD TO PLAYLIST
@router.callback_query(F.data.startswith('add_playlist_'))
async def add_playlist(call: CallbackQuery, bot: Bot):
    await call.answer()
    user_id = call.from_user.id
    message_id = call.message.message_id
    callback = call.data.split('add_playlist_')[-1]

    data = await fetchone_query('SELECT * FROM new WHERE callback = ?', (callback,))
    track_id = data[0]; name = data[2]; callback = data[3]; path = data[4]
    await execute_query('INSERT INTO playlists (user_id, name, path) VALUES (?, ?, ?)', (user_id, name, path))
    
    language = await get_user_language_row(user_id)
    if language[0] == 'ru':
        text = txt.ru_added_to_playlist_text.format(name)
    else:
        text = txt.en_added_to_playlist_text.format(name)
    
    await bot.send_message(
        chat_id=user_id,
        text=text)



#  REMOVE FROM PLAYLIST
@router.callback_query(F.data.startswith('remove_playlist_'))
async def remove_playlist(call: CallbackQuery, bot: Bot):
    await call.answer()
    user_id = call.from_user.id
    message_id = call.message.message_id
    track_id = int(call.data.split('remove_playlist_')[-1])

    await execute_query('DELETE FROM playlists WHERE id = ?', (track_id,))

    language = await get_user_language_row(user_id)
    if language[0] == 'ru':
        text = txt.ru_removed_from_playlist_text
    else:
        text = txt.en_removed_from_playlist_text
    
    await bot.delete_message(chat_id=user_id, message_id=message_id)
    await bot.send_message(
        chat_id=user_id,
        text=text)















#  RUSSIAN REMIXES
@router.message(F.text.in_(["🇷🇺 Русские", "🇷🇺 Russian", "⬅ Предыдущая страница", "⬅ Previous page"]))
async def russian_remixes(message: Message, bot):
    user_id = message.from_user.id

    language = await get_user_language_row(user_id)
    if language[0] == 'ru':
        text = txt.ru_russian_remixes_1_text
        next_page_text = "Следующая страница ➡"
        back_text = "⬅ Назад"
        menu_text = "🏠 Главное меню"
        choose_artist_text = "Выберите артиста, чтобы получить все его ремиксы:"
    else:
        text = txt.en_russian_remixes_1_text
        next_page_text = "Next page ➡"
        back_text = "⬅ Back"
        menu_text = "🏠 Main menu"
        choose_artist_text = "Choose an artist to get all their remixes:"

    artist_buttons = [KeyboardButton(text=name) for name in const.RU_ARTISTS_1]
    rows = [artist_buttons[i:i + 3] for i in range(0, len(artist_buttons), 3)]

    control_row = [
        KeyboardButton(text=back_text),
        KeyboardButton(text=menu_text)]

    rows.insert(0, control_row)
    rows.append([KeyboardButton(text=next_page_text)])
    rows.append(control_row)
    keyboard = ReplyKeyboardMarkup(keyboard=rows, resize_keyboard=True, input_field_placeholder=choose_artist_text)

    await bot.send_message(
        chat_id=user_id,
        text=text,
        reply_markup=keyboard)

@router.message(F.text.in_(["Следующая страница ➡", "Next page ➡"]))
async def russian_remixes_page_2(message: Message, bot):
    user_id = message.from_user.id

    language = await get_user_language_row(user_id)
    if language[0] == 'ru':
        text = txt.ru_russian_remixes_2_text
        prev_page_text = "⬅ Предыдущая страница"
        back_text = "⬅ Назад"
        menu_text = "🏠 Главное меню"
        choose_artist_text = "Выберите артиста, чтобы получить все его ремиксы:"
    else:
        text = txt.en_russian_remixes_2_text
        prev_page_text = "⬅ Previous page"
        back_text = "⬅ Back"
        menu_text = "🏠 Main menu"
        choose_artist_text = "Choose an artist to get all their remixes:"


    artist_buttons = [KeyboardButton(text=name) for name in const.RU_ARTISTS_2]
    rows = [artist_buttons[i:i + 3] for i in range(0, len(artist_buttons), 3)]

    control_row = [
        KeyboardButton(text=back_text),
        KeyboardButton(text=menu_text)]

    rows.insert(0, control_row)
    rows.append([KeyboardButton(text=prev_page_text)])
    rows.append(control_row)
    keyboard = ReplyKeyboardMarkup(keyboard=rows, resize_keyboard=True, input_field_placeholder=choose_artist_text)

    await bot.send_message(
        chat_id=user_id,
        text=text,
        reply_markup=keyboard)



#  ENGLISH REMIXES
@router.message(F.text.in_(["🇺🇸 Английские", "🇺🇸 English"]))
async def english_remixes(message: Message, bot):
    user_id = message.from_user.id

    language = await get_user_language_row(user_id)
    if language[0] == 'ru':
        text = txt.ru_english_remixes_text
        back_text = "⬅ Назад"
        menu_text = "🏠 Главное меню"
        choose_artist_text = "Выберите артиста, чтобы получить все его ремиксы:"
    else:
        text = txt.en_english_remixes_text
        back_text = "⬅ Back"
        menu_text = "🏠 Main menu"
        choose_artist_text = "Choose an artist to get all their remixes:"

    artist_buttons = [KeyboardButton(text=name) for name in const.EN_ARTISTS]
    rows = [artist_buttons[i:i + 3] for i in range(0, len(artist_buttons), 3)]

    control_row = [
        KeyboardButton(text=back_text),
        KeyboardButton(text=menu_text)]

    rows.insert(0, control_row)
    rows.append(control_row)
    keyboard = ReplyKeyboardMarkup(keyboard=rows, resize_keyboard=True, input_field_placeholder=choose_artist_text)

    await bot.send_message(
        chat_id=user_id,
        text=text,
        reply_markup=keyboard)
















#  MAIN MENU
@router.message(F.text.in_(["🏠 Главное меню", "🏠 Main menu"]))
async def main_menu(message: Message, bot: Bot):
    user_id = message.from_user.id
    message_id = message.message_id

    language = await get_user_language_row(user_id)
    if language[0] == 'ru':
        text = txt.ru_greeting_text
        button = kb.ru_menu
    else:
        text = txt.en_greeting_text
        button = kb.en_menu
    
    await bot.send_message(
        chat_id=user_id, 
        text=text,
        reply_markup=button)


#  BACK
@router.message(F.text.in_(["⬅ Назад", "⬅ Back"]))
async def back(message: Message, bot: Bot):
    user_id = message.from_user.id
    message_id = message.message_id

    language = await get_user_language_row(user_id)
    if language[0] == 'ru':
        text = txt.ru_remixes_text
        button = kb.ru_remixes
    else:
        text = txt.en_remixes_text
        button = kb.en_remixes
    
    await bot.send_message(
        chat_id=user_id, 
        text=text,
        reply_markup=button)











@router.message(F.text)
async def text(message: Message, bot: Bot):
    user_id = message.from_user.id
    query = message.text.strip()

    language = await get_user_language_row(user_id)
    if language[0] == 'ru':
        text = 'Неизвестная команда. Пожалуйста, выберите опцию из меню.'
    else:
        text = 'Unknown command. Please choose an option from the menu.'


    russian = await fetchall_query('SELECT * FROM russian WHERE artist = ?', (query,))
    if russian:
        for row in russian:
            ru_button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="❤️ Добавить в плейлист", callback_data=f"ru_add_playlist_{row[0]}")]])
            en_button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="❤️ Add to playlist", callback_data=f"ru_add_playlist_{row[0]}")]])
            path = row[3]

            if language[0] == 'ru':
                text = txt.ru_links_text
                button = ru_button
            else:
                text = txt.en_links_text
                button = en_button

            await bot.send_audio(
                chat_id=user_id,
                audio=path,
                caption=text,
                reply_markup=button)
        return
    
    english = await fetchall_query('SELECT * FROM english WHERE artist = ?', (query,))
    if english:
        for row in english:
            ru_button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="❤️ Добавить в плейлист", callback_data=f"en_add_playlist_{row[0]}")]])
            en_button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="❤️ Add to playlist", callback_data=f"en_add_playlist_{row[0]}")]])
            path = row[3]

            if language[0] == 'ru':
                text = txt.ru_links_text
                button = ru_button
            else:
                text = txt.en_links_text
                button = en_button

            await bot.send_audio(
                chat_id=user_id,
                audio=path,
                caption=text,
                reply_markup=button)
        return
    

    
#  RUSSIAN ADD TO PLAYLIST
@router.callback_query(F.data.startswith('ru_add_playlist_'))
async def add_playlist(call: CallbackQuery, bot: Bot):
    await call.answer()
    user_id = call.from_user.id
    message_id = call.message.message_id
    query = call.data.split('ru_add_playlist_')[-1]

    data = await fetchone_query('SELECT * FROM russian WHERE id = ?', (query,))
    track_id = data[0]; artist = data[1]; name = data[2]; path = data[3]; fullname = '{} - {}'.format(artist, name)
    await execute_query('INSERT INTO playlists (user_id, name, path) VALUES (?, ?, ?)', (user_id, fullname, path))
    
    language = await get_user_language_row(user_id)
    if language[0] == 'ru':
        text = txt.ru_added_to_playlist_text.format(name)
    else:
        text = txt.en_added_to_playlist_text.format(name)
    
    await bot.send_message(
        chat_id=user_id,
        text=text)

#  ENGLISH ADD TO PLAYLIST
@router.callback_query(F.data.startswith('en_add_playlist_'))
async def add_playlist(call: CallbackQuery, bot: Bot):
    await call.answer()
    user_id = call.from_user.id
    message_id = call.message.message_id
    query = call.data.split('en_add_playlist_')[-1]

    data = await fetchone_query('SELECT * FROM english WHERE id = ?', (query,))
    track_id = data[0]; artist = data[1]; name = data[2]; path = data[3]; fullname = '{} - {}'.format(artist, name)
    await execute_query('INSERT INTO playlists (user_id, name, path) VALUES (?, ?, ?)', (user_id, fullname, path))
    
    language = await get_user_language_row(user_id)
    if language[0] == 'ru':
        text = txt.ru_added_to_playlist_text.format(name)
    else:
        text = txt.en_added_to_playlist_text.format(name)
    
    await bot.send_message(
        chat_id=user_id,
        text=text)






















#  DEBUG AUDIO HANDLER
@router.message(F.audio)
async def on_audio(message: Message):
    if message.chat.id in ADMIN_IDS:
        await message.reply(f'<code>{message.audio.file_id}</code>', parse_mode='HTML')

