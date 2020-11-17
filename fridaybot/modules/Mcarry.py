from telethon import events
import asyncio
import os
import sys
from fridaybot.utils import admin_cmd
import random

img1="https://telegra.ph/fileimg/5ce11befae23186761a3e.mp4"

img2="https://telegra.ph/file/a36e7014ead61d50f3e01.mp4"

img3="https://telegra.ph/file/de3750c1925a2537d68ed.mp4"


@borg.on(admin_cmd(outgoing=True, pattern="mcarry"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Caryy coming😎😎")
    await asyncio.sleep(0.8)
    x=(random.randrange(1,3))
    if x==1:
        await borg.send_file(event.chat_id,img1)
        await event.delete()
    if x==2:
        await borg.send_file(event.chat_id,img2)
        await event.delete()
    if x==3:
        await borg.send_file(event.chat_id,img3)
        await event.delete()