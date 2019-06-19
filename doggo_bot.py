from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re

def get_url_imageAPI():
    contents = requests.get('https://random.dog/woof.json').json()	#API
    url = contents['url']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url_image()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

def get_url_factAPI():
	



def woof(bot, update):	#request for image
    url = get_image_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def fact(bot, update):	#request for video
	url = get_fact_url()
	chat_id = update.message.chat_id
	bot.send_fact(chat_id=chat_id, fact=url)

def main():
    updater = Updater('723455293:AAGckXg1oR6k61GBWVEJeMM9lk3vjnDBdHY')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('woof', woof))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()