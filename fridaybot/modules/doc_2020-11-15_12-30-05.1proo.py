"""Fun pligon...for HardcoreUserbot
\nCode by @The_Avengers_leader
type `.1proo` and to see the fun.
"""
import random, re
from uniborg.util import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern="1proo ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("TERI JAISI RANDI MAINE AAJ TAK DEKHA NHI")
        await asyncio.sleep(2.5)
        await event.edit("TU TO HAZARO MAI EK HAI")
        await asyncio.sleep(2.5)
        await event.edit("ISLIYE TO MAI TUJHE ROZ CHODTA HUU")
        await asyncio.sleep(2.5)
        await event.edit("CHAL AB CHOD DIYA MAI TUJHE AB NIKAL KOI DUSRA DUNDH NA MILE TO WAPS AANA")
        await asyncio.sleep(2.5)
        await event.edit("**TERI JAISI RANDI MAINE AAJ TAK DEKHA NHI, TU TO HAZARO MAI EK HAI  ,ISLIYE TO MAI TUJHE ROZ CHODTA HUU  ,CHAL AB CHOD DIYA MAI TUJHE AB NIKAL KOI DUSRA DUNDH NA MILE TO WAPS AANA  **")





