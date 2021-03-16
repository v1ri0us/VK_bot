import math
import vk_api
import pyowm
from pyowm.commons.exceptions import NotFoundError
from random import randint
from vk_api.longpoll import VkLongPoll , VkEventType
from toks import main_token

vk_session = vk_api.VkApi (token=main_token)
session_api = vk_session.get_api ()
longpoll = VkLongPoll (vk_session)
owm = pyowm.OWM ('4a6c9bbd99e597d23d3969984949314d')


def sender (id , text):
	vk_session.method ('messages.send' , {'user_id': id , 'message': text , 'random_id': 0})


for event in longpoll.listen ():
	if event.type == VkEventType.MESSAGE_NEW:
		if event.to_me:
			msg = event.text.lower ()
			if msg == 'привет':
				id = event.user_id
				sender (id , "@id" + str (
					id) + "(Дружище), приветствую тебя! Чем могу помочь? \n (Доступные команды: помощь, калькулятор, погода)")
			elif msg == 'старт':
				id = event.user_id
				sender (id , "@id" + str (
					id) + "(Дружище), приветствую тебя! Чем могу помочь? \n (Доступные команды: помощь, калькулятор, погода)")
			elif msg == 'начать':
				id = event.user_id
				sender (id , "@id" + str (
					id) + "(Дружище), приветствую тебя! Чем могу помочь? \n (Доступные команды: помощь, калькулятор, погода)")
			elif msg == 'хай':
				id = event.user_id
				sender (id , "@id" + str (
					id) + "(Дружище), хаюшки! Чем могу помочь? \n (Доступные команды: помощь, калькулятор, погода)")
			elif msg == 'йо':
				id = event.user_id
				sender (id , "@id" + str (
					id) + "(Дружище), йо! Чем могу помочь? \n (Доступные команды: помощь, калькулятор, погода)")
			elif msg == 'дарова':
				id = event.user_id
				sender (id , "@id" + str (
					id) + "(Дружище), здоровеньки булы! Чем могу помочь? \n (Доступные команды: помощь, калькулятор, погода)")
			elif msg == 'помощь':
				id = event.user_id
				sender (id , "@id" + str (id) + "(Доступные команды: помощь, калькулятор, погода")
			if msg == 'калькулятор':
				id = event.user_id
				sender (id , "Запускаю калькулятор. Введи первое число!")
				user_input = []
				for event in longpoll.listen ():
					if event.type == VkEventType.MESSAGE_NEW:
						if event.to_me:
							msg = event.text.lower ()
							user_input.append (msg)
							sender (id , "Отлично. Введи второе число!")
							break
				for event in longpoll.listen ():
					if event.type == VkEventType.MESSAGE_NEW:
						if event.to_me:
							msg = event.text.lower ()
							user_input.append (msg)
							sender (id , "Теперь ввведи арифметическое действие(+, -, /, *)")
							break
				for event in longpoll.listen ():
					if event.type == VkEventType.MESSAGE_NEW:
						if event.to_me:
							msg = event.text.lower ()
							user_input.append (msg)
							break
				n1 = user_input[0]
				n2 = user_input[1]
				act = user_input[2]
				try:
					a = float (n1)
					b = float (n2)

					if act == '+':
						answer = a + b
						sender (id , 'Твой ответ: ' + str (answer))

					elif act == '-':
						answer = a - b
						sender (id , 'Твой ответ: ' + str (answer))

					elif act == '/':
						answer = a / b
						sender (id , 'Твой ответ: ' + str (answer))
					elif act == '*':
						answer = a * b
						sender (id , 'Твой ответ: ' + str (answer))
					else:
						sender(id, 'Ты ввел недопустимое действие. Попробуй снова!')
				except Exception:
					id = event.user_id
					sender (id , "Произошла ошибка при вычислениях!>.< \n Попробуй ввести числа снова!")
			if msg == 'погода':
				id = event.user_id
				sender (id , "@id" + str (id) + '(Назови) город, который тебе нужен!')
				for event in longpoll.listen ():
					if event.type == VkEventType.MESSAGE_NEW:
						if event.to_me:
							place = event.text.lower ()
							mgr = owm.weather_manager ()
							try:
								observation = mgr.weather_at_place (place)
								w = observation.weather
								temperature = w.temperature ('celsius')['temp']
								temp = math.floor (temperature)
								sender (id , "@id" + str (id) + "(Смотри), в городе " + place.title () + " сейчас: " + str (temp) + " по Цельсию!")
								break
							except NotFoundError:
								id = event.user_id
								sender (id , "Ошибка при поиске места!>.<")
								break
	continue

							
				