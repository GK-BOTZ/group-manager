import requests
from pyrogram import filters
from pyrogram.types import Message,InlineKeyboardButton,InlineKeyboardMarkup
from pyrogram.enums import *
from MahakRobot import pbot as app
from MahakRobot import BOT_USERNAME



@app.on_message(filters.command("nude"))
async def nudes(_,message):
    if message.chat.type != ChatType.PRIVATE:
        return await message.reply_text("**⬤ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ᴏɴʟʏ ᴜsᴀʙʟᴇ ɪɴ ᴘᴍ ғᴏʀ ɢʀᴏᴜᴘ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ.**",
         reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("ɢᴏ ᴘᴍ", url=f"https://t.me/{app.me.username}?start=True")]
            ]
        ))
    x = requests.get('https://api.night-api.com/images/nsfw',headers={"authorization": "pUieNWJRIs-2Q073qw9dddUcM3Vncmn-eusGidDCIw"})
    await message.reply_photo(x.json()["content"]["url"], caption=f"❖ ɴᴜᴅᴇ ᴘɪᴄs ʙʏ ➥  ˹ ᴍᴀʜᴀᴋ ꭙ ʀᴏʙᴏᴛ™ ♡゙",)


__mod_name__ = "ɴᴜᴅᴇ"

__help__ = """

 ⬤ /nude ➥ ʀᴀɴᴅᴏᴍ ɴᴜᴅᴇ ɪᴍᴀɢᴇs (ᴡᴏʀᴋ ᴏɴʟʏ ʙᴏᴛ ᴘᴍ, ғᴏʀ ɢʀᴏᴜᴘ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ).
 """
