import telebot
from telebot import types

TOKEN = "8427762306:AAHyHEeH-xZhnuQvj4raZ2gNkPtDBT6y8wc"
ADMIN = "@emiryildiz63"
KANAL = "@tj65J7be_7M4MjI0"

bot = telebot.TeleBot(TOKEN)
users = {}

def check_user(user_id):
    if user_id not in users:
        users[user_id] = {"ref": 0}

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    check_user(user_id)

    args = message.text.split()
    if len(args) > 1:
        try:
            ref_id = int(args[1])
            if ref_id != user_id:
                check_user(ref_id)
                users[ref_id]["ref"] += 1
        except:
            pass

    bot.send_message(user_id,
        "👋 Hoş geldin!\n\n"
        "📢 Botu kullanmak için kanala katıl:\n"
        "👉 https://t.me/+tj65J7be_7M4MjI0\n\n"
        "Sonra /menu yaz"
    )

@bot.message_handler(commands=['menu'])
def menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🎮 PUBG Hesap", "🚗 Car Parking")
    markup.add("🎁 Gizli Hediye", "📊 Referansım")
    bot.send_message(message.chat.id, "🛒 Market:", reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def market(message):
    user_id = message.from_user.id
    check_user(user_id)
    ref = users[user_id]["ref"]

    if message.text == "📊 Referansım":
        bot.send_message(user_id, f"👥 Referansın: {ref}\n🔗 Linkin:\nhttps://t.me/{bot.get_me().username}?start={user_id}")

    elif message.text == "🎮 PUBG Hesap":
        if ref >= 3:
            bot.send_message(user_id,
                "✅ PUBG Hesap almaya hak kazandın!\n\n"
                f"📩 Admine yaz: {ADMIN}\n"
                "🧾 Hesabı aldıktan sonra SS atmayı unutma."
            )
        else:
            bot.send_message(user_id, f"❌ 3 referans lazım. Senin: {ref}")

    elif message.text == "🚗 Car Parking":
        if ref >= 5:
            bot.send_message(user_id,
                "✅ Car Parking Hesap almaya hak kazandın!\n\n"
                f"📩 Admine yaz: {ADMIN}\n"
                "🧾 Hesabı aldıktan sonra SS atmayı unutma."
            )
        else:
            bot.send_message(user_id, f"❌ 5 referans lazım. Senin: {ref}")

    elif message.text == "🎁 Gizli Hediye":
        if ref >= 10:
            bot.send_message(user_id,
                "🎉 Gizli Hediyeyi kazandın!\n\n"
                f"📩 Detay için admine yaz: {ADMIN}\n"
                "🧾 SS atman zorunludur."
            )
        else:
            bot.send_message(user_id, f"❌ 10 referans lazım. Senin: {ref}")

bot.infinity_polling()
