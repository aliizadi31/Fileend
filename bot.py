import telebot

# توکن واقعی ربات
TOKEN = '7790176814:AAGmyznBhxqB7_jzpcnT4KCgEx1X5rCLSpE'

# ساخت ربات
bot = telebot.TeleBot(TOKEN)

# هندلر شروع
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! ربات حرفه‌ای تحلیل ارز دیجیتال فعال شد.")

# اجرای همیشگی ربات
bot.infinity_polling()
