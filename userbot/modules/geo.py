# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.b (the "License");
# you may not use this file except in compliance with the License.
"""
Userbot module to help you manage a group
"""

from asyncio import sleep
from telethon.errors import (BadRequestError, ChatAdminRequiredError,
                             ImageProcessFailedError, PhotoCropSizeSmallError,
                             UserAdminInvalidError)
from telethon.errors.rpcerrorlist import UserIdInvalidError
from telethon.tl.functions.channels import (EditAdminRequest,
                                            EditBannedRequest,
                                            EditPhotoRequest)
from telethon.tl.functions.messages import UpdatePinnedMessageRequest
from telethon.tl.types import (ChannelParticipantsAdmins, ChatAdminRights,
                               ChatBannedRights, MessageEntityMentionName,
                               MessageMediaPhoto)
from userbot import (BRAIN_CHECKER,
                     CMD_HELP, BOTLOG, BOTLOG_CHATID, bot,
                     is_mongo_alive, is_redis_alive)
from userbot.events import register
from userbot.modules.dbhelper import (mute, unmute, get_muted,
                                      gmute, ungmute, get_gmuted)
from telethon import events									  
from time import sleep
import asyncio
from datetime import date , time , datetime , timedelta


datetimeFormat = '%H:%M:%S'					  

# =================== CONSTANT ===================
PP_TOO_SMOL = "`The image is too small`"
PP_ERROR = "`Failure while processing image`"
NO_ADMIN = "`You aren't an admin!`"
NO_PERM = "`You don't have sufficient permissions!`"
NO_SQL = "`Database connections failing!`"

CHAT_PP_CHANGED = "`Chat Picture Changed`"
CHAT_PP_ERROR = "`Some issue with updating the pic,`" \
                "`maybe you aren't an admin,`" \
                "`or don't have the desired rights.`"
INVALID_MEDIA = "`Invalid Extension`"


@bot.on(events.NewMessage(outgoing=True, pattern="^.hate"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.hate"))
async def hate(bon):
    """ For .ban command, do "thanos" at targeted person """
    if not bon.text[0].isalpha() and bon.text[0] not in ("/", "#", "@", "!"):
        

        sender = await bon.get_reply_message()

        # Announce that we're going to whacking the pest
        await bon.edit("`AM ARSCH LECKEN`")
        await asyncio.sleep(3)
        # Delete message and then tell that the command
        # is done gracefully
        await bon.edit("`Die Person kann dich nun erfolgreich am Arsch lecken!`")

        # Announce to the logging group if we done a banning
        if BOTLOG:
            await bot.send_message(
                BOTLOG_CHATID,
                "DER IDIOT IS SCHEISSE " + str((await bon.get_reply_message()).sender_id),
            )

@bot.on(events.NewMessage(outgoing=True, pattern="^.love"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.love"))
async def love(bon):
    """ For .ban command, do "thanos" at targeted person """
    if not bon.text[0].isalpha() and bon.text[0] not in ("/", "#", "@", "!"):
        

        sender = await bon.get_reply_message()

        # Announce that we're going to whacking the pest
        await bon.edit("`AALP gestartet`")
        await asyncio.sleep(3)
        # Delete message and then tell that the command
        # is done gracefully
        await bon.edit("`Ich mag dich doch wieder!`")

        # Announce to the logging group if we done a banning
        if BOTLOG:
            await bot.send_message(
                BOTLOG_CHATID,
                "DER IDIOT IS SCHEISSE " + str((await bon.get_reply_message()).sender_id),
            )

@bot.on(events.NewMessage(outgoing=True, pattern="^.elph03"))
@bot.on(events.NewMessage(incoming=True,chats=-1001174690556, pattern="^.elph03"))
@bot.on(events.MessageEdited(outgoing=True, pattern="^.elph03"))
async def elph03(bon):
    """ Tell people when it's elph03 """
    if not bon.text[0].isalpha() and bon.text[0] not in ("/", "#", "@", "!"):
        

        sender = await bon.get_reply_message()

        # Questioning when it's 11:03
        el03 = await bon.reply("`Wann ist es endlich 11:03?`")
        await asyncio.sleep(5)
        # Delete message and then tell that the command
        # is done gracefully
        #now = datetime.now()
        #elph03 = 
        await el03.edit("`Es ist 11:03 in`" + " `das kann ich dir noch nicht sagen weil mein Boss das noch nicht programmiert hat`")

        # Announce to the logging group if we did tell them
        if BOTLOG:
            await bot.send_message(
                BOTLOG_CHATID,
                "1103 abgefragt",
            )
			
			
@bot.on(events.NewMessage(pattern="^.report", outgoing=True))
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
        mentions = "@admins\n"

    async def send_current_mentions():
        nonlocal mentions
        nonlocal event
        await event.respond(mentions)
        reset_mentions()

    reset_mentions()
    async for x in bot.iter_participants(input_chat, filter=ChannelParticipantsAdmins):
        if current_mentions < mention_limit:
            current_mentions += 1
           









            #mentions += f"[\u2063](tg://user?id={x.id})\n"
            # mentions += f"[@{x.username}](tg://user?id={x.id})\n"
            # mentions += f"@{x.username} "
            await event.respond(f"[Hey, {x.first_name}!](tg://user?id={x.id})")
        else:
            await send_current_mentions()
    if current_mentions > 0:
        await send_current_mentions()


CMD_HELP.update({
    "hate": ".hate\
    \nUsage: Tells people in German that you hate them."
})
CMD_HELP.update({
    "love": ".love\
    \nUsage: Tells people in German that you no longer hate them."
})
CMD_HELP.update({
    "elph03": ".elph03\
    \nUsage: This is a Insider so no Infos about that."
})
CMD_HELP.update({
    "report": ".report\
    \nUsage: Reports people and mentions all admins of the group."
})