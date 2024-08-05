from pyrogram import filters
from MahakRobot import pgram
from MahakRobot import OWNER_ID
from MahakRobot import pbot as app


@bot.on_message(filters.private & filters.incoming)
async def on_pm_s(client: Client, message: Message):
    if not message.from_user.id == 6454209118:
        fwded_mesg = await message.forward(chat_id=OWNER_ID, disable_notification=True)