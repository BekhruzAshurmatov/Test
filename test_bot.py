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
