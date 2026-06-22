from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton





language = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="🇷🇺 Русский", callback_data="russian"),
     InlineKeyboardButton(text="🇬🇧 English", callback_data="english")]])







# -------------------- MENU --------------------
ru_menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='🎶 Ремиксы')],
    [KeyboardButton(text='🔍 Поиск'), 
     KeyboardButton(text='📲 Плейлист')]],
    resize_keyboard=True)

en_menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='🎶 Remixes')],
    [KeyboardButton(text='🔍 Search'), 
     KeyboardButton(text='📲 Playlist')]],
    resize_keyboard=True)





# -------------------- REMIX LANGUAGES --------------------
ru_remixes = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='🇷🇺 Русские'), KeyboardButton(text='🇺🇸 Английские')],
    [KeyboardButton(text='🏠 Главное меню')]],
    resize_keyboard=True, input_field_placeholder='Выберите язык')

en_remixes = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='🇷🇺 Russian'), KeyboardButton(text='🇺🇸 English')],
    [KeyboardButton(text='🏠 Main menu')]],
    resize_keyboard=True, input_field_placeholder='Choose language of remixes')






# -------------------- CANCEL --------------------
ru_cancel = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='🚫 Отменить поиск')]],
    resize_keyboard=True, input_field_placeholder='Введите название трека или имя артиста:')

en_cancel = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='🚫 Cancel search')]],
    resize_keyboard=True, input_field_placeholder='Enter the track name or artist name:')




# -------------------- BACK --------------------
ru_back = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='⬅ Назад')]],
    resize_keyboard=True, input_field_placeholder='Вернуться назад')

en_back = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='⬅ Back')]],
    resize_keyboard=True, input_field_placeholder='Go back')






# -------------------- MAIN MENU --------------------
ru_main_menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='🏠 Главное меню')]],
    resize_keyboard=True, input_field_placeholder='Вернуться в главное меню')

en_main_menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='🏠 Main menu')]],
    resize_keyboard=True, input_field_placeholder='Return to main menu')







# -------------------- Subscribe --------------------
ru_subscribe = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🎶 ShaHriXMusic', url='https://t.me/+hAbZZYXs0O5kNzBi')],
    [InlineKeyboardButton(text='✅ Проверить', callback_data='check')]])


en_subscribe = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🎶 ShaHriXMusic', url='https://t.me/+hAbZZYXs0O5kNzBi')],
    [InlineKeyboardButton(text='✅ Check', callback_data='check')]])







# -------------------- Chat --------------------
ru_chat = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='📲 Перейти в чат', url='https://t.me/+uHPwQOJPeAowNTAy')]])

en_chat = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='📲 Go to chat', url='https://t.me/+uHPwQOJPeAowNTAy')]])




