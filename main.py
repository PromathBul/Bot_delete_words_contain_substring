from telegram import Bot
from telegram.ext import Updater, CommandHandler

bot = Bot(token = '')
updater = Updater(token = '')
dispatcher = updater.dispatcher
   

def delete_words(update, context):
    string = update.message.text
    context.bot.send_message(update.effective_chat.id, f"{' '.join(filter(lambda word: 'абв' not in word.lower(), string.split()))}")

start_handler = CommandHandler("start", delete_words)

dispatcher.add_handler(start_handler)

updater.start_polling()
updater.idle()