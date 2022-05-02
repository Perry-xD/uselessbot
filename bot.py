from pyrogram import filters, Client as c
from pyrogram.types import Message

import os
import json
import requests
from requests.structures import CaseInsensitiveDict






API_ID = 11392764 #os.environ.get('API_ID')
API_HASH = 'fc83fc5ae9c699cc5356aec7de6773ae' #os.environ.get('API_HASH')
BOT_TOKEN = '5225227620:AAGPMfMRS-y7gTvZrb0xjZzT6C8y88rWWC0' #os.environ.get('BOT_TOKEN')

god = c("godboyx", API_ID, API_HASH, BOT_TOKEN)

@god.on_message(filters.command('start', '/') & filters.private)
async def starting(_, m: Message):
    await god.send_message(m.chat.id, 'hello sir just the command /link to get the live class link')

@god.on_message(filters.command('link', '/') & filters.private)
async def starting(_, m: Message):
    try:
        url = "https://api.penpencil.xyz/v1/batches/621c5167a592f502085b0878/todays-schedule"
        headers = CaseInsensitiveDict()
        headers["Authorization"] = "Bearer 07edea9b4401621e458ca83a732d15b7b8a39846a7076ce940f3421e9a5a6925"
        p = headers["Authorization"]
        resp = await requests.get(url, headers=headers)
        a = await json.loads(resp.text)
        topic = a['data'][0]['videoDetails']['name']
        k = a['data'][0]['videoDetails']['videoUrl']
        l = await k.replace('.mpd', '.m3u8')
        await god.send_message(m.chat.id, f'here is the link for the {topic} \n\n[clck here]({l})')
    except:
        await god.send_message(m.chat.id, 'aaj koi class nai hai lode!!')

@god.on_message(filters.command('live', '/') & filters.private)
async def starting(_, m: Message):
    try:
        url = "https://api.penpencil.xyz/v1/batches/621c5167a592f502085b0878/todays-schedule"
        headers = CaseInsensitiveDict()
        headers["Authorization"] = "Bearer 07edea9b4401621e458ca83a732d15b7b8a39846a7076ce940f3421e9a5a6925"
        p = headers["Authorization"]
        resp = requests.get(url, headers=headers)
        a = json.loads(resp.text)
        topic = a['data'][0]['topic']
        k = a['data'][0]['url']
        await god.send_message(m.chat.id, f'here is the link for the {topic} \n\n[clck here]({k})')
    except:
        await god.send_message(m.chat.id, 'aaj koi live class nai hai lode!!')


god.run()
