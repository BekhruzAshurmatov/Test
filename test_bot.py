from aiogram import Bot, Dispatcher, types
import asyncio
from random import randint
import importlib
import os
import requests

Token = '7985683028:AAG6RIzih8Rh5_kubPPq-e_xeum75z-R-3U'
channel = ''

bot = Bot(token=Token)
dp = Dispatcher()

user_data = {}
project_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(project_dir, 'images')



email = 'bekhruzashurmatov1@gmail.com'
password = 'ElwGZZg0d4ja2b6BDyuQQNs4bJeMn0calvdmGZtV'

async def eskiz_login(email, password):
    url = "https://notify.eskiz.uz/api/auth/login"
    payload = {'email': email,
               'password': password}
    files = []
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    print(response.text)
    token = response.json()['data']['token']
    return token

    print('Привет Мир!')
