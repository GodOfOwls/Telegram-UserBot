
import re
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

from userbot import (BOTLOG, BOTLOG_CHATID, BRAIN_CHECKER, CMD_HELP, bot,
                     is_mongo_alive, is_redis_alive)
from userbot.events import errors_handler, register
from userbot.modules.dbhelper import (get_gmuted, get_muted, gmute, mute,
                                      ungmute, unmute)
from userbot.utils import helpers
from userbot.utils.mdtex import Bold, Code, KeyValueItem, MDTeXDocument, Section






@register(outgoing=True, pattern="^\.i(nvite)?l(ink)?")
@errors_handler
async def invitelink(event):
    """Command to get link creator, chatid and the random part of an invite link."""

    _, args = await helpers.get_args(event)
    link = args[0]
    link_creator, chatid, random_part = await helpers.resolve_invite_link(link)
    caption = "<b>INVITELINK INFO:</b> \n"
    caption += f"Creator ID: {link_creator} \n"
    caption += f"Chat ID: {chatid} \n"
    caption += f"Random ID: {random_part} \n"
    
    await event.reply(caption)






















CMD_HELP.update({
    ".il ":" check invite links BETA"
})
