import os

import telegram

# enviroment variable: TOKEN=389264369:AAH5hHTN7sr7cQIf5GljTD4jtx4CjB5Q6Mg
def hg_function(request):
    bot = telegram.Bot(token=os.environ["TOKEN"])
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        chat_id = update.message.chat.id
        # Reply with the same message
        bot.sendMessage(chat_id=chat_id, text="HG-11 says: " + update.message.text)
    return "test ok"