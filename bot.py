#1 - импорт Updater
#2 - тело бота
from telegram.ext import Updater


def main():
	mybot = Updater("777086407:AAE32a5z9xeQHfJTvqHeB1fOyoxg-pmtB-o") # ключ от нашего бота, полученный от botFather
	mybot.start_polling() # активация бота для считвания сообщений
	mybot.idle()  # mybot работает до принудительной остановки
