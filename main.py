import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

# ================= НАСТРОЙКИ =================
BOT_TOKEN = "8261950692:AAGPdrjcNIL4M3mZvg1iBuQGI5t5pXQHyZw"
SITE_URL = "https://one-vv02.life/casino/list?open=register&p=rtt2&sub1=1win&sub2=Ere1&sub3=Arm"
PROMO_CODE = "Yere1"
VIDEO_PATH = "login_instruction.mp4"

# ================= ИНИЦИАЛИЗАЦИЯ =================
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# ================= ХРАНЕНИЕ ЯЗЫКА =================
user_languages = {}

# ================= КЛАВИАТУРЫ =================
def language_keyboard():
    kb = [
        [
            types.KeyboardButton(text="🇷🇺 Русский"),
            types.KeyboardButton(text="🇦🇲 Հայերեն")
        ]
    ]
    return types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        one_time_keyboard=True
    )

def main_keyboard_ru():
    kb = [
        [types.KeyboardButton(text="🎁 Бонусы")],
        [types.KeyboardButton(text="🌐 Забрать Бонус и Играть")],
        [types.KeyboardButton(text="📘 Инструкция по входу на сайт")],
        [types.KeyboardButton(text="💳 Пополнение и вывод")],
        [types.KeyboardButton(text="🔄 Сменить язык")]
    ]
    return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

def main_keyboard_am():
    kb = [
        [types.KeyboardButton(text="🎁 Բոնուսներ")],
        [types.KeyboardButton(text="🌐 Վերցնել բոնուսը և խաղալ")],
        [types.KeyboardButton(text="📘 Մուտքի ուղեցույց")],
        [types.KeyboardButton(text="💳 Լիցքավորում և դուրսբերում")],
        [types.KeyboardButton(text="🔄 Փոխել լեզուն")]
    ]
    return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

# ================= /START =================
@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer(
        "Выберите язык / Ընտրեք լեզուն 👇",
        reply_markup=language_keyboard()
    )

# ================= ВЫБОР ЯЗЫКА =================
@dp.message(lambda m: m.text == "🇷🇺 Русский")
async def set_ru(message: types.Message):
    user_languages[message.from_user.id] = "ru"
    await message.answer(
        f"Здравствуйте, {message.from_user.first_name} 👋",
        reply_markup=main_keyboard_ru()
    )

@dp.message(lambda m: m.text == "🇦🇲 Հայերեն")
async def set_am(message: types.Message):
    user_languages[message.from_user.id] = "am"
    await message.answer(
        f"Բարև ձեզ, {message.from_user.first_name} 👋",
        reply_markup=main_keyboard_am()
    )

# ================= СМЕНА ЯЗЫКА =================
@dp.message(lambda m: m.text in ["🔄 Сменить язык", "🔄 Փոխել լեզուն"])
async def change_language(message: types.Message):
    await message.answer(
        "Выберите язык / Ընտրեք լեզուն 👇",
        reply_markup=language_keyboard()
    )

# ================= БОНУСЫ =================
@dp.message(lambda m: m.text in ["🎁 Бонусы", "🎁 Բոնուսներ"])
async def bonuses(message: types.Message):
    lang = user_languages.get(message.from_user.id, "ru")

    if lang == "ru":
        text = """🎁 Бонусы

- 500% на первые 4 депозита
- 600% при пополнении криптовалютой
- Кэшбэк до 30%
- Бонус на экспресс
- 70 фриспинов от 1500₽
- Покерные турниры
- Розыгрыши авто и техники Apple

Вы получите эти бонусы, только перейдя по нашей ссылке и промо-коду
"""
    else:
        text = """🎁 Վերցնել բոնուսը և խաղալ

- 500% առաջին 4 դեպոզիտների համար
- 600% կրիպտո լիցքավորման դեպքում
- Մինչև 30% քեշբեք
- Բոնուս էքսպրեսի համար
- 70 ֆրիսպին 3500֏-ից
- Պոկերի մրցաշարեր
- Ավտոմեքենաների և Apple մրցանակների խաղարկումներ

Դուք կստանաք այս բոնուսները  միայն անցնելով մեր հղումով և պրոմո կոդով
"""

    await message.answer(text)

# ================= ССЫЛКА НА САЙТ + ПРОМОКОД =================
@dp.message(lambda m: m.text in ["🌐 Забрать Бонус и Играть", "🌐 Վերցնել բոնուսը և խաղալ"])
async def site(message: types.Message):
    lang = user_languages.get(message.from_user.id, "ru")

    if lang == "ru":
        await message.answer(
            f"""🌐 Перейти на сайт:
{SITE_URL}

🎁 Промокод для регистрации:
`{PROMO_CODE}`

Обязательно введите промокод, чтобы получить бонусы."""
        )
    else:
        await message.answer(
            f"""🌐 Անցնել կայք:
{SITE_URL}

🎁 Գրանցման պրոմոկոդը՝
`{PROMO_CODE}`

Պրոմոկոդը մուտքագրեք բոնուսներ ստանալու համար։"""
        )

# ================= ВИДЕО ИНСТРУКЦИЯ =================
@dp.message(lambda m: m.text in ["📘 Инструкция по входу на сайт", "📘 Ինչպես մուտք գործել կայք"])
async def instruction(message: types.Message):
    lang = user_languages.get(message.from_user.id, "ru")
    video = types.FSInputFile(VIDEO_PATH)

    if lang == "ru":
        loading_text = "Загрузка..."
        caption = """📘 Инструкция по входу

1️⃣ Перейдите на сайт  
2️⃣ Нажмите «Войти»  
3️⃣ Введите логин и пароль  
4️⃣ Подтвердите вход
"""
    else:
        loading_text = "Բեռնում..."
        caption = """📘 Մուտքի ուղեցույց

1️⃣ Մուտք գործեք կայք  
2️⃣ Սեղմեք «Մուտք»  
3️⃣ Մուտքագրեք տվյալները  
4️⃣ Հաստատեք մուտքը
"""

    loading_msg = await message.answer(loading_text)
    try:
        await message.answer_video(video=video, caption=caption)
    except Exception:
        # при ошибке удаляем сообщение о загрузке и пробрасываем ошибку дальше
        await loading_msg.delete()
        raise
    else:
        # удаляем сообщение "Загрузка..." после успешной отправки видео
        await loading_msg.delete()

# ================= ПОПОЛНЕНИЕ / ВЫВОД =================
@dp.message(lambda m: m.text in ["💳 Пополнение и вывод", "💳 Լիցքավորում և դուրսբերում"])
async def deposit_withdraw(message: types.Message):
    lang = user_languages.get(message.from_user.id, "ru")

    if lang == "ru":
        text = """💳 Пополнение и вывод

🔹 Пополнение:
1️⃣ Войдите в аккаунт
2️⃣ Нажмите «Пополнить»
3️⃣ Выберите способ оплаты
4️⃣ Подтвердите платёж

🔹 Вывод:
1️⃣ Личный кабинет
2️⃣ Нажмите «Вывести»
3️⃣ Выберите метод
4️⃣ Подтвердите заявку
"""
    else:
        text = """💳 Լիցքավորում և դուրսբերում

🔹 Լիցքավորում:
1️⃣ Մուտք գործեք հաշիվ
2️⃣ Սեղմեք «Լիցքավորել»
3️⃣ Ընտրեք վճարման եղանակ
4️⃣ Հաստատեք վճարումը

🔹 Դուրսբերում:
1️⃣ Անձնական հաշիվ
2️⃣ Սեղմեք «Դուրս բերել»
3️⃣ Ընտրեք եղանակը
4️⃣ Հաստատեք հայտը
"""

    await message.answer(text)

# ================= ЗАПУСК =================
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

