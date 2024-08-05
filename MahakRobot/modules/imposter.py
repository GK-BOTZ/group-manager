import random 

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message 
from MahakRobot import BOT_USERNAME
from MahakRobot.modules.pretenderdb import impo_off, impo_on, check_pretender, add_userdata, get_userdata, usr_data
from MahakRobot import pbot as app

MISHI = [

]




@app.on_message(filters.group & ~filters.bot & ~filters.via_bot, group=69)
async def chk_usr(_, message: Message):
    if message.sender_chat or not await check_pretender(message.chat.id):
        return
    if not await usr_data(message.from_user.id):
        return await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    usernamebefore, first_name, lastname_before = await get_userdata(message.from_user.id)
    msg = ""
    if (
        usernamebefore != message.from_user.username
        or first_name != message.from_user.first_name
        or lastname_before != message.from_user.last_name
    ):
        msg += f"""
**❖ ᴜsᴇʀ sʜᴏʀᴛ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ❖**

**● ɴᴀᴍᴇ** ➥ {message.from_user.mention}
**● ᴜsᴇʀ ɪᴅ** ➥ {message.from_user.id}
"""
    if usernamebefore != message.from_user.username:
        usernamebefore = f"@{usernamebefore}" if usernamebefore else "ɴᴏ ᴜsᴇʀɴᴀᴍᴇ"
        usernameafter = (
            f"@{message.from_user.username}"
            if message.from_user.username
            else "ɴᴏ ᴜsᴇʀɴᴀᴍᴇ"
        )
        msg += """
**✽ ᴄʜᴀɴɢᴇᴅ ᴜsᴇʀɴᴀᴍᴇ ✽**

**● ʙᴇғᴏʀᴇ** ➥ {bef}
**● ᴀғᴛᴇʀ** ➥ {aft}
""".format(bef=usernamebefore, aft=usernameafter)
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if first_name != message.from_user.first_name:
        msg += """
**✽ ᴄʜᴀɴɢᴇs ғɪʀsᴛ ɴᴀᴍᴇ ✽**

**● ʙᴇғᴏʀᴇ** ➥ {bef}
**● ᴀғᴛᴇʀ** ➥ {aft}
""".format(
            bef=first_name, aft=message.from_user.first_name
        )
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if lastname_before != message.from_user.last_name:
        lastname_before = lastname_before or "ɴᴏ ʟᴀsᴛ ɴᴀᴍᴇ"
        lastname_after = message.from_user.last_name or "ɴᴏ ʟᴀsᴛ ɴᴀᴍᴇ"
        msg += """
**✽ ᴄʜᴀɴɢᴇs ʟᴀsᴛ ɴᴀᴍᴇ ✽**

**● ʙᴇғᴏʀᴇ** ➥ {bef}
**● ᴀғᴛᴇʀ** ➥ {aft}
""".format(
            bef=lastname_before, aft=lastname_after
        )
        await add_userdata(
            message.from_user.id,
            message.from_user.username,
            message.from_user.first_name,
            message.from_user.last_name,
        )
    if msg != "":
        await message.reply_photo(random.choice(MISHI), caption=msg)


@app.on_message(filters.group & filters.command("imposter") & ~filters.bot & ~filters.via_bot)
async def set_mataa(_, message: Message):
    if len(message.command) == 1:
        return await message.reply("**❅ ᴅᴇᴛᴇᴄᴛ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴜsᴇʀs ᴜsᴀɢᴇ ➥ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴏɴ|ᴏғғ**")
    if message.command[1] == "enable":
        cekset = await impo_on(message.chat.id)
        if cekset:
            await message.reply("**❅ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴍᴏᴅᴇ ɪs ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ.**")
        else:
            await impo_on(message.chat.id)
            await message.reply(f"**❅ sᴜᴄᴄᴇssғᴜʟʟʏ ᴇɴᴀʙʟᴇᴅ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴍᴏᴅᴇ ғᴏʀ** {message.chat.title}")
    elif message.command[1] == "disable":
        cekset = await impo_off(message.chat.id)
        if not cekset:
            await message.reply("**❅ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴍᴏᴅᴇ ɪs ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ.**")
        else:
            await impo_off(message.chat.id)
            await message.reply(f"**❅ sᴜᴄᴄᴇssғᴜʟʟʏ ᴅɪsᴀʙʟᴇᴅ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴍᴏᴅᴇ ғᴏʀ** {message.chat.title}")
    else:
        await message.reply("**❅ ᴅᴇᴛᴇᴄᴛ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴜsᴇʀs ᴜsᴀɢᴇ ➥ ᴘʀᴇᴛᴇɴᴅᴇʀ ᴏɴ|ᴏғғ**")


__help__ = """

 ⬤ /imposter [Enable || Disable]* ➥* ᴛʜɪs ɪs ᴜsᴇʀ ɴᴀᴍᴇ/ᴜsᴇʀɴᴀᴍᴇ ᴄʜᴀɴɢᴇ ᴀʟᴇʀᴛ sʏsᴛᴇᴍ.
"""

__mod_name__ = "ɪᴍᴘᴏsᴛᴇʀ"
