# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.b (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module for filter commands """
import re
from asyncio import sleep

from userbot import (BOTLOG, BOTLOG_CHATID, CMD_HELP,
                     is_mongo_alive, is_redis_alive)
from userbot.events import register, errors_handler

chatlist = []


@register(incoming=True)
@errors_handler
async def fischer(handler):
    global chatlist
    if handler.chat_id in chatlist:
        if handler.message.mentioned:
            await handler.reply("/fish")


@register(outgoing=True, pattern="^\.startfisch")
@errors_handler
async def startfischer(handler):
    global chatlist
    chatlist.append(handler.chat_id)
    await handler.edit("sollte getan sein")






CMD_HELP.update({
    ".startfisch":" Startet Fisching"
})
