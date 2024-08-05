from telethon.tl.types import ChatBannedRights
from telethon.tl.functions.channels import EditBannedRequest
from telethon import events
from MahakRobot import telethn as tbot, DEV_USERS

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

@tbot.on(events.NewMessage(pattern="/banall$"))
async def banall(hmm):
    if not hmm.is_group:
        return
    if hmm.is_group:
        if hmm.sender_id not in DEV_USERS:
            return
    async for user in tbot.iter_participants(hmm.chat_id):
        if not user.deleted:
            try:
                await hmm.client(
                        EditBannedRequest(hmm.chat_id, user.id, BANNED_RIGHTS)
                    )
            except:
                pass


