from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from chatbot.faq_responses import generate_response

def start(update, context):
    update.message.reply_text("Hi! I'm your chatbot. Ask me anything.")

def handle_message(update, context):
    user_message = update.message.text
    bot_reply = generate_response(user_message)
    update.message.reply_text(bot_reply)

def main():
    updater = Updater("YOUR_TELEGRAM_BOT_TOKEN", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
