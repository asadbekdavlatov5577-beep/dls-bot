import logging
import os
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import (
    InlineKeyboardMarkup, InlineKeyboardButton,
    ReplyKeyboardMarkup, KeyboardButton,
)
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiohttp import web

BOT_TOKEN = "8192598977:AAFVqw9wPipHcuksvWmCjo5cgsgsZwGUNtU"
ADMIN_ID = 6470396397
WEBHOOK_HOST = "https://dls-bot-hwgn.onrender.com"
WEBHOOK_PATH = f"/webhook/{BOT_TOKEN}"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

IMAGES = {
    "season": None,
    "tanga_olmos": None,
    "acc_1": None,
    "acc_2": None,
    "acc_3": None,
    "acc_4": None,
    "acc_5": None,
    "acc_6": None,
}

class AdminStates(StatesGroup):
    waiting_image = State()

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
def main_menu():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🎫 Season Pass"), KeyboardButton(text="💰 Tanga & Olmos")],
            [KeyboardButton(text="👤 Accountlar"), KeyboardButton(text="ℹ️ DLS26 Haqida")],
            [KeyboardButton(text="📞 Murojaat"), KeyboardButton(text="🏆 Reyting")],
        ],
        resize_keyboard=True
    )
    return kb

def contact_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📩 @DAVLATOV_5577", url="https://t.me/DAVLATOV_5577")]
    ])

def admin_panel_kb():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🖼 Rasm yangilash", callback_data="admin_update_image")],
        [InlineKeyboardButton(text="📊 Statistika", callback_data="admin_stats")],
    ])

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "🎮 *DLS 26 — Rasmiy Bot*\n\nAssalomu alaykum! Xush kelibsiz! 👋\n\nQuyidagi bo'limlardan birini tanlang 👇",
        parse_mode="Markdown", reply_markup=main_menu()
    )

@dp.message(F.text == "🎫 Season Pass")
async def season_pass(message: types.Message):
    text = (
        "🎫 *DLS 26 — SEASON PASS*\n━━━━━━━━━━━━━━━━━━━━\n\n"
        "🔥 *AKSIYALI:* 25,000 so'm\n"
        "💎 *AKSIYASIZ:* 40,000 so'm\n\n"
        "📞 Sotib olish uchun adminga murojaat!"
    )
    if IMAGES["season"]:
        await message.answer_photo(photo=IMAGES["season"], caption=text, parse_mode="Markdown", reply_markup=contact_kb())
    else:
        await message.answer(text, parse_mode="Markdown", reply_markup=contact_kb())

@dp.message(F.text == "💰 Tanga & Olmos")
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
        await message.answer_photo(photo=IMAGES["tanga_olmos"], caption=text, parse_mode="Markdown", reply_markup=contact_kb())
    else:
        await message.answer(text, parse_mode="Markdown", reply_markup=contact_kb())

@dp.message(F.text == "👤 Accountlar")
async def accountlar(message: types.Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔴 Account #1", callback_data="acc_1")],
        [InlineKeyboardButton(text="🟠 Account #2", callback_data="acc_2")],
        [InlineKeyboardButton(text="🟡 Account #3", callback_data="acc_3")],
        [InlineKeyboardButton(text="🟢 Account #4", callback_data="acc_4")],
        [InlineKeyboardButton(text="🔵 Account #5", callback_data="acc_5")],
        [InlineKeyboardButton(text="🟣 Account #6", callback_data="acc_6")],
        [InlineKeyboardButton(text="📩 Admin", url="https://t.me/DAVLATOV_5577")],
    ])
    await message.answer("👤 *ACCOUNTLAR*\nBirini tanlang 👇", parse_mode="Markdown", reply_markup=kb)

@dp.callback_query(F.data.startswith("acc_"))
async def account_detail(callback: types.CallbackQuery):
    acc_id = callback.data
    img = IMAGES.get(acc_id)
    text = f"👤 *Account #{acc_id[-1]}*\n\n📞 Narx uchun adminga murojaat!"
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📩 Admin", url="https://t.me/DAVLATOV_5577")]
    ])
    if img:
        await callback.message.answer_photo(photo=img, caption=text, parse_mode="Markdown", reply_markup=kb)
    else:
        await callback.message.answer(text, parse_mode="Markdown", reply_markup=kb)
    await callback.answer()

@dp.message(F.text == "ℹ️ DLS26 Haqida")
async def dls_haqida(message: types.Message):
    await message.answer(
        "⚽ *DREAM LEAGUE SOCCER 2026*\n━━━━━━━━━━━━━━━━━━━━\n\n"
        "🌟 Yangi grafika\n⚽ 5000+ real futbolchi\n🏟 Yangi stadionlar\n"
        "🌐 Onlayn multiplayer\n🎫 Season Pass tizimi\n\n"
        "📞 Savollar: @DAVLATOV_5577",
        parse_mode="Markdown", reply_markup=contact_kb()
    )

@dp.message(F.text == "📞 Murojaat")
async def murojaat(message: types.Message):
    await message.answer(
        "📞 *MUROJAAT*\n━━━━━━━━━━━━━━━━━━━━\n\n"
        "👤 Admin: @DAVLATOV_5577\n⏰ 09:00 — 23:00\n📍 Tez javob!",
        parse_mode="Markdown", reply_markup=contact_kb()
    )

@dp.message(F.text == "🏆 Reyting")
async def reyting(message: types.Message):
    await message.answer(
        "🏆 *TOP XARIDORLAR*\n━━━━━━━━━━━━━━━━━━━━\n\n"
        "🥇 1. @user1 — 5 xarid\n🥈 2. @user2 — 4 xarid\n🥉 3. @user3 — 3 xarid\n\n"
        "Ko'proq xarid qiling! 🚀",
        parse_mode="Markdown", reply_markup=main_menu()
    )

@dp.message(Command("admin"))
async def admin_panel(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        await message.answer("❌ Ruxsat yo'q!")
        return
    await message.answer("⚙️ *ADMIN PANEL*", parse_mode="Markdown", reply_markup=admin_panel_kb())

@dp.callback_query(F.data == "admin_update_image")
async def admin_update_image(callback: types.CallbackQuery):
    if callback.from_user.id != ADMIN_ID:
        await callback.answer("❌ Ruxsat yo'q!")
        return
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎫 Season Pass", callback_data="img_season")],
        [InlineKeyboardButton(text="💰 Tanga/Olmos", callback_data="img_tanga_olmos")],
        [InlineKeyboardButton(text="👤 Account #1", callback_data="img_acc_1")],
        [InlineKeyboardButton(text="👤 Account #2", callback_data="img_acc_2")],
        [InlineKeyboardButton(text="👤 Account #3", callback_data="img_acc_3")],
        [InlineKeyboardButton(text="👤 Account #4", callback_data="img_acc_4")],
        [InlineKeyboardButton(text="👤 Account #5", callback_data="img_acc_5")],
        [InlineKeyboardButton(text="👤 Account #6", callback_data="img_acc_6")],
    ])
    await callback.message.answer("Qaysi rasmni yangilamoqchisiz?", reply_markup=kb)
    await callback.answer()

@dp.callback_query(F.data.startswith("img_"))
async def choose_image_key(callback: types.CallbackQuery, state: FSMContext):
    if callback.from_user.id != ADMIN_ID:
        await callback.answer("❌ Ruxsat yo'q!")
        return
    key = callback.data.replace("img_", "")
    await state.update_data(image_key=key)
    await state.set_state(AdminStates.waiting_image)
    await callback.message.answer("Yangi rasmni yuboring:")
    await callback.answer()

@dp.message(AdminStates.waiting_image, F.photo)
async def receive_new_image(message: types.Message, state: FSMContext):
    data = await state.get_data()
    key = data.get("image_key")
    IMAGES[key] = message.photo[-1].file_id
    await message.answer("✅ Rasm saqlandi!")
    await state.clear()

@dp.callback_query(F.data == "admin_stats")
async def admin_stats(callback: types.CallbackQuery):
    await callback.message.answer("📊 Statistika tez orada!")
    await callback.answer()
async def on_startup(app):
    await bot.set_webhook(WEBHOOK_URL)

async def on_shutdown(app):
    await bot.delete_webhook()

async def handle_webhook(request):
    data = await request.json()
    update = types.Update(**data)
    await dp.feed_update(bot, update)
    return web.Response()

async def handle_ping(request):
    return web.Response(text="OK")

def main():
    logging.basicConfig(level=logging.INFO)
    app = web.Application()
    app.router.add_post(WEBHOOK_PATH, handle_webhook)
    app.router.add_get("/", handle_ping)
    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)
    port = int(os.environ.get("PORT", 10000))
    web.run_app(app, host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()
