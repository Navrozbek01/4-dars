# run.py
import asyncio
from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton, FSInputFile
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.exceptions import TelegramForbiddenError

from tugmalar import *
from config import TOKEN
from logger import log_action, log_system
import traceback

bot = Bot(token=TOKEN)
dp = Dispatcher()


class Reg(StatesGroup):
    name = State()
    number = State()


# # 1-Handler - Start komandasi
# #print("Bu yangi commit uchun!")
# @dp.message(CommandStart())
# async def cmd_start(message: Message):
#     await message.answer(f"Assalomu alaykum hurmatli foydalanuvchi!\nTest Botimizga xush kelibsiz!",
#                         reply_markup=menyu)

@dp.message(CommandStart())
async def cmd_start(message: Message):
    log_action(message.from_user, "/start komandasi bosildi")
    try:
        ## Internetdan to'g'ri gifni olish
        # await message.answer_animation(animation="https://avatars.dzeninfra.ru/get-zen_doc/5227693/pub_62544d2f7d73a62ef8d8f0ac_62572ad521806f06afb2d287/orig")

        ## Kompyuterdan ststik faylni (gifni) olish
        # gif = FSInputFile("Gif/Mister Bin.mp4")
        # await message.answer_animation(gif)

        ## Gifni matnli xabarga qo'shib bir Telegram post qilib yuborish
        # gif = FSInputFile("Gif/Mister Bin.mp4")
        # await message.answer_animation(
        #     animation=gif,
        #     caption=("Assalomu alaykum hurmatli foydalanuvchi!\nTest Botimizga xush kelibsiz!"),
        #     reply_markup=menyu
        # )
        ## Oddiy xabar yuborish
        # await message.answer(
        #     "Assalomu alaykum hurmatli foydalanuvchi!\nTest Botimizga xush kelibsiz!",
        #     reply_markup=menyu
        # )

        # photo = FSInputFile("Foto/Janob Bin.jpg")
        # await message.answer("Xush kelibsiz!")
        # await message.answer_photo(photo=photo, caption="Bu xabar Foto bilan qo'shilib boradi!")

        # await message.answer_photo(photo="https://i.pinimg.com/736x/c9/97/7f/c9977f50c5efef3b02de04bd6ac04fb4.jpg", caption="Bu foto Internetdan to'g'ri URL orqali olindi!")

        await message.answer("Assalomu alaykum!\nTelegram Botimizga xush kelibsiz!", reply_markup=menyu)


    except TelegramForbiddenError:
        print(f"Foydalanuvchi {message.from_user} botni bloklagan!")


# 2-Handler - Katalog tugmasi
@dp.callback_query(F.data == 'catalog')
async def catalog(callback: CallbackQuery):
    log_action(callback.from_user, "Katalog tugmasi bosildi")
    await callback.answer("Siz Katalog tugmasini bosdingiz!")
    await callback.message.edit_text('Bitta meva tanlang:', reply_markup=inline_katalog)


# 3-Handler - Yordam tugmasi
@dp.callback_query(F.data == 'help')
async def help_handler(callback: CallbackQuery):
    log_action(callback.from_user, "Yordam tugmasi bosildi")
    await callback.answer("Yordam bo'limi!")
    help_text = """
Bot haqida:

Bu bot mevalar katalogi haqida ma'lumot beradi.

Buyruqlar:
/start - Botni ishga tushirish
Katalog - Mevalar ro'yxatini ko'rish
Yordam - Bu xabarni ko'rish

Mavjud mevalar:
Anor, Olma, Anjir, Banan, Uzum

Savollar bo'lsa, Adminga murojaat qiling.
    """
    await callback.message.edit_text(help_text, reply_markup=bosh_sahifa)


# 4-Handler - Anor haqida
@dp.callback_query(F.data == 'anor')
async def anor_info(callback: CallbackQuery):
    log_action(callback.from_user, "Anor tugmasi bosildi")

    await callback.answer("Anor haqida ma'lumot!")

    anor_text = """
ANOR HAQIDA MA'LUMOT

Oddiy anor (lotincha: Púnica granátum) — derbenlar oilasiga (Lythraceae) turkumiga mansub o'simlik turi, mevasi iste'molga yaroqli.

Foydali xususiyatlari:
• Vitaminlar (C, K, folat) bilan boy
• Antioksidantlar miqdori yuqori
• Yurак-qon tomir tizimi uchun foydali
• Immunitetni mustahkamlaydi

Iste'mol qilish usullari:
• Xom holda iste'mol qilish
• Tayyor ovqatlarga qo'shish
• Sharbat sifatida ichish
• Salatlarga qo'shish

Mavsumi: Sentabrdan fevralgacha (shimoliy yarimsharda)

Anor Gʻarbiy Osiyo aholisi tomonidan qadim zamonlardan buyon qo'llanib kelinadi.
    """
    await callback.message.answer_photo(
        photo="clck.ru/3Nodhq", # Bu Yerda Anorni rasmi bor !
        caption=anor_text, reply_markup=orqaga_va_bosh)


# 5-Handler - Olma haqida
@dp.callback_query(F.data == 'olma')
async def olma_info(callback: CallbackQuery):
    log_action(callback.from_user, "Olma tugmasi bosildi")
    await callback.answer("Olma haqida ma'lumot!")
    olma_text = """
OLMA HAQIDA MA'LUMOT

Olma (lotincha: Malus domestica) — guldoshlar oilasiga mansub daraxt mevasi.

Foydali xususiyatlari:
• Tolalar (fiber) bilan boy
• Vitamin C manbai
• Antioksidantlar mavjud
• Xolesterol darajasini kamaytiradi

Iste'mol qilish usullari:
• Xom holda iste'mol
• Pishirish uchun
• Sharbat tayyorlash
• Quritilgan olma

Mavsumi: Avgustdan noyabrgacha
    """
    await callback.message.answer_photo(
        photo="clck.ru/3Nodo2", # Bu Yerda Olmani rasmi bor !
        caption=olma_text, reply_markup=orqaga_va_bosh)


# 6-Handler - Anjir haqida
@dp.callback_query(F.data == 'anjir')
async def anjir_info(callback: CallbackQuery):
    log_action(callback.from_user, "Anjir tugmasi bosildi")
    await callback.answer("Anjir haqida ma'lumot!")
    anjir_text = """
ANJIR HAQIDA MA'LUMOT

Anjir (lotincha: Ficus carica) — tut oilasiga mansub o'simlik mevasi.

Foydali xususiyatlari:
• Tolalar bilan juda boy
• Kaliy va magniy manbai
• Tabiiy shakar mavjud
• Suyak salomatligi uchun foydali

Iste'mol qilish usullari:
• Yangi anjir
• Quritilgan anjir
• Murabbo tayyorlash
• Shirinliklar uchun

Mavsumi: Iyuldan oktabrgacha

Anjir qadimgi zamonlardan beri O'rta er dengizi hududlarida yetishtiriladi.
    """
    await callback.message.answer_photo(
        photo="clck.ru/3NoegD", # Bu Yerda Anjir rasmi bor !
        caption=anjir_text, reply_markup=orqaga_va_bosh)


# 7-Handler - Banan haqida
@dp.callback_query(F.data == 'banan')
async def banan_info(callback: CallbackQuery):
    log_action(callback.from_user, "Banan tugmasi bosildi")
    await callback.answer("Banan haqida ma'lumot!")
    banan_text = """
BANAN HAQIDA MA'LUMOT

Banan (lotincha: Musa) — banan oilasiga mansub tropik o'simlik mevasi.

Foydali xususiyatlari:
• Kaliy bilan juda boy
• Vitamin B6 manbai
• Tabiiy energiya beruvchi
• Sportchilar uchun ideal

Iste'mol qilish usullari:
• Xom holda iste'mol
• Smoodi tayyorlash
• Pishiriq uchun
• Quritilgan chips

Mavjudligi: Yil davomida

Banan tropik va subtropik hududlarda yetishtiriladi va dunyoning eng mashhur mevalaridan biri.
    """
    await callback.message.answer_photo(
        photo="clck.ru/3Noehx", # Bu Yerda Banan rasmi bor !
        caption=banan_text, reply_markup=orqaga_va_bosh)


# 8-Handler - Uzum haqida
@dp.callback_query(F.data == 'uzum')
async def uzum_info(callback: CallbackQuery):
    log_action(callback.from_user, "Uzum tugmasi bosildi")
    await callback.answer("Uzum haqida ma'lumot!")
    uzum_text = """
UZUM HAQIDA MA'LUMOT

Uzum (lotincha: Vitis vinifera) — uzum oilasiga mansub o'simlik mevasi.

Foydali xususiyatlari:
• Antioksidantlar (resveratrol) bilan boy
• Vitamin C va K mavjud
• Yurak salomatligi uchun foydali
• Xotira yaxshilaydi

Iste'mol qilish usullari:
• Yangi uzum
• Quritilgan uzum (mayiz)
• Sharbat tayyorlash
• Vino ishlab chiqarish

Mavsumi: Avgustdan oktabrgacha

Uzum qadimgi zamonlardan beri dunyoning turli hududlarida yetishtiriladi va vino ishlab chiqarish uchun ishlatiladi.
    """
    await callback.message.answer_photo(
        photo="clck.ru/3Noem6", # Bu Yerda Uzum rasmi bor !
        caption=uzum_text, reply_markup=orqaga_va_bosh)


# 9-Handler - Orqaga qaytish (katalogga)
@dp.callback_query(F.data.in_(['orqaga', 'back']))
async def orqaga_katalog(callback: CallbackQuery):
    log_action(callback.from_user, "Orqaga qaytish (katalogga) tugmasi bosildi")
    await callback.answer("Katalogga qaytildi!")
    await callback.message.answer('Bitta meva tanlang:', reply_markup=inline_katalog)


# 10-Handler - Bosh sahifaga qaytish
@dp.callback_query(F.data == 'bosh_sahifa')
async def bosh_sahifa_handler(callback: CallbackQuery):
    log_action(callback.from_user, "Bosh sahifaga qaytish tugmasi bosildi")
    await callback.answer("Bosh sahifaga qaytildi!")
    await callback.message.answer(f"Assalomu alaykum hurmatli foydalanuvchi!\nTest Botimizga xush kelibsiz!",
                                  reply_markup=menyu)


@dp.message(Command('reg'))
async def reg_1(message: Message, state: FSMContext):
    log_action(message.from_user, "/reg komandasi bosildi")
    await state.set_state(Reg.name)
    await message.answer('Ismingizni kiriting:')


@dp.message(Reg.name)
async def reg_2(message: Message, state: FSMContext):
    log_action(message.from_user, "Foydalanuvchi 2-statega o'tkazildi")
    await state.update_data(name=message.text)
    await state.set_state(Reg.number)
    await message.answer('Telefon raqamingizni kiriting: ', reply_markup=phone_button)


@dp.message(Reg.number)
async def two_three(message: Message, state: FSMContext):
    log_action(message.from_user, "Foydalanuvchi 3-statega o'tkazildi")
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(
        f"Tabriklaymiz!\nSiz telegram Botimizdan ro'yxatdan o'tdingiz!\nIsm: {data["name"]}\nRaqam: {data["number"]}",
        reply_markup=menyu)
    await state.clear()


async def main():
    print("Bot ishga tushdi...")
    log_system("Bot ishga tushdi ✅")
    try:
        await dp.start_polling(bot)
    except Exception as e:
        log_system(f"Xatolik: {e}\nTraceback:\n{traceback.format_exc()}", level="error")
    finally:
        log_system("Bot to‘xtadi ❌")


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Dastur to'xtadi!")