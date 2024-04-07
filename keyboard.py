from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

main_kb = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="Математика"),
            KeyboardButton(text="Русский язык")
        ]
    ],
    input_field_placeholder="Выберите действия из меню"
)

math_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton
            (
                text="дроби",
                url="http://vekgivi.ru/pravila_deystviy_nad_drobjami/"
            ),
            InlineKeyboardButton
            (
                text="графики функций",
                url="https://epmat.ru/modul-algebra/urok-5-grafiki-funktsij/"
            ),
        ],
        [
            InlineKeyboardButton
            (
                text="неравенства",
                url="https://epmat.ru/modul-algebra/urok-8-neravenstva-sistemy-neravenstv/"
            ),
            InlineKeyboardButton
            (
                text="квадратные уравнения",
                url="https://ege-study.ru/kvadratnye-uravneniya/"
            )
        ],
        [
            InlineKeyboardButton
            (
                text="квадратные неравенства",
                url="http://cos-cos.ru/math/178/"
            ),
            InlineKeyboardButton
            (
                text="системы уравнений",
                url="https://www.napishem.ru/spravochnik/matematika/funkczii/sistemy-uravnenij-s-dvumya-peremennymi-sposoby-resheniya.html"
            )
        ],
        [
            InlineKeyboardButton
            (
                text="Общие математические формулы",
                url="https://educon.by/index.php/formuly/formmat"
            )
        ]
    ],
    input_field_placeholder="Выберите действия из меню"
)

russian_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton
            (
                text="словосочетания",
                url="https://skysmart.ru/articles/russian/vidy-svyazi-v-slovosochetaniyah"
            ),
            InlineKeyboardButton
            (
                text="односоставные предложения",
                url="https://skysmart.ru/articles/russian/tipy-odnosostavnyh-predlozhenij"
            ),
        ],
        [
            InlineKeyboardButton
            (
                text="сложные предложения",
                url="https://skysmart.ru/articles/russian/slozhnoe-predlozhenie"
            ),
            InlineKeyboardButton
            (
                text="сочинения-рассуждения",
                url="https://ctege.info/teoriya-oge-po-russkomu-yazyiku/sochinenie-oge-po-russkomu-yazyiku.html"
            ),
        ],
        [
            InlineKeyboardButton
            (
                text="чередование гласных в корне",
                url="https://skysmart.ru/articles/russian/cheredovanie-glasnyh-v-korne"
            ),
            InlineKeyboardButton
            (
                text="правописание -н- и -нн-",
                url="https://www.kp.ru/putevoditel/ege/russkij-yazyk/pravopisanie-n-i-nn/"
            ),
        ],
        [
            InlineKeyboardButton
            (
                text="Основные случаи постановки запятых",
                url="https://www.sravni.ru/text/rasstavlyat-zapyatye-v-predlozhenii/"
            ),
        ]
    ],
    input_field_placeholder="Выберите действия из меню"
)