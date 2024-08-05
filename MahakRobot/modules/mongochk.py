import asyncio
import re
from time import time

from pymongo import MongoClient
from pyrogram import filters
from pyrogram.types import Message

from MahakRobot import pbot as app


user_last_message_time = {}
user_command_count = {}

SPAM_THRESHOLD = 2
SPAM_WINDOW_SECONDS = 5


mongo_url_pattern = re.compile(r"mongodb(?:\+srv)?:\/\/[^\s]+")


@app.on_message(filters.command("mongochk"))
async def mongo_command(client, message: Message):
    user_id = message.from_user.id
    current_time = time()
    # Update the last message timestamp for the user
    last_message_time = user_last_message_time.get(user_id, 0)

    if current_time - last_message_time < SPAM_WINDOW_SECONDS:
        # If less than the spam window time has passed since the last message
        user_last_message_time[user_id] = current_time
        user_command_count[user_id] = user_command_count.get(user_id, 0) + 1
        if user_command_count[user_id] > SPAM_THRESHOLD:
            # Block the user if they exceed the threshold
            hu = await message.reply_text(
                f"**⬤ {message.from_user.mention} ᴘʟᴇᴀsᴇ ᴅᴏɴᴛ ᴅᴏ sᴘᴀᴍ, ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴀғᴛᴇʀ 5 sᴇᴄ**"
            )
            await asyncio.sleep(3)
            await hu.delete()
            return
    else:
        # If more than the spam window time has passed, reset the command count and update the message timestamp
        user_command_count[user_id] = 1
        user_last_message_time[user_id] = current_time

    if len(message.command) < 2:
        await message.reply(
            "⬤ Please enter your MongoDB URL after the command. Example ➥`/mongochk your_mongodb_url`"
        )
        return

    mongo_url = message.command[1]
    if re.match(mongo_url_pattern, mongo_url):
        try:
            # Attempt to connect to the MongoDB instance
            client = MongoClient(mongo_url, serverSelectionTimeoutMS=5000)
            client.server_info()  # Will cause an exception if connection fails
            await message.reply("⬤ ᴍᴏɴɢᴏᴅʙ ᴜʀʟ ɪs ᴠᴀʟɪᴅ ᴀɴᴅ ᴄᴏɴɴᴇᴄᴛɪᴏɴ sᴜᴄᴄᴇssғᴜʟʟ. ✅")
        except Exception as e:
            await message.reply(f"⬤ Failed to connect to MongoDB ➥ {e}")
    else:
        await message.reply("⬤ ɪɴᴠᴀʟɪᴅ ᴍᴏɴɢᴏᴅʙ ᴜʀʟ ғᴏʀᴍᴀᴛ 💔")
