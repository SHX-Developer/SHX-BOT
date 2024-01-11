from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



#  OFFICIAL CHANNEL
channel_inline = InlineKeyboardMarkup()
channel_inline.row(InlineKeyboardButton('🎶  Официальный канал автора  🎶', url = 'https://t.me/ShaHriX_Music'))



#  OFFICIAL CHAT
chat_inline = InlineKeyboardMarkup()
chat_inline.row(InlineKeyboardButton('✅  Записаться на пробный урок', url = 'https://t.me/ShaHriXMusic'))


course_inline = InlineKeyboardMarkup()
course_inline.row(InlineKeyboardButton('✅  Записаться', url = 'https://t.me/ShaHriXMusic'))



#  TRACKS
official_tracks_inline = InlineKeyboardMarkup(row_width = 1)
official_tracks_inline.row(InlineKeyboardButton(text = "Young And In Love", callback_data = "track_1"))
official_tracks_inline.row(InlineKeyboardButton(text = "Fade Away", callback_data = "track_2"))



#  TOP REMIXES
top_remixes_inline = InlineKeyboardMarkup()
top_remixes_inline.row(InlineKeyboardButton(text = "Нэнси - Чистый Лист (Real Girl Cover) (ShaHriX Remix)", callback_data = "top_remix_1"))
top_remixes_inline.row(InlineKeyboardButton(text = "Konfuz - Ратата (ShaHriX Remix)", callback_data = "top_remix_2"))
top_remixes_inline.row(InlineKeyboardButton(text = "Raikaho & Lxe - Девочка Наркотик (ShaHriX Remix)", callback_data = "top_remix_3"))
top_remixes_inline.row(InlineKeyboardButton(text = "Miyagi & Эндшпиль - Санавабич (ShaHriX Remix)", callback_data = "top_remix_4"))
top_remixes_inline.row(InlineKeyboardButton(text = "Lisa - Money (ShaHriX & TheBlvcks Remix)", callback_data = "top_remix_5"))
top_remixes_inline.row(InlineKeyboardButton(text = "MACAN - ASPHALT 8 (ShaHriX Remix)", callback_data = "top_remix_6"))
top_remixes_inline.row(InlineKeyboardButton(text = "Sza - Big Boy (ShaHriX Remix)", callback_data = "top_remix_7"))
top_remixes_inline.row(InlineKeyboardButton(text = "Real Girl - Всё для тебя (ShaHriX Remix)", callback_data = "top_remix_8"))
top_remixes_inline.row(InlineKeyboardButton(text = "Andro, ELMAN, TONI, MONA - Зари", callback_data = "top_remix_9"))
top_remixes_inline.row(InlineKeyboardButton(text = "Cvetocek7 - Седая Ночь (ShaHriX Remix)", callback_data = "top_remix_10"))




#  NEW REMIXES
new_remixes_inline = InlineKeyboardMarkup()
new_remixes_inline.row(InlineKeyboardButton(text = "Kenya Grace - Strangers (ShaHrix Remmix)", callback_data = "new_remix_1"))
new_remixes_inline.row(InlineKeyboardButton(text = "PUSSYKILLER - Одним выстрелом (ShaHriX Remix)", callback_data = "new_remix_2"))
new_remixes_inline.row(InlineKeyboardButton(text = "A.V.G - Я плачу (ShaHriX Remix)", callback_data = "new_remix_3"))
new_remixes_inline.row(InlineKeyboardButton(text = "MACAN, Jakone - Поспешили (ShaHriX Remix)", callback_data = "new_remix_4"))
new_remixes_inline.row(InlineKeyboardButton(text = "Амура - Минимум (ShaHriX Remix)", callback_data = "new_remix_5"))
new_remixes_inline.row(InlineKeyboardButton(text = "ANNA ASTI - Царица (ShaHriX Remix)", callback_data = "new_remix_6"))
new_remixes_inline.row(InlineKeyboardButton(text = "By Индия, The Limba - money (ShaHriX Remix)", callback_data = "new_remix_7"))
new_remixes_inline.row(InlineKeyboardButton(text = "Elvira T - Все решено (Real Girl Cover) (ShaHriX Remix)", callback_data = "new_remix_8"))
new_remixes_inline.row(InlineKeyboardButton(text = "Xcho - Музыка в Ночи (ShaHriX Remix)", callback_data = "new_remix_9"))
new_remixes_inline.row(InlineKeyboardButton(text = "By Индия - ещё хуже (ShaHriX Remix)", callback_data = "new_remix_10"))





#  SOCIAL NETWORKS
social_networks_inline = InlineKeyboardMarkup()
social_networks_inline.row(InlineKeyboardButton(text = "💬   TELEGRAM", url = "https://t.me/ShaHriX_Music"))
social_networks_inline.row(InlineKeyboardButton(text = "🔻   YOUTUBE", url = "https://www.youtube.com/channel/UCDCWwYn-PpN443Shev-J4kg"))
social_networks_inline.row(InlineKeyboardButton(text = "📷   INSTAGRAM", url = "https://www.instagram.com/shahrixmusic/"))
social_networks_inline.row(InlineKeyboardButton(text = "🔷   VK", url = "https://vk.com/public203837947"))
social_networks_inline.row(InlineKeyboardButton(text = "🎶   TIK TOK", url = "https://www.tiktok.com/@shahrix_music"))
social_networks_inline.row(InlineKeyboardButton(text = "🟣   TWITCH", url = "https://www.twitch.tv/shahrixmusic"))



#  CONNECT
connect_inline = InlineKeyboardMarkup()
connect_inline.row(InlineKeyboardButton(text = "💬   Связаться", url = "https://t.me/ShaHriXMusic"))






