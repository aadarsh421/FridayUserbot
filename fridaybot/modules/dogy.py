#Credit to @M_R_S_P_I_D_Y
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from fridaybot import CMD_HELP
from fridaybot.utils import admin_cmd
D=("░░░░░░░░░░\n"
"░▐░░░░░░░▄██▄▄\n"
"░░▀▀██████▀░░░░▓▓\n"
"░░░░▐▐░░▐▐░░░░░░▓▓▓▓╝\n"
"▒▒▒▒▐▐▒▒▐▐▒▒▒▒▒▒▓▒▒▓\n")

@borg.on(admin_cmd(pattern=r"dogy"))
async def spidy(dogy):
    await dogy.edit(D)