from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message 
from MahakRobot import pbot as app
from MahakRobot import BOT_USERNAME



@app.on_message(filters.command("groupinfo", prefixes="/"))
async def get_group_status(_, message: Message):
    if len(message.command) != 2:
        await message.reply("❖ Please provide a group username.● Example ➥ `/groupinfo YourGroupUsername`")
        return
    
    group_username = message.command[1]
    
    try:
        group = await app.get_chat(group_username)
    except Exception as e:
        await message.reply(f"Error: {e}")
        return
    
    total_members = await app.get_chat_members_count(group.id)
    group_description = group.description
    premium_acc = banned = deleted_acc = bot = 0  # You should replace these variables with actual counts.

    response_text = (
        f"❖ ɢʀᴏᴜᴘ ɴᴀᴍᴇ ➥ {group.title}\n\n"
        f"● ɢʀᴏᴜᴘ ɪᴅ ➥ `{group.id}`\n"
        f"● ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀs ➥ {total_members}\n"
        f"● ᴜsᴇʀɴᴀᴍᴇ ➥ @{group_username}\n"
        f"● ᴅᴇsᴄʀɪᴘᴛɪᴏɴ ➥ \n{group_description or 'N/A'}\n\n"
        f"❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥ ˹ ᴍᴀʜᴀᴋ ꭙ ʀᴏʙᴏᴛ™ ♡゙"
    )
    
    await message.reply((response_text))






# Command handler to get group status
@app.on_message(filters.command("status") & filters.group)
def group_status(client, message):
    chat = message.chat  # Chat where the command was sent
    status_text = f"● ɢʀᴏᴜᴘ ɪᴅ ➥ `{chat.id}`\n" \
                  f"● ᴛɪᴛʟᴇ ➥ {chat.title}\n" \
                  f"● ᴛʏᴘᴇ ➥ {chat.type}\n"
                  
    if chat.username:  # Not all groups have a username
        status_text += f"● ᴜsᴇʀɴᴀᴍᴇ ➥ @{chat.username}\n\n❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥ ˹ ᴍᴀʜᴀᴋ ꭙ ʀᴏʙᴏᴛ™ ♡゙"
    else:
        status_text += "Username: None"

    message.reply_text((status_text))
    


__help__ = """

 ⬤ /groupinfo ➥ ɢᴇᴛ ɢʀᴏᴜᴘ ɪɴғᴏʀᴍᴀᴛɪᴏɴ.
 ⬤ /groupdata ➥ ɢᴇᴛ ɢʀᴏᴜᴘ ᴅᴀᴛᴀ.
"""

__mod_name__ = "ɢʀᴏᴜᴘ"
