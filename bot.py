#1 - импорт Updater
#2 - тело бота, объявление функции
#3 - объявление прокси
#4 - вложение прокси в переменную mybot
#5 - import CommandHandler
#6 - объявление функции greet_user для отслеживания откликов бота
#7 - учим бота отвечать через 	update.message.reply_text(). теперь бот посылает нам сообщение из переменной text и в консоли, и в чате при исполнении add_handler
#8 - import logging
#9 - базовая конфигурации logging
#10 - импорт MessageHandler - обработка ботом сообщений и Filters - фильтр для выбора типов сообщений с которыми бот работает( тест, фото, видео, аудио)
#11 - объявление функции talk_to_me, которая возвращает сообщение пользователю
from glob import glob
import logging
from random import choice

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 	#?настройка logging, указываем формат лога (время и дата события, имя файла в котором произошло событие, уровень важности события, сообщение  событии)
                    level=logging.INFO,  											#? уровень логирования INFO - для получения информационных сообщений уровня info, warnig и error
										filename='bot.log') 						#? название файла жернала logging в котором будут отражены все события



def greet_user(bot, update):
	text = 'Вызван /start'
	print(text)
	update.message.reply_text(text) # обновление текста сообщения и вывод его в консоль, в данном случае текст помещенный в переменную text


def talk_to_me(bot, update):
	user_text = "Hello {}! You wrote: {}".format(update.message.chat.first_name, update.message.text) #переменная в которой лежит сообщение пользователя, включаем шаблон сообщения бота, которое будет вовзвращаться пользователю, с именем пользователя
	logging.info("User: %s, Chat id: %s, Message: %s, First_name: %s", update.message.chat.username, 
              update.message.chat.id, update.message.text, update.message.chat.first_name)  # возврат данных в лог username, id чата, сообщение
	# print(update.message)  # update.message возвращает в консоль данные пользователя и сообщение
	update.message.reply_text(user_text) # отправление текста пользователя в чат с пользователем и в консоль


def send_dog_pict(bot, update):
	dog_list = glob('img/*dog*.jp*g')
	dog_pic = choice(dog_list)
	bot.send_photo(chat_id=update.message.chat.id, photo=open(dog_pic, 'rb'))


def send_cat_pict(bot, update):
	cat_list = glob('img/*cat*.jp*g')
	cat_pic = choice(cat_list)
	bot.send_photo(chat_id=update.message.chat.id, photo=open(cat_pic, 'rb'))


def main():
	mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY) # ключ от нашего бота, полученный от botFather //#переменной mubot дополнительно передаем PROXY как параметр
	
	logging.info('Bot starting') #первое сообщение для журнала

	dp = mybot.dispatcher # объявляем переменную dp для сокращения написания команд add_hadler
	dp.add_handler(CommandHandler('start', greet_user)) #Handler'ы выполняются в порядке расположения(вызова)
	dp.add_handler(CommandHandler('dog', send_dog_pict))
	dp.add_handler(CommandHandler('cat', send_cat_pict))
	dp.add_handler(MessageHandler(Filters.text, talk_to_me))  # add_handler для MessageHandler, устанавливаем фильтр для текста и производим вызов функции talk_to_me. #!MessageHandler должен быть последним Hendler'ом
	
	mybot.start_polling() # активация бота для считвания сообщений
	mybot.idle()  # mybot работает до принудительной остановки

main() # вызов функции