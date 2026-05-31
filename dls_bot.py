import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8192598977:AAEX4eykCxTZTJ4R1PqB0kYs5wmq1lsPdw4")
ADMIN_ID = 6470396397

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

IMAGES = {
    "season": None, "tanga_olmos": None,
    "acc_1": None, "acc_2": None, "acc_3": None,
    "acc_4": None, "acc_5": None, "acc_6": None,
}

class ImageState(StatesGroup):
    waiting_image = State()

def main_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton("🎫 Season Pass"), KeyboardButton("💰 Tanga & Olmos"))
    kb.add(KeyboardButton("👤 Accountlar"), KeyboardButton("ℹ️ DLS26 Haqida"))
    kb.add(KeyboardButton("📞 Murojaat"), KeyboardButton("🏆 Reyting"))
    return kb

def contact_kb():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("📩 @DAVLATOV_5577", url="https://t.me/DAVLATOV_5577"))
    return kb

def admin_kb():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("🖼 Rasm yangilash", callback_data="admin_image"))
    kb.add(InlineKeyboardButton("📢 E'lon yuborish", callback_data="admin_broadcast"))
    return kb

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(
        "🎮 *DLS 26 — Rasmiy Bot*\n\nAssalomu alaykum! Xush kelibsiz! 👋\n\nQuyidagi bo'limlardan birini tanlang 👇",
        parse_mode="Markdown", reply_markup=main_menu()
    )

@dp.message_handler(lambda m: m.text == "🎫 Season Pass")
async def season_pass(message: types.Message):
    text = (
        "🎫 *DLS 26 — SEASON PASS*\n━━━━━━━━━━━━━━━━━━━━\n\n"
        "🔥 *AKSIYALI:* 25,000 so'm\n"
        "💎 *AKSIYASIZ:* 40,000 so'm\n\n"
        "📞 Sotib olish uchun adminga murojaat!"
    )
    if IMAGES["season"]:
        await message.answer_photo(IMAGES["season"], caption=text, parse_mode="Markdown", reply_markup=contact_kb())
    else:
        await message.answer(text, parse_mode="Markdown", reply_markup=contact_kb())

@dp.message_handler(lambda m: m.text == "💰 Tanga & Olmos")
async def tanga_olmos(message: types.Message):
    text = (
        "💰 *TANGA & OLMOS NARXLARI*\n━━━━━━━━━━━━━━━━━━━━\n\n"
        "🥉 *80,000 so'm*\n🪙 40k Tanga | 💎 1,000 Olmos\n⏰ 5-6 kun | 👤 1 Classic\n\n"
        "🥈 *150,000 so'm*\n🪙 90k Tanga | 💎 2,000 Olmos\n⏰ 10-12 kun | 👤 2 Classic\n\n"
        "🥇 *300,000 so'm*\n🪙 180k Tanga | 💎 4,500 Olmos\n⏰ 22-24 kun | 👤 3 Classic\n\n"
        "💠 *400,000 so'm*\n🪙 300k Tanga | 💎 6,500 Olmos\n⏰ 33-36 kun | 👤 4 Classic\n\n"
        "🔷 *600,000 so'm*\n🪙 400k Tanga | 💎 8,000 Olmos\n⏰ 45-50 kun | 👤 4 Classic\n\n"
        "👑 *700,000 so'm*\n🪙 500k Tanga | 💎 10,000 Olmos\n⏰ 62 kun | 👤 4 Classic\n\n"
        "📞 Buyurtma uchun adminga murojaat!"
    )
    if IMAGES["tanga_olmos"]:
        await message.answer_photo(IMAGES["tanga_olmos"], caption=text, parse_mode="Markdown", reply_markup=contact_kb())
    else:
        await message.answer(text, parse_mode="Markdown", reply_markup=contact_kb())

@dp.message_handler(lambda m: m.text == "👤 Accountlar")
async def accountlar(message: types.Message):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("🔴 Account #1", callback_data="acc_1"))
    kb.add(InlineKeyboardButton("🟠 Account #2", callback_data="acc_2"))
    kb.add(InlineKeyboardButton("🟡 Account #3", callback_data="acc_3"))
    kb.add(InlineKeyboardButton("🟢 Account #4", callback_data="acc_4"))
    kb.add(InlineKeyboardButton("🔵 Account #5", callback_data="acc_5"))
    kb.add(InlineKeyboardButton("🟣 Account #6", callback_data="acc_6"))
    kb.add(InlineKeyboardButton("📩 Admin", url="https://t.me/DAVLATOV_5577"))
    await message.answer("👤 *ACCOUNTLAR*\nBirini tanlang 👇", parse_mode="Markdown", reply_markup=kb)

@dp.callback_query_handler(lambda c: c.data.startswith("acc_"))
async def account_detail(callback: types.CallbackQuery):
    acc_id = callback.data
    img = IMAGES.get(acc_id)
    text = f"👤 *Account #{acc_id[-1]}*\n\n📞 Narx uchun adminga murojaat!"
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("📩 Admin", url="https://t.me/DAVLATOV_5577"))
    if img:
        await callback.message.answer_photo(img, caption=text, parse_mode="Markdown", reply_markup=kb)
    else:
        await callback.message.answer(text, parse_mode="Markdown", reply_markup=kb)
    await callback.answer()

@dp.message_handler(lambda m: m.text == "ℹ️ DLS26 Haqida")
async def dls_haqida(message: types.Message):
    await message.answer(
        "⚽ *DREAM LEAGUE SOCCER 2026*\n━━━━━━━━━━━━━━━━━━━━\n\n"
        "🌟 Yangi grafika\n⚽ 5000+ futbolchi\n🏟 Yangi stadionlar\n"
        "🌐 Onlayn multiplayer\n🎫 Season Pass\n\n📞 @DAVLATOV_5577",
        parse_mode="Markdown", reply_markup=contact_kb()
    )

@dp.message_handler(lambda m: m.text == "📞 Murojaat")
async def murojaat(message: types.Message):
    await message.answer(
        "📞 *MUROJAAT*\n━━━━━━━━━━━━━━━━━━━━\n\n"
        "👤 Admin: @DAVLATOV_5577\n⏰ 09:00 — 23:00\n📍 Tez javob!",
        parse_mode="Markdown", reply_markup=contact_kb()
    )

@dp.message_handler(lambda m: m.text == "🏆 Reyting")
async def reyting(message: types.Message):
    await message.answer(
        "🏆 *TOP XARIDORLAR*\n━━━━━━━━━━━━━━━━━━━━\n\n"
        "🥇 1. @user1 — 5 xarid\n🥈 2. @user2 — 4 xarid\n🥉 3. @user3 — 3 xarid",
        parse_mode="Markdown", reply_markup=main_menu()
    )

@dp.message_handler(commands=["admin"])
async def admin_panel(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        await message.answer("❌ Ruxsat yo'q!")
        return
    await message.answer("⚙️ *ADMIN PANEL*", parse_mode="Markdown", reply_markup=admin_kb())

@dp.callback_query_handler(lambda c: c.data == "admin_image")
async def admin_image(callback: types.CallbackQuery):
    if callback.from_user.id != ADMIN_ID:
        await callback.answer("❌ Ruxsat yo'q!")
        return
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("🎫 Season Pass", callback_data="img_season"))
    kb.add(InlineKeyboardButton("💰 Tanga/Olmos", callback_data="img_tanga_olmos"))
    kb.add(InlineKeyboardButton("👤 Account #1", callback_data="img_acc_1"))
    kb.add(InlineKeyboardButton("👤 Account #2", callback_data="img_acc_2"))
    kb.add(InlineKeyboardButton("👤 Account #3", callback_data="img_acc_3"))
    kb.add(InlineKeyboardButton("👤 Account #4", callback_data="img_acc_4"))
    kb.add(InlineKeyboardButton("👤 Account #5", callback_data="img_acc_5"))
    kb.add(InlineKeyboardButton("👤 Account #6", callback_data="img_acc_6"))
    await callback.message.answer("Qaysi rasmni yangilamoqchisiz?", reply_markup=kb)
    await callback.answer()

@dp.callback_query_handler(lambda c: c.data.startswith("img_"))
async def choose_image(callback: types.CallbackQuery, state: FSMContext):
    if callback.from_user.id != ADMIN_ID:
        await callback.answer("❌ Ruxsat yo'q!")
        return
    key = callback.data.replace("img_", "")
    await state.update_data(image_key=key)
    await ImageState.waiting_image.set()
    await callback.message.answer("Yangi rasmni yuboring:")
    await callback.answer()

@dp.message_handler(state=ImageState.waiting_image, content_types=types.ContentType.PHOTO)
async def save_image(message: types.Message, state: FSMContext):
    data = await state.get_data()
    key = data.get("image_key")
    IMAGES[key] = message.photo[-1].file_id
    await message.answer("✅ Rasm saqlandi!")
    await state.finish()

@dp.callback_query_handler(lambda c: c.data == "admin_broadcast")
async def admin_broadcast(callback: types.CallbackQuery):
    if callback.from_user.id != ADMIN_ID:
        await callback.answer("❌ Ruxsat yo'q!")
        return
    await callback.message.answer("📢 E'lon yuborish tez orada!")
    await callback.answer()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
