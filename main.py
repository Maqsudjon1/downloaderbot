from requests import *
from telegram import *
from telegram.ext import *

TOKEN = "6591099248:AAH8FAMtsbaz8AdFyorR1DSWSDoRpq0aXjY"

RANDOM_IMAGE = "Random image"
GET_MP3 = "Get mp3"
RANDOM_IMG_URL = "https://picsum.photos/120B"

global IMAGE_COUNTER
IMAGE_COUNTER = 0

print('Running up the bot....')