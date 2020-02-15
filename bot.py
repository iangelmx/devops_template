import telebot
import requests
import json
import datetime
import json
import os

TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
	chat_id = message.from_user.id
	action_string = 'typing'
	bot.send_chat_action(chat_id, action_string)

	jsonMessage = message.json
	#for key in jsonMessage:
	#	print("jsonMessage[",key,"] :",jsonMessage[key])

	bot.reply_to(message, "Ahora digo otra cosa...")

@bot.message_handler(content_types=['location'])
def recibeUbicacion(message):
	chat_id = message.from_user.id
	
	action_string = 'typing'
	bot.send_chat_action(chat_id, action_string)
	print("Recibí una ubicación")
	print(message)

	mensaje="mensaje de prueba"
	
	bot.send_message(message.from_user.id, mensaje,  parse_mode='HTML')

	msg = "mensaje de prueba"
	
    #bot.send_message(telegram_id_user, "cadena de texto a enviar...", parse_mode='HTML')
	bot.send_message(message.from_user.id, msg,  parse_mode='HTML')
	
	bot.send_contact(message.from_user.id, phone_number="+525555555555", first_name="Ejemplo" )
	
	bot.send_location(message.from_user.id, latitude=0, longitude=0)

	
@bot.message_handler(commands=['comando'])
def comando(message):
	chat_id = message.from_user.id
	
	action_string = 'typing'
	bot.send_chat_action(chat_id, action_string)

	msg = "Comando..."
	print( message )

	bot.send_message(message.from_user.id, msg,  parse_mode='HTML')

#@bot.message_handler(func=lambda message: True) #First
@bot.message_handler(content_types=['voice']) #Evolución para notas de voz
@bot.message_handler(func=lambda m: True) #Evolución para notas de voz
def echo_all(message):
	global last, lastMessage
	chat_id = message.from_user.id
	now = datetime.datetime.now()
	
	action_string = 'typing'
	bot.send_chat_action(chat_id, action_string)

	if message.voice is not None:
		print("Es un audio")
		id_voice_note = message.voice.file_id
		file = bot.get_file(id_voice_note)
		#print( 'file.file_path =', file.file_path)
		downloaded_file = bot.download_file(file.file_path)
		nombre = str(chat_id)+"_"+now.strftime("%Y.%m.%d_%H.%M")
		
		formato_audio = 'ogg'
		file_path_sys = f"./voice_notes/{nombre}.{formato_audio}"

		with open(file_path_sys, 'wb') as new_file:
			new_file.write(downloaded_file)
        
        #Se guardó el archivo...


	jsonMessage = message.json

	mensaje_transcrito = "Mensaje..."
	
	bot.send_message(message.from_user.id, mensaje_transcrito, parse_mode='HTML')


def makeForm( form ):
	if len(form)>0:
		from telebot import types

		# Using the ReplyKeyboardMarkup class
		# It's constructor can take the following optional arguments:
		# - resize_keyboard: True/False (default False)
		# - one_time_keyboard: True/False (default False)
		# - selective: True/False (default False)
		# - row_width: integer (default 3)
		# row_width is used in combination with the add() function.
		# It defines how many buttons are fit on each row before continuing on the next row.
		markup = types.ReplyKeyboardMarkup(row_width=2)
		items_btn = []
		for texto_boton in form:
			boton = types.KeyboardButton( str(texto_boton) ) 
			markup.add(boton)

		return markup
	return None


bot.polling()

while True: # Don't let the main Thread end.
	pass

