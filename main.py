import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

user_points = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    if user_id not in user_points:
        user_points[user_id] = 0
    await update.message.reply_text(f"مرحباً! نقاطك الحالية: {user_points[user_id]}")

async def click(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    user_points[user_id] = user_points.get(user_id, 0) + 1
    await update.message.reply_text(f"تم الضغط! نقاطك: {user_points[user_id]}")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("click", click))

    app.run_polling()
