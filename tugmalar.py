from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

menyu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Katalog', callback_data='catalog')
    ],

    [
        InlineKeyboardButton(text='Yordam', callback_data='help')
    ]
]
)

# Inline Keyboard
inline_katalog = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Anor", callback_data='anor'),
            InlineKeyboardButton(text="Olma", callback_data='olma')
        ],
        [
            InlineKeyboardButton(text="Anjir", callback_data='anjir'),
            InlineKeyboardButton(text="Banan", callback_data='banan'),
            InlineKeyboardButton(text="Uzum", callback_data='uzum')
        ],
        [
            InlineKeyboardButton(text='Orqaga', callback_data='orqaga')
        ]

])

orqaga = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Orqaga', callback_data='orqaga')
    ]
])



# # Reply Keyboard
# reply_katalog = ReplyKeyboardMarkup(keyboard=[
#     [
#         KeyboardButton(text="Anor")
#     ],
#     [
#         KeyboardButton(text="Olma"),
#         KeyboardButton(text="Anjir")
#     ],
#     [
#         KeyboardButton(text="Banan"),
#         KeyboardButton(text="Uzum"),
#         KeyboardButton(text="Shaftoli")
#     ]
# ],
# resize_keyboard=True,
# input_field_placeholder="Kerakli tugmani bosing...")






# mevalar = ['Anor', 'Olma', 'Anjir', 'Banan', 'Uzum', 'Shaftoli']

# async def inline_cars():
#     keyboard = InlineKeyboardBuilder()
#     for meva in mevalar:
#         keyboard.add(InlineKeyboardButton(text=meva, url='...'))
#     return keyboard.adjust(3).as_markup()



# Uyga vazifa: Unikal mavzuda Bot yarating, unda 10 ta Handler yarating, ularning har birida 10 tadan tugma bo'lsin!

# Statik
# 2 ta Handler Reply keyboard orqali yaratilsin!
# 3 ta Handler Inline keyboard orqali yaratilsin!

# Dinamik
# 5 ta Handlerda for orqali button bo'lsin!
# 2 ta Handler Reply keyboard orqali yaratilsin!
# 3 ta Handler Inline keyboard orqali yaratilsin!
