import discord
from discord.ext import commands
from discord.utils import get
import os
import asyncio
from datetime import Uptime
from captcha.image import ImageCaptcha
import random
import datetime
import urllib
from urllib.request import Request
import bs4
from urllib.request import URLError
from urllib.request import HTTPError
from urllib.request import urlopen
from urllib.request import Request, urlopen
from urllib.request import quote
from bs4 import BeautifulSoup
from urllib import parse
import warnings
import requests
import json
import re
import openpyxl
import koreanbots
import os, random, time

client = discord.Client()

@client.event
async def on_ready():
    print('봇이 로그인 하였습니다.')
    print(' ')
    print('닉네임 : {}'.format(client.user.name))
    print('아이디 : {}'.format(client.user.id))
    while True:
        user = len(client.users)
        server = len(client.guilds)
        messages = ["제 접두사는 / 입니다!", "건의는 ∑」Greencookie#3907 또는 ∑」바나나#1234 에게 해주세요!" , "저는 SKY BOT TEAM 에서 개발, 관리되고 있어요!" , str(user) + "분의 디스코드를 함께하고 있어요!", str(server) + "개의 서버에 있다구요!"]
        for (m) in range(5):
            await client.change_presence(status=discord.Status.online, activity=discord.Activity(name=messages[(m)], type=discord.ActivityType.watching))
            await asyncio.sleep(4)

@client.event
async def on_message(message):
