from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = "7555855256:AAHfTwjfkEaPz3Z89RBD41Q5Y-i5lEGyHms"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Бот успешно запущен! Пришлите фото или видео для анализа.")

def handle_photo(update: Update, context: CallbackContext):
    update.message.reply_text("Получено фото! Обработка...")

def handle_video(update: Update, context: CallbackContext):
    update.message.reply_text("Получено видео! Обработка...")

def main():
    updater = Updater(7555855256:AAHfTwjfkEaPz3Z89RBD41Q5Y-i5lEGyHms,use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.photo, handle_photo))
    dp.add_handler(MessageHandler(Filters.video, handle_video))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
