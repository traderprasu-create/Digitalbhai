import telebot
from telebot import types

BOT_TOKEN = "8420413028:AAGKCQc2maPamZUbcMESp2NSyNRNakOBcN0"

bot = telebot.TeleBot(BOT_TOKEN)

APK_FILE = "app.apk"        # APK file name
VOICE_FILE = "voice.mp3"    # Voice file name

@bot.chat_join_request_handler()
def handle_join_request(join_request):
    try:
        user = join_request.from_user

        # Hello Message
        bot.send_message(
            user.id,
            f"Hello 👋 {user.first_name}"
        )

        # Channel Button
        markup = types.InlineKeyboardMarkup()
        markup.add(
            types.InlineKeyboardButton(
                "💚 VIP CHANNEL",
                url="https://t.me/+PLPLQSMksXo4MmU1"
            )
        )

        # APK File
        with open(APK_FILE, "rb") as apk:
            bot.send_document(
                user.id,
                apk,
                caption="""𝙎𝙋𝙀𝘾𝙄𝘼𝙇 𝙉𝙐𝙈𝘽𝙀𝙍 𝙎𝙐𝙍𝙀𝙎𝙃𝙊𝙏
𝙇𝙊𝙎𝙎 𝙍𝙀𝘾𝙊𝙑𝙀𝙍𝙔 𝙃𝘼𝘾𝙆
𝗡𝗨𝗠𝗕𝗘𝗥 𝗛𝗔𝗖𝗞

𝘿𝙀𝙋𝙊𝙎𝙄𝙏 200 𝙏𝙃𝙀𝙉 𝙃𝘼𝘾𝙆 𝙒𝙊𝙍𝙆𝙄𝙉𝙂
• 100% 𝙒𝙄𝙉𝙂𝙊 𝙎𝙐𝙍𝙀 𝙎𝙃𝙊𝙏

𝙮𝙖𝙖𝙧 𝙬𝙞𝙣 𝗦𝗨𝗥𝗘𝗦𝗛𝗢𝗧 𝗣𝗔𝗡𝗘𝗟""",
                reply_markup=markup
            )

        # Voice Message
        with open(VOICE_FILE, "rb") as voice:
            bot.send_audio(
                user.id,
                voice,
                caption="🔊 𝙎𝘼𝘽 𝙇𝙊𝙂 𝙎𝙐𝙉𝙊.....❤️❤️",
                reply_markup=markup
            )

    except Exception as e:
        print("Error:", e)

print("Bot Running...")
bot.infinity_polling()