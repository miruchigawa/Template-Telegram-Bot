# TELEGRAM BOT
#
# Author: Miftah Fauzan | Erikaanyann
# Version: OpenJk Beta
# Python Version: 3.10.7
# 
# IMPORT MODULES
import telegram.ext
import json
import requests
import logging

json_context = open('config.json')
read_context = json.load(json_context)
TOKEN = read_context['token']

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def start(update, context):
    update.message.reply_text("hello!\nType /help to see all command")
def help(update, context):
    update.message.reply_text("""
    The following commands are available:
    
    /start => To start bot
    /help => See all command available
    /fun => for fun command
    /anime => See all about anime
    """)
def anime(update, context):
    try:
        msg = context.args[0]
        if msg == "help":
            update.message.reply_text("/anime quote => For showing random anime quote")
        elif msg == "quote":
            get_url = requests.get("https://animechan.vercel.app/api/random")
            get_url_content = get_url.json()
            update.message.reply_text(f"""
            RANDOM ANIME QUOTE

Name: {get_url_content['character']}
From: {get_url_content['anime']}
Quote: {get_url_content['quote']}
            """)
        else:
            update.message.reply_text(f"Command {msg} not found! Are you sure?")
    except:
        update.message.reply_text(f"Type /anime help to see about anime command")
def fun(update, context):
    update.message.reply_text("Example")
def handle_message(update, context):
    user = update.message.from_user
    print(f"New Messages received from: {user['username']} Id: {user['id']} Say: {update.message.text}")


updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher


disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("anime", anime))
disp.add_handler(telegram.ext.CommandHandler("fun", fun))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))
updater.start_polling()
updater.idle()
