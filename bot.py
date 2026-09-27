import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Your High-Power Agent Bot is active on the cloud.")

if __name__ == '__main__':
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        print("Error: TELEGRAM_BOT_TOKEN not found!")
        exit(1)

    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))

    print("Bot is starting polling...")
    app.run_polling()
