# coding: utf8
from pyrogram.handlers import MessageHandler
import time
from pyrogram import Client,  filters
import logging
import requests
import download
import random
import os
import validation
logging.basicConfig(level=logging.INFO)
bot = Client(
    "ses1",
    api_id=, 
    api_hash="",
  workers = 5, 
  bot_token=''
)



@bot.on_message(filters.command("start", ["!", "/"]))
def connect(chat, m):
	try:
		userID = m.chat.id
		bot.send_message(userID, 'Привет! Я умею скачивать видео из YouTube. Отправь мне ссылку — а я отправлю тебе скачанное видео')
	except Exception as e:
		print(e)


@bot.on_message(filters.text)
def get(chat, m):
	url=m.text	
	userID = m.chat.id
	try:
		VID_ID = ''
		VID_ID = validation.to_valid(url, VID_ID) #валидация регуляркой из validation.py
		bot.send_message(m.chat.id, 'Начинаем загрузку видео...')
		download.worker(VID_ID) #скачивание видео
		bot.send_video(m.chat.id, str(VID_ID) + '.mp4') #отправляем видео пользователю
		os.remove(VID_ID + '.mp4') #удаляем видео на диске в целях жкономии места
	except Exception as e:
		bot.send_message(m.chat.id, f'Что-то пошло не так! Ошибка `{e}`')	


bot.run()	
