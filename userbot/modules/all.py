# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

#TODO Support specifying the message content. The subsequent mentions should just reply to this message and have a ☝🏻 emoji.

from time import sleep

from telethon import events
from telethon.errors import BadRequestError
from telethon.errors.rpcerrorlist import UserIdInvalidError
from telethon.tl.functions.channels import EditAdminRequest, EditBannedRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChatAdminRights, ChatBannedRights

from userbot import (BRAIN_CHECKER, bot)





@bot.on(events.NewMessage(pattern=r"(?i)^\.all(IDs)?$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.delete()
    mention_limit = 30
    current_mentions = 0
    mentions = "@all\n"
    input_chat = event.chat
    def reset_mentions():
        nonlocal current_mentions
        nonlocal mentions
        nonlocal mention_limit
        current_mentions = 0
        if event.raw_text.lower() == '.allids':
            mention_limit = 90
            mentions = f"Users in chat number {input_chat.id}:\n"
        else:
            mentions = "@all\n"

    async def send_current_mentions():
        nonlocal mentions
        nonlocal event
        await event.respond(mentions)
        reset_mentions()

    reset_mentions()
    async for x in bot.iter_participants(input_chat, 9000):
        if current_mentions < mention_limit:
            current_mentions += 1
            if event.raw_text.lower() == '.allids':
                # current_mentions = 1 #Effectively disables the chunking scheme and sends all output in a huge text. It might actually be undesirable since there is a limit on message size. So let's not use it.
                mentions += f"{x.first_name} {x.last_name} ({x.username}): id={x.id}\n"
            else:
                mentions += f"[\u2063](tg://user?id={x.id})"
                # mentions += f"[@{x.username}](tg://user?id={x.id})\n"
            # mentions += f"@{x.username} "
            # await event.respond(f"[Hey, {x.first_name}!](tg://user?id={x.id})")
        else:
            await send_current_mentions()
    if current_mentions > 0:
        await send_current_mentions()





@bot.on(events.NewMessage(pattern=".commonsofall", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.delete()
    current_mentions = 0
    mention_limit = 20
    input_chat = event.chat
    mentions = "Eine Liste der gemeinsamen Gruppen pro User:"
    def reset_mentions():
        nonlocal current_mentions
        nonlocal mentions
        nonlocal mention_limit
        current_mentions = 0


    async def send_current_mentions():
        nonlocal mentions
        nonlocal event
        await event.respond(mentions)
        reset_mentions()

    reset_mentions()
    async for x in bot.iter_participants(input_chat, 9000):
        if current_mentions < mention_limit:
            current_mentions += 1
            replied_user = await bot(GetFullUserRequest(x.id))
            mentions += f"[{x.first_name}](tg://user?id={x.id}): gemeinsame Chats={replied_user.common_chats_count}\n"


        else:
            await send_current_mentions()
    if current_mentions > 0:
        await send_current_mentions()
