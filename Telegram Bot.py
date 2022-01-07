import requests

import re

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import json

updater = Updater(token='5067980534:AAF7u8F6lvDTftiCki2Wgs7AeTqA2ENbP2s', use_context = True)

dispatcher = updater.dispatcher

updater.start_polling()

def summary(update, context):
    response = requests.get('https://api.covid19api.com/summary')
    if (response.status_code == 200):
        data = response.json()
        date = data['Date'][:10]
        ans = f"Covid 19 Summary (as of {date}): \n";

        for attribute, value in data['Global'].items():
            if attribute not in ['NewConfirmed', 'NewDeaths', 'NewRecovered']:
                ans += 'Total ' + attribute[5::].lower() + " : " + str(value) + "\n"
        
        print(ans)
        context.bot.send_message(chat_id = update.effective_chat.id, text = ans)

    else:
        context.bot.send_message(chat_id = update.effective_chat.id, text = "Error, something went wrong")

corona_summary_handler = CommandHandler('summary', summary)
dispatcher.add_handler(corona_summary_handler)
