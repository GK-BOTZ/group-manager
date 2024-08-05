from pyrogram import filters
from blackpink import blackpink as bp
from MahakRobot import pbot as app
from MahakRobot import BOT_USERNAME
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup



###
@app.on_message(filters.command("blackpink"))
async def blackpink(_, message):
    text = message.text[len("/blackpink ") :]
    bp(f"{text}").save(f"blackpink_{message.from_user.id}.png", caption=f"❖ ʙʟᴀᴄᴋᴘɪɴᴋ ʙʏ ➥ ˹ ᴍᴀʜᴀᴋ ꭙ ʀᴏʙᴏᴛ™", )
    await message.reply_photo(f"blackpink_{message.from_user.id}.png", caption=f"❖ ʙʟᴀᴄᴋᴘɪɴᴋ ʙʏ ➥ ˹ ᴍᴀʜᴀᴋ ꭙ ʀᴏʙᴏᴛ™",)
    os.remove(f"blackpink_{message.from_user.id}.png")
  
