import telebot
import os
from telebot import types

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8192598977:AAEX4eykCxTZTJ4R1PqB0kYs5wmq1lsPdw4")
ADMIN_ID = 6470396397

bot = telebot.TeleBot(BOT_TOKEN)

IMAGES = {
   "season": None, "tanga_olmos": None,
   "acc_1": None, "acc_2": None, "acc_3": None,
   "acc_4": None, "acc_5": None, "acc_6": None,
   "sariq": None,
}

users = set()
waiting_image_key = {}
waiting_broadcast = set()

def main_menu():
   kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
   kb.add(types.KeyboardButton("🎫 Season Pass"), types.KeyboardButton("💰 Tanga & Olmos"))
   kb.add(types.KeyboardButton("👤 Accountlar"), types.KeyboardButton("⭐ Sariq Oyinchilar"))
   kb.add(types.KeyboardButton("ℹ️ DLS26 Haqida"), types.KeyboardButton("📞 Murojaat"))
   kb.add(types.KeyboardButton("🏆 Reyting"))
   return kb

def contact_kb():
   kb = types.InlineKeyboardMarkup()
   kb.add(types.InlineKeyboardButton("📩 @DAVLATOV_5577", url="https://t.me/DAVLATOV_5577"))
   return kb

def admin_kb():
   kb = types.InlineKeyboardMarkup()
   kb.add(types.InlineKeyboardButton("🖼 Rasm yangilash", callback_data="admin_image"))
   kb.add(types.InlineKeyboardButton("📢 E'lon yuborish", callback_data="admin_broadcast"))
   kb.add(types.InlineKeyboardButton("📊 Statistika", callback_data="admin_stats"))
   return kb

@bot.message_handler(commands=["start"])
def start(message):
   users.add(message.from_user.id)
   bot.send_message(message.chat.id,
       "🎮 *DLS 26 — Rasmiy Bot*\n\n"
       "⚠ *Majburiy obuna:* @DLS_UZB_UZB kanaliga a'zo bo'ling!\n\n"
       "Assalomu alaykum! Xush kelibsiz! 👋",
       parse_mode="Markdown", 
       reply_markup=types.InlineKeyboardMarkup().add(
           types.InlineKeyboardButton("📢 Kanalga a'zo bo'lish", url="https://t.me/DLS_UZB_UZB")
       ).add(types.KeyboardButton("✅ Davom ettirish")))
   bot.register_next_step_handler(message, main_menu_send)

def main_menu_send(message):
   if message.text == "✅ Davom ettirish":
       bot.send_message(message.chat.id,
           "🎮 *DLS 26 — Rasmiy Bot*\n\nQuyidagi bo'limlardan birini tanlang 👇",
           parse_mode="Markdown", reply_markup=main_menu())
   else:
       bot.send_message(message.chat.id, "❌ Iltimos, tugmani bosing!")

@bot.message_handler(func=lambda m: m.text == "🎫 Season Pass")
def season_pass(message):
   text = ("🎫 *DLS 26 — SEASON PASS*\n━━━━━━━━━━━━━━━━━━━━\n\n"
       "🔥 *AKSIYALI:* 25,000 so'm\n💎 *AKSIYASIZ:* 40,000 so'm\n\n"
       "📞 Sotib olish uchun adminga murojaat!")
   if IMAGES["season"]:
       bot.send_photo(message.chat.id, IMAGES["season"], caption=text, parse_mode="Markdown", reply_markup=contact_kb())
   else:
       bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=contact_kb())

@bot.message_handler(func=lambda m: m.text == "💰 Tanga & Olmos")
def tanga_olmos(message):
   text = ("💰 *TANGA & OLMOS NARXLARI*\n━━━━━━━━━━━━━━━━━━━━\n\n"
       "🥉 *80,000 so'm*\n🪙 40k Tanga | 💎 1,000 Olmos | ⏰ 5-6 kun | 👤 1 Classic\n\n"
       "🥈 *150,000 so'm*\n🪙 90k Tanga | 💎 2,000 Olmos | ⏰ 10-12 kun | 👤 2 Classic\n\n"
       "🥇 *300,000 so'm*\n🪙 180k Tanga | 💎 4,500 Olmos | ⏰ 22-24 kun | 👤 3 Classic\n\n"
       "💠 *400,000 so'm*\n🪙 300k Tanga | 💎 6,500 Olmos | ⏰ 33-36 kun | 👤 4 Classic\n\n"
       "🔷 *600,000 so'm*\n🪙 400k Tanga | 💎 8,000 Olmos | ⏰ 45-50 kun | 👤 4 Classic\n\n"
       "👑 *700,000 so'm*\n🪙 500k Tanga | 💎 10,000 Olmos | ⏰ 62 kun | 👤 4 Classic\n\n"
       "📞 Buyurtma uchun adminga murojaat!")
   if IMAGES["tanga_olmos"]:
       bot.send_photo(message.chat.id, IMAGES["tanga_olmos"], caption=text, parse_mode="Markdown", reply_markup=contact_kb())
   else:
       bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=contact_kb())

@bot.message_handler(func=lambda m: m.text == "👤 Accountlar")
def accountlar(message):
   kb = types.InlineKeyboardMarkup()
   kb.add(types.InlineKeyboardButton("🔴 Account #1", callback_data="acc_1"))
   kb.add(types.InlineKeyboardButton("🟠 Account #2", callback_data="acc_2"))
   kb.add(types.InlineKeyboardButton("🟡 Account #3", callback_data="acc_3"))
   kb.add(types.InlineKeyboardButton("🟢 Account #4", callback_data="acc_4"))
   kb.add(types.InlineKeyboardButton("🔵 Account #5", callback_data="acc_5"))
   kb.add(types.InlineKeyboardButton("🟣 Account #6", callback_data="acc_6"))
   kb.add(types.InlineKeyboardButton("📩 Admin", url="https://t.me/DAVLATOV_5577"))
   bot.send_message(message.chat.id, "👤 *ACCOUNTLAR*\nBirini tanlang 👇", parse_mode="Markdown", reply_markup=kb)

@bot.callback_query_handler(func=lambda c: c.data.startswith("acc_"))
def account_detail(call):
   img = IMAGES.get(call.data)
   text = f"👤 *Account #{call.data[-1]}*\n\n📞 Narx uchun adminga murojaat!"
   kb = types.InlineKeyboardMarkup()
   kb.add(types.InlineKeyboardButton("📩 Admin", url="https://t.me/DAVLATOV_5577"))
   if img:
       bot.send_photo(call.message.chat.id, img, caption=text, parse_mode="Markdown", reply_markup=kb)
   else:
       bot.send_message(call.message.chat.id, text, parse_mode="Markdown", reply_markup=kb)
   bot.answer_callback_query(call.id)

@bot.message_handler(func=lambda m: m.text == "⭐ Sariq Oyinchilar")
def sariq_oyinchilar(message):
   text = ("⭐ *DLS 26 — SARIQ OYINCHILAR*\n━━━━━━━━━━━━━━━━━━━━\n\n"
       "🌟 Eng yaxshi sariq oyinchilar!\n\n"
       "📞 Batafsil ma'lumot uchun adminga murojaat!")
   if IMAGES["sariq"]:
       bot.send_photo(message.chat.id, IMAGES["sariq"], caption=text, parse_mode="Markdown", reply_markup=contact_kb())
   else:
       bot.send_message(message.chat.id, text, parse_mode="Markdown", reply_markup=contact_kb())

@bot.message_handler(func=lambda m: m.text == "ℹ️ DLS26 Haqida")
def dls_haqida(message):
   bot.send_message(message.chat.id,
       "⚽ *DREAM LEAGUE SOCCER 2026*\n━━━━━━━━━━━━━━━━━━━━\n\n"
       "🌟 Yangi grafika\n⚽ 5000+ futbolchi\n🏟 Yangi stadionlar\n"
       "🌐 Onlayn multiplayer\n🎫 Season Pass\n\n📞 @DAVLATOV_5577",
       parse_mode="Markdown", reply_markup=contact_kb())

@bot.message_handler(func=lambda m: m.text == "📞 Murojaat")
def murojaat(message):
   bot.send_message(message.chat.id,
       "📞 *MUROJAAT*\n━━━━━━━━━━━━━━━━━━━━\n\n"
       "👤 Admin: @DAVLATOV_5577\n⏰ 09:00 — 23:00\n📍 Tez javob!",
       parse_mode="Markdown", reply_markup=contact_kb())

@bot.message_handler(func=lambda m: m.text == "🏆 Reyting")
def reyting(message):
   bot.send_message(message.chat.id,
       "🏆 *TOP XARIDORLAR*\n━━━━━━━━━━━━━━━━━━━━\n\n"
       "🥇 1. @user1 — 5 xarid\n🥈 2. @user2 — 4 xarid\n🥉 3. @user3 — 3 xarid",
       parse_mode="Markdown", reply_markup=main_menu())

@bot.message_handler(commands=["admin"])
def admin_panel(message):
   if message.from_user.id != ADMIN_ID:
       bot.send_message(message.chat.id, "❌ Ruxsat yo'q!")
       return
   bot.send_message(message.chat.id, "⚙️ *ADMIN PANEL*", parse_mode="Markdown", reply_markup=admin_kb())

@bot.callback_query_handler(func=lambda c: c.data == "admin_stats")
def admin_stats(call):
   if call.from_user.id != ADMIN_ID:
       bot.answer_callback_query(call.id, "❌ Ruxsat yo'q!")
       return
   bot.send_message(call.message.chat.id,
       f"📊 *STATISTIKA*\n\n👥 Foydalanuvchilar: {len(users)} ta",
       parse_mode="Markdown")
   bot.answer_callback_query(call.id)

@bot.callback_query_handler(func=lambda c: c.data == "admin_broadcast")
def admin_broadcast(call):
   if call.from_user.id != ADMIN_ID:
       bot.answer_callback_query(call.id, "❌ Ruxsat yo'q!")
       return
   waiting_broadcast.add(call.from_user.id)
   bot.send_message(call.message.chat.id, "📢 E'lon matnini yuboring:")
   bot.answer_callback_query(call.id)

@bot.callback_query_handler(func=lambda c: c.data == "admin_image")
def admin_image(call):
   if call.from_user.id != ADMIN_ID:
       bot.answer_callback_query(call.id, "❌ Ruxsat yo'q!")
       return
   kb = types.InlineKeyboardMarkup()
   kb.add(types.InlineKeyboardButton("🎫 Season Pass", callback_data="img_season"))
   kb.add(types.InlineKeyboardButton("💰 Tanga/Olmos", callback_data="img_tanga_olmos"))
   kb.add(types.InlineKeyboardButton("⭐ Sariq Oyinchilar", callback_data="img_sariq"))
   kb.add(types.InlineKeyboardButton("👤 Account #1", callback_data="img_acc_1"))
   kb.add(types.InlineKeyboardButton("👤 Account #2", callback_data="img_acc_2"))
   kb.add(types.InlineKeyboardButton("👤 Account #3", callback_data="img_acc_3"))
   kb.add(types.InlineKeyboardButton("👤 Account #4", callback_data="img_acc_4"))
   kb.add(types.InlineKeyboardButton("👤 Account #5", callback_data="img_acc_5"))
   kb.add(types.InlineKeyboardButton("👤 Account #6", callback_data="img_acc_6"))
   bot.send_message(call.message.chat.id, "Qaysi rasmni yangilamoqchisiz?", reply_markup=kb)
   bot.answer_callback_query(call.id)

@bot.callback_query_handler(func=lambda c: c.data.startswith("img_"))
def choose_image(call):
   if call.from_user.id != ADMIN_ID:
       bot.answer_callback_query(call.id, "❌ Ruxsat yo'q!")
       return
   key = call.data.replace("img_", "")
   waiting_image_key[call.from_user.id] = key
   bot.send_message(call.message.chat.id, "Yangi rasmni yuboring:")
   bot.answer_callback_query(call.id)

@bot.message_handler(content_types=["photo"])
def save_image(message):
   if message.from_user.id in waiting_image_key:
       key = waiting_image_key.pop(message.from_user.id)
       IMAGES[key] = message.photo[-1].file_id
       bot.send_message(message.chat.id, "✅ Rasm saqlandi!")
   elif message.from_user.id in waiting_broadcast:
       waiting_broadcast.discard(message.from_user.id)
       count = 0
       for uid in users:
           try:
               bot.copy_message(uid, message.chat.id, message.message_id)
               count += 1
           except:
               pass
       bot.send_message(message.chat.id, f"✅ E'lon {count} ta foydalanuvchiga yuborildi!")

@bot.message_handler(content_types=["text"])
def broadcast_handler(message):
   if message.from_user.id in waiting_broadcast:
       waiting_broadcast.discard(message.from_user.id)
       count = 0
       for uid in users:
           try:
               bot.send_message(uid, message.text, parse_mode="Markdown")
               count += 1
           except:
               pass
       bot.send_message(message.chat.id, f"✅ E'lon {count} ta foydalanuvchiga yuborildi!")

print("✅ DLS26 Bot ishga tushdi!")
bot.infinity_polling()
