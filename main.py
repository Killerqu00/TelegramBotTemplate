import json
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import logging

from commands.EchoCommand import EchoCommand

from telegram import Update

with open("creds.json", "r") as f:
    TOKEN = json.loads(f.read())["token"]


if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, EchoCommand))
    app.run_polling(allowed_updates=Update.ALL_TYPES)
    