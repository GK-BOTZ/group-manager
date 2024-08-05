from pyrogram import filters

from MahakRobot import pbot
from MahakRobot import BOT_USERNAME
from MahakRobot.utils.errors import capture_err
from MahakRobot.utils.functions import make_carbon

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup



@pbot.on_message(filters.command("carbon"))
@capture_err
async def carbon_func(_, message):
    if message.reply_to_message:
        if message.reply_to_message.text:
            txt = message.reply_to_message.text
        else:
            return await message.reply_text("⬤ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ.")
    else:
        try:
            txt = message.text.split(None, 1)[1]
        except IndexError:
            return await message.reply_text("⬤ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ sᴏᴍᴇ ᴛᴇxᴛ.")
    m = await message.reply_text("⚡")
    carbon = await make_carbon(txt)
    await m.edit_text("⬤ ᴜᴩʟᴏᴀᴅɪɴɢ ɢᴇɴᴇʀᴀᴛᴇᴅ ᴄᴀʀʙᴏɴ...")
    await pbot.send_photo(
        message.chat.id,
        photo=carbon,
        caption=f"❖ ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥ ˹ ᴍᴀʜᴀᴋ ꭙ ʀᴏʙᴏᴛ™ ♡゙",
    )
    await m.delete()
    carbon.close()

####
