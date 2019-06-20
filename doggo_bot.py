from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re

def get_url_dog():
    contents = requests.get('https://random.dog/woof.json').json()	#API dog
    url_dog = contents['url']
    return url_dog

def get_image_url_dog():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url_dog = get_url_dog()
        file_extension = re.search("([^.]*)$",url_dog).group(1).lower()
    return url_dog

def woof(bot, update):	#request for dog image
    url_dog = get_image_url_dog()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url_dog)

def get_url_cat():
	urlCAT = 'https://api.thecatapi.com/v1/images/search?format=json'
	payload = {}
	headers = {
	  'Content-Type': 'application/json',
	  'x-api-key': '06d76875-b54b-4bab-b2ec-e561e6bdf3e1'
	}
	response = requests.request('GET', url)
	data = json.loads(response.text)	#list
	for i in data:    
		url_cat = i["url"]	#dict
	print(url_cat)
	return url_cat

def get_image_url_cat():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url_cat = get_url_cat()
        file_extension = re.search("([^.]*)$",url_cat).group(1).lower()
    return url_cat

def purr(bot, update):	#request for cat image
	url_cat = get_url_cat()
	chat_id = update.message.chat_id
	bot.send_photo(chat_id=chat_id, photo=url_cat)

def main():
    updater = Updater('723455293:AAGckXg1oR6k61GBWVEJeMM9lk3vjnDBdHY')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('woof', woof))
    dp.add_handler(CommandHandler('purr', purr))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()