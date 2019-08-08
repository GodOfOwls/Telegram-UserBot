# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from telethon.errors import MessageTooLongError

from time import sleep

from telethon import events
from telethon.errors import BadRequestError
from telethon.errors.rpcerrorlist import UserIdInvalidError
from telethon.tl.functions.channels import EditAdminRequest, EditBannedRequest

from telethon.tl.types import ChatAdminRights, ChatBannedRights

from userbot import (BRAIN_CHECKER, bot)
@bot.on(events.NewMessage(pattern=r"\.json", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        print(previous_message.stringify())
        try:
            await event.edit(previous_message.stringify())
        except MessageTooLongError as e:
            await event.edit(str(e))
    else:
        try:
            await event.edit(event.stringify())
        except MessageTooLongError as e:
            await event.edit(str(e))


