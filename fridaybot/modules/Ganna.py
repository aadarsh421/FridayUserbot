from telethon.errors.rpcerrorlist import YouBlockedUserError
#Marahmellow
from fridaybot.utils import admin_cmd, sudo_cmd, edit_or_reply

import asyncio

 

@borg.on(admin_cmd(pattern="gaana ?(.*)"))
@borg.on(sudo_cmd(pattern="gaana ?(.*)", allow_sudo=True))

async def FindMusicPleaseBot(gaana):

    song = gaana.pattern_match.group(1)

    chat = "@FindMusicPleaseBot"

    if not song:

        return await gaana.edit("```what should i search```")

    await gaana.edit("```Getting Your Music```")

    await asyncio.sleep(2)

    async with bot.conversation(chat) as conv:

        await gaana.edit("`Downloading...Please wait`")

        try:

            msg = await conv.send_message(song)

            response = await conv.get_response()

            if response.text.startswith("Sorry"):

                await bot.send_read_acknowledge(conv.chat_id)

                return await gaana.edit(f"Sorry, can't find {song}")

            respond = await conv.get_response()

            cobra = await conv.get_response()

        except YouBlockedUserError:

            await gaana.edit("```Please unblock``` @FindmusicpleaseBot``` and try again```")

            return

        await gaana.edit("`Sending Your Music...weit!Ã°ÂÂÂ`")

        await bot.send_file(gaana.chat_id, cobra)

        await bot.send_read_acknowledge(conv.chat_id)

    await gaana.delete()