from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



#  COUNRIES
countries_reply = ReplyKeyboardMarkup(resize_keyboard = True)
countries_reply.row("🇷🇺  Россия", "🇺🇦  Украина")
countries_reply.row("🇺🇿  Узбекистан", "🇰🇿  Казахстан")
countries_reply.row("🌐  Другая")



#  MENU
menu_reply = ReplyKeyboardMarkup(resize_keyboard = True)
menu_reply.row("🎶  Курс - создание ремиксов с нуля")
menu_reply.row("🔥  Ремиксы", "🚀  Топ")
menu_reply.row("🔍  Поиск")
menu_reply.row("🔔 Социальные Сети", "🆘  Обратная Связь")



#  TOP
top_reply = ReplyKeyboardMarkup(resize_keyboard = True)
top_reply.row("🎧  Топ Ремиксы", "🎼  Топ Новинки")
top_reply.row("🏠  Главное меню")



#  REMIX LANGUAGE
remix_language_reply = ReplyKeyboardMarkup(resize_keyboard = True)
remix_language_reply.row("🇷🇺  Русские", "🇺🇸  Английские")
remix_language_reply.row("🏠  Главное меню")



#  OFFICIAL TRACKS
official_tracks_reply = ReplyKeyboardMarkup(resize_keyboard = True)
official_tracks_reply.row("Young And In Love", "Fade Away")
official_tracks_reply.row("🏠  Главное меню")



#  CANCEL
cancel_search_reply = ReplyKeyboardMarkup(resize_keyboard = True)
cancel_search_reply.row("Отменить")



#  RUSSIAN ARTISTS
russian_artists_reply = ReplyKeyboardMarkup(row_width = 3, resize_keyboard = True)
russian_artists_reply.row("⬅   Назад", "🏠  Главное меню")
RussianArtistsButton1 = KeyboardButton("Aleks Ataman")
RussianArtistsButton64 = KeyboardButton("Anna Asti")
RussianArtistsButton2 = KeyboardButton("Andro")
RussianArtistsButton3 = KeyboardButton("Andy Panda")
RussianArtistsButton4 = KeyboardButton("AVG")
RussianArtistsButton57 = KeyboardButton("Bakr")
RussianArtistsButton5 = KeyboardButton("Branya")
RussianArtistsButton63 = KeyboardButton("By Индия")
RussianArtistsButton6 = KeyboardButton("Cvetocek7")
RussianArtistsButton7 = KeyboardButton("Dareem")
RussianArtistsButton8 = KeyboardButton("Elman")
RussianArtistsButton9 = KeyboardButton("Escape")
RussianArtistsButton10 = KeyboardButton("Finik")
RussianArtistsButton11 = KeyboardButton("Gafur")
RussianArtistsButton12 = KeyboardButton("Gidayyat")
RussianArtistsButton13 = KeyboardButton("Guma")
RussianArtistsButton14 = KeyboardButton("Hensy")
RussianArtistsButton59 = KeyboardButton("Iletre")
RussianArtistsButton15 = KeyboardButton("Imanbek")
RussianArtistsButton16 = KeyboardButton("Jakomo")
RussianArtistsButton17 = KeyboardButton("Jamik")
RussianArtistsButton18 = KeyboardButton("Janaga")
RussianArtistsButton19 = KeyboardButton("Jony")
RussianArtistsButton20 = KeyboardButton("Kambulat")
RussianArtistsButton21 = KeyboardButton("Konfuz")
RussianArtistsButton22 = KeyboardButton("Limba")
RussianArtistsButton23 = KeyboardButton("Lxe")
RussianArtistsButton24 = KeyboardButton("Macan")
RussianArtistsButton25 = KeyboardButton("Maksim")
RussianArtistsButton26 = KeyboardButton("Markul")
RussianArtistsButton27 = KeyboardButton("Miyagi")
RussianArtistsButton28 = KeyboardButton("Mona")
RussianArtistsButton29 = KeyboardButton("Moneyken")
RussianArtistsButton30 = KeyboardButton("Morgenshtern")
RussianArtistsButton31 = KeyboardButton("Neki")
RussianArtistsButton32 = KeyboardButton("Nlo")
RussianArtistsButton33 = KeyboardButton("Pussykiller")
RussianArtistsButton34 = KeyboardButton("Raikaho")
RussianArtistsButton35 = KeyboardButton("Rakhim")
RussianArtistsButton36 = KeyboardButton("Ramil")
RussianArtistsButton37 = KeyboardButton("Rauf & Faik")
RussianArtistsButton38 = KeyboardButton("Real Girl")
RussianArtistsButton61 = KeyboardButton("Scirena")
RussianArtistsButton39 = KeyboardButton("Slava Marlow")
RussianArtistsButton58 = KeyboardButton("Slavik Pogosov")
RussianArtistsButton40 = KeyboardButton("Hammali & Navai")
RussianArtistsButton41 = KeyboardButton("Xassa")
RussianArtistsButton42 = KeyboardButton("Xcho")
RussianArtistsButton62 = KeyboardButton("Амура")
RussianArtistsButton43 = KeyboardButton("Анет Сай")
RussianArtistsButton44 = KeyboardButton("Аркайда")
RussianArtistsButton45 = KeyboardButton("Джарахов")
RussianArtistsButton46 = KeyboardButton("Егор Крид")
RussianArtistsButton47 = KeyboardButton("Канги")
RussianArtistsButton58 = KeyboardButton("Каспийский Груз")
RussianArtistsButton48 = KeyboardButton("Клава Кока")
RussianArtistsButton49 = KeyboardButton("Коста Лакоста")
RussianArtistsButton60 = KeyboardButton("Криспи")
RussianArtistsButton50 = KeyboardButton("Кучер")
RussianArtistsButton51 = KeyboardButton("Райда")
RussianArtistsButton52 = KeyboardButton("Скриптонит")
RussianArtistsButton53 = KeyboardButton("Султан Лагучев")
RussianArtistsButton54 = KeyboardButton("Элджей")
RussianArtistsButton55 = KeyboardButton("Эндшпиль")
RussianArtistsButton56 = KeyboardButton("10Age")
russian_artists_reply.add(RussianArtistsButton1, RussianArtistsButton64, RussianArtistsButton2, RussianArtistsButton3, RussianArtistsButton4, RussianArtistsButton57,
                          RussianArtistsButton5, RussianArtistsButton63, RussianArtistsButton6, RussianArtistsButton7, RussianArtistsButton8, RussianArtistsButton9, RussianArtistsButton10,
                          RussianArtistsButton11, RussianArtistsButton12, RussianArtistsButton13, RussianArtistsButton14, RussianArtistsButton59, RussianArtistsButton15,
                          RussianArtistsButton16, RussianArtistsButton17, RussianArtistsButton18, RussianArtistsButton19, RussianArtistsButton20,
                          RussianArtistsButton21, RussianArtistsButton22, RussianArtistsButton23, RussianArtistsButton24, RussianArtistsButton25,
                          RussianArtistsButton26, RussianArtistsButton27, RussianArtistsButton28, RussianArtistsButton29, RussianArtistsButton30,
                          RussianArtistsButton31, RussianArtistsButton32, RussianArtistsButton33, RussianArtistsButton34, RussianArtistsButton35,
                          RussianArtistsButton36, RussianArtistsButton37, RussianArtistsButton38, RussianArtistsButton61, RussianArtistsButton39, RussianArtistsButton58, RussianArtistsButton40,
                          RussianArtistsButton41, RussianArtistsButton42, RussianArtistsButton62, RussianArtistsButton43, RussianArtistsButton44, RussianArtistsButton45,
                          RussianArtistsButton46, RussianArtistsButton47, RussianArtistsButton58, RussianArtistsButton48, RussianArtistsButton49, RussianArtistsButton60, RussianArtistsButton50,
                          RussianArtistsButton51, RussianArtistsButton52, RussianArtistsButton53, RussianArtistsButton54, RussianArtistsButton55,
                          RussianArtistsButton56)
russian_artists_reply.row("⬅   Назад", "🏠  Главное меню")




#  ENGLISH ARTISTS
english_artists_reply = ReplyKeyboardMarkup(row_width = 3, resize_keyboard = True)
english_artists_reply.row("⬅   Назад", "🏠  Главное меню")
EnglishArtistsButton1 = KeyboardButton("Blackbear")
EnglishArtistsButton2 = KeyboardButton("Cassette")
EnglishArtistsButton3 = KeyboardButton("Daft Punk")
EnglishArtistsButton4 = KeyboardButton("Dua Lipa")
EnglishArtistsButton5 = KeyboardButton("Foushee")
EnglishArtistsButton6 = KeyboardButton("G-Easy")
EnglishArtistsButton7 = KeyboardButton("Ghostly Kisses")
EnglishArtistsButton8 = KeyboardButton("Halsey")
EnglishArtistsButton9 = KeyboardButton("Ian Storm")
EnglishArtistsButton10 = KeyboardButton("Inna")
EnglishArtistsButton11 = KeyboardButton("Jvla")
EnglishArtistsButton28 = KeyboardButton("Kenya Grace")
EnglishArtistsButton12 = KeyboardButton("Kina")
EnglishArtistsButton25 = KeyboardButton("Lady Gaga")
EnglishArtistsButton13 = KeyboardButton("Lisa")
EnglishArtistsButton14 = KeyboardButton("Minelli")
EnglishArtistsButton15 = KeyboardButton("Mishlawi")
EnglishArtistsButton27 = KeyboardButton("Nbsplv")
EnglishArtistsButton16 = KeyboardButton("Oliver Tree")
EnglishArtistsButton17 = KeyboardButton("Pharell Williams")
EnglishArtistsButton18 = KeyboardButton("Sean Paul")
EnglishArtistsButton19 = KeyboardButton("Selena Gomez")
EnglishArtistsButton20 = KeyboardButton("Spice")
EnglishArtistsButton21 = KeyboardButton("Squid Game")
EnglishArtistsButton26 = KeyboardButton("SZA")
EnglishArtistsButton22 = KeyboardButton("Tiesto")
EnglishArtistsButton23 = KeyboardButton("Trevor Daniel")
EnglishArtistsButton24 = KeyboardButton("Xxxtentacion")
english_artists_reply.add(EnglishArtistsButton1, EnglishArtistsButton2, EnglishArtistsButton3, EnglishArtistsButton4, EnglishArtistsButton5,
                         EnglishArtistsButton6, EnglishArtistsButton7, EnglishArtistsButton8, EnglishArtistsButton9, EnglishArtistsButton10,
                         EnglishArtistsButton11, EnglishArtistsButton28, EnglishArtistsButton12, EnglishArtistsButton25, EnglishArtistsButton13, EnglishArtistsButton14, EnglishArtistsButton15, EnglishArtistsButton27,
                         EnglishArtistsButton16, EnglishArtistsButton17, EnglishArtistsButton18, EnglishArtistsButton19, EnglishArtistsButton20,
                         EnglishArtistsButton21, EnglishArtistsButton26, EnglishArtistsButton22, EnglishArtistsButton23, EnglishArtistsButton24)
english_artists_reply.row("⬅   Назад", "🏠  Главное меню")



#  RUSSIAN ARTISTS REMIXES

AleksAtamanRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
AleksAtamanRemixesButton.row("Диалоги Тет-а-тет", "ОЙОЙОЙ (ТЫ ГОВОРИЛА)")
AleksAtamanRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

AmuraRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
AmuraRemixesButton.row("Как Дела", "Минимум", "Спрячься")
AmuraRemixesButton.row("Хотелось Бросить")
AmuraRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

AnnaAstiRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
AnnaAstiRemixesButton.row("Царица")
AnnaAstiRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

AndroRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
AndroRemixesButton.row("Другому", "Зари", "X.O")
AndroRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

AndyPandaRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
AndyPandaRemixesButton.row("Патрон", "Там Ревели Горы", "All The Time")
AndyPandaRemixesButton.row("Marmelade")
AndyPandaRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

AnetSayRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
AnetSayRemixesButton.row("Слёзы")
AnetSayRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

ArkaydaRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
ArkaydaRemixesButton.row("Дай Дыма Брат")
ArkaydaRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

AVGRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
AVGRemixesButton.row("Она Кайф", "Платина", "С Тобой")
AVGRemixesButton.row("Я плачу", "25 Кадр")
AVGRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

BakrRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
BakrRemixesButton.row("За Любовь")
BakrRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

BranyaRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
BranyaRemixesButton.row("Пополам")
BranyaRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

ByIndiaRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
ByIndiaRemixesButton.row("Ещё Хуже", "money")
ByIndiaRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

Cvetocek7RemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
Cvetocek7RemixesButton.row("Все ссоры надоели", "Седая Ночь")
Cvetocek7RemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

DareemRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
DareemRemixesButton.row("Новый Год")
DareemRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

DjarahovRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
DjarahovRemixesButton.row("Я в моменте")
DjarahovRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

ElmanRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
ElmanRemixesButton.row("Балкон", "Зари", "Морозы")
ElmanRemixesButton.row("Чёрная Любовь")
ElmanRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

EscapeRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
EscapeRemixesButton.row("Не Смотри")
EscapeRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

EgorKreedRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
EgorKreedRemixesButton.row("(Не) Идеальна", "Отпускаю", "We Gotta Get Love")
EgorKreedRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

EldjeyRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
EldjeyRemixesButton.row("Бронежилет", "Harakiri")
EldjeyRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

EndshpilRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
EndshpilRemixesButton.row("Санавабич")
EndshpilRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

FinikRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
FinikRemixesButton.row("Диалоги Тет-а-тет")
FinikRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

GafurRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
GafurRemixesButton.row("Атом", "OK", "Морозы")
GafurRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

GidayyatRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
GidayyatRemixesButton.row("Лунная")
GidayyatRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

GumaRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
GumaRemixesButton.row("Стеклянная")
GumaRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

HensyRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
HensyRemixesButton.row("Костёр")
HensyRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

IletreRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
IletreRemixesButton.row("Седая Ночь")
IletreRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

ImanbekRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
ImanbekRemixesButton.row("Leck")
ImanbekRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

JakomoRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
JakomoRemixesButton.row("Платина")
JakomoRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

JamikRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
JamikRemixesButton.row("Франция")
JamikRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

JanagaRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
JanagaRemixesButton.row("По Щекам Слёзы")
JanagaRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

JonyRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
JonyRemixesButton.row("Балкон", "Камнепад", "Наверно Ты Меня Не Помнишь")
JonyRemixesButton.row("Небесные Розы", "Ты Пари", "Уйдёшь")
JonyRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

KambulatRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
KambulatRemixesButton.row("Выпей Меня", "Душа Устала", "Звездопад")
KambulatRemixesButton.row("Как Дела", "Письма")
KambulatRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

KonfuzRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
KonfuzRemixesButton.row("Аккорды", "Война", "Выше")
KonfuzRemixesButton.row("Касаюсь", "Не Смотри", "Очень Очень")
KonfuzRemixesButton.row("Пропал Интерес", "Ратата", "Рокстар")
KonfuzRemixesButton.row("Сказка")
KonfuzRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

KangiRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
KangiRemixesButton.row("Возьми Сердце Моё", "Голова", "Жить Не Запретишь")
KangiRemixesButton.row("Эйя")
KangiRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

KaspiyskiyGruzRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
KaspiyskiyGruzRemixesButton.row("На белом")
KaspiyskiyGruzRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

KlavaKokaRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
KlavaKokaRemixesButton.row("Костёр")
KlavaKokaRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

KostaLakostaRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
KostaLakostaRemixesButton.row("Бронежилет")
KostaLakostaRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

KrispiRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
KrispiRemixesButton.row("Целуй")
KrispiRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

KucherRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
KucherRemixesButton.row("По Щекам Слёзы", "Се Ля Ви")
KucherRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

LimbaRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
LimbaRemixesButton.row("Секрет", "X.O")
LimbaRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

LxeRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
LxeRemixesButton.row("Девочка Наркотик")
LxeRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

MacanRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
MacanRemixesButton.row("Пополам", "Поспешили", "Asphalt 8")
MacanRemixesButton.row("IVL", "Memories", "Mp3")
MacanRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

MakSimRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
MakSimRemixesButton.row("Отпускаю")
MakSimRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

MarkulRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
MarkulRemixesButton.row("Стрелы", "Я в моменте")
MarkulRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

MiyagiRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
MiyagiRemixesButton.row("Патрон", "Санавабич", "Там Ревели Горы")
MiyagiRemixesButton.row("All The Time", "Angel", "Marmelade")
MiyagiRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

MonaRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
MonaRemixesButton.row("Зари", "Чёрная Любовь")
MonaRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

MoneykenRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
MoneykenRemixesButton.row("Она Не Любит Вино")
MoneykenRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

MorgenshternRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
MorgenshternRemixesButton.row("Cristal Моёт", "Family", "Leck")
MorgenshternRemixesButton.row("Show")
MorgenshternRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

NekiRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
NekiRemixesButton.row("Мысли", "Огни")
NekiRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

NloRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
NloRemixesButton.row("Не Грусти")
NloRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

PussyKillerRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
PussyKillerRemixesButton.row("Одним Выстрелом", "Франция", "Целуй")
PussyKillerRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

RaikahoRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
RaikahoRemixesButton.row("Девочка Наркотик")
RaikahoRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

RakhimRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
RakhimRemixesButton.row("Аккорды", "Синий Lamborghini", "Уйдёшь")
RakhimRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

RamilRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
RamilRemixesButton.row("Аромат", "Дождь", "Маяк")
RamilRemixesButton.row("Просто Лети", "Сияй", "Сон")
RamilRemixesButton.row("Увидимся", "Mp3")
RamilRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

RaufFaikRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
RaufFaikRemixesButton.row("Деньги и Счастье", "Я Люблю Тебя Давно", "5 Минут")
RaufFaikRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

RealGirlRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
RealGirlRemixesButton.row("Всё Для Тебя (Cover)", "Все Решено")
RealGirlRemixesButton.row("Вино и Сигареты", "Девушка Мечты (Short Version)")
RealGirlRemixesButton.row("Девушка Мечты (Full Version)", "Девушка Мечты (Trap Version)")
RealGirlRemixesButton.row("Девушка Мечты (Original Cover)", "Отпускаю (Cover)")
RealGirlRemixesButton.row("Сектор Газа (Cover)", "Послала (Cover)")
RealGirlRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

RaydaRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
RaydaRemixesButton.row("Baby Mama")
RaydaRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

ScirenaRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
ScirenaRemixesButton.row("IVL")
ScirenaRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

SlavikPogosovRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
SlavikPogosovRemixesButton.row("Монро")
SlavikPogosovRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

SlavaMarlowRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
SlavaMarlowRemixesButton.row("Кому Это Надо", "Ты Горишь Как Огонь")
SlavaMarlowRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

SkriptonitRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
SkriptonitRemixesButton.row("Чистый", "Baby Mama")
SkriptonitRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

SultanLaguchevRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
SultanLaguchevRemixesButton.row("Горький Вкус", "Не Души")
SultanLaguchevRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

HammaliNavaiRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
HammaliNavaiRemixesButton.row("А Если Это Любовь", "Где Ты Была", "Девочка Танцуй")
HammaliNavaiRemixesButton.row("Наверно Ты Меня Не Помнишь", "Не Люби Меня", "Птичка")
HammaliNavaiRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

XassaRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
XassaRemixesButton.row("Дикари")
XassaRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

XchoRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
XchoRemixesButton.row("Музыка В Ночи", "Мысли", "Поэт")
XchoRemixesButton.row( "All Right", "Memories")
XchoRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")

IOAgeRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
IOAgeRemixesButton.row("Нету Интереса", "Паровозик", "Пушка")
IOAgeRemixesButton.row("⬅   Нaзад", "🏠  Главное меню")





#  ENGLISH ARTISTS REMIXES

BlackbearRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
BlackbearRemixesButton.row("IDFC")
BlackbearRemixesButton.row("⬅   Назaд", "🏠  Главное меню")

CassetteRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
CassetteRemixesButton.row("My Way")
CassetteRemixesButton.row("⬅   Назaд", "🏠  Главное меню")

DaftPunkRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
DaftPunkRemixesButton.row("Get Lucky")
DaftPunkRemixesButton.row("⬅   Назaд", "🏠  Главное меню")

DualipaRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
DualipaRemixesButton.row("No Lie")
DualipaRemixesButton.row("⬅   Назaд", "🏠  Главное меню")

FousheeRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
FousheeRemixesButton.row("Deep End")
FousheeRemixesButton.row("⬅   Назaд", "🏠  Главное меню")

GEasyRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
GEasyRemixesButton.row("Him & I")
GEasyRemixesButton.row("⬅   Назaд", "🏠  Главное меню")

GhostlyKissesRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
GhostlyKissesRemixesButton.row("Empty Note")
GhostlyKissesRemixesButton.row("⬅   Назaд", "🏠  Главное меню")

HalseyRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
HalseyRemixesButton.row("Him & I")
HalseyRemixesButton.row("⬅   Назaд", "🏠  Главное меню")

IanStormRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
IanStormRemixesButton.row("Run Away")
IanStormRemixesButton.row("⬅   Назaд", "🏠  Главное меню")

InnaRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
InnaRemixesButton.row("Lonely", "Solo")
InnaRemixesButton.row("⬅   Назaд", "🏠  Главное меню")

JvlaRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
JvlaRemixesButton.row("Such A Whore")
JvlaRemixesButton.row("⬅   Назaд", "🏠  Главное меню")

KenyaGraceRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
KenyaGraceRemixesButton.row("Strangers")
KenyaGraceRemixesButton.row("⬅   Назaд", "🏠  Главное меню")

KinaRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
KinaRemixesButton.row("Get You The Moon")
KinaRemixesButton.row("⬅   Назaд", "🏠  Главное меню")

LadyGagaRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
LadyGagaRemixesButton.row("Bloody Mary")
LadyGagaRemixesButton.row("⬅   Назaд", "🏠  Главное меню")

LisaRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
LisaRemixesButton.row("Money")
LisaRemixesButton.row("⬅   Назaд", "🏠  Главное меню")

MinelliRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
MinelliRemixesButton.row("Rampampam")
MinelliRemixesButton.row("⬅   Назaд", "🏠  Главное меню")

MishlawiRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
MishlawiRemixesButton.row("All Night")
MishlawiRemixesButton.row("⬅   Назaд", "🏠  Главное меню")

NbsplvRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
NbsplvRemixesButton.row("The Lost Soul Down")
NbsplvRemixesButton.row("⬅   Назaд", "🏠  Главное меню")

OliverTreeRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
OliverTreeRemixesButton.row("Cowboys Don't Cry")
OliverTreeRemixesButton.row("⬅   Назaд", "🏠  Главное меню")

PharellWilliamsRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
PharellWilliamsRemixesButton.row("Get Lucky")
PharellWilliamsRemixesButton.row("⬅   Назaд", "🏠  Главное меню")

SeanPaulRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
SeanPaulRemixesButton.row("Go Down Deh", "No Lie")
SeanPaulRemixesButton.row("⬅   Назaд", "🏠  Главное меню")

SelenaGomezRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
SelenaGomezRemixesButton.row("Past Life")
SelenaGomezRemixesButton.row("⬅   Назaд", "🏠  Главное меню")

SpiceRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
SpiceRemixesButton.row("Go Down Deh")
SpiceRemixesButton.row("⬅   Назaд", "🏠  Главное меню")

SquidGameRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
SquidGameRemixesButton.row("Pink Soldiers")
SquidGameRemixesButton.row("⬅   Назaд", "🏠  Главное меню")

SZARemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
SZARemixesButton.row("Big Boy")
SZARemixesButton.row("⬅   Назaд", "🏠  Главное меню")

TiestoRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
TiestoRemixesButton.row("The Business")
TiestoRemixesButton.row("⬅   Назaд", "🏠  Главное меню")

TrevorDanielRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
TrevorDanielRemixesButton.row("Past Life")
TrevorDanielRemixesButton.row("⬅   Назaд", "🏠  Главное меню")

XXXTentacionRemixesButton = ReplyKeyboardMarkup(resize_keyboard = True)
XXXTentacionRemixesButton.row("Bad")
XXXTentacionRemixesButton.row("⬅   Назaд", "🏠  Главное меню")



#  ADMIN
admin_reply = ReplyKeyboardMarkup(resize_keyboard = True)
admin_reply.row("Статистика")
admin_reply.row("Рассылка трека", "Рассылка текста")
admin_reply.row("Рассылка каналов")
admin_reply.row("🏠  Главное меню")

#  CANCEL
admin_cancel_reply = ReplyKeyboardMarkup(resize_keyboard = True)
admin_cancel_reply.row("Отмена")





















