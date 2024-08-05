import logging
import os
import platform
import psutil
import time

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message
from MahakRobot import BOT_USERNAME, OWNER_ID
from MahakRobot import pbot as app

# Constants
FORBIDDEN_KEYWORDS = [
    "porn", "xxx", "NCERT", "ncert", "ans", "Pre-Medical",
    "kinematics", "Experiment", "experiments", "Ans", "jee",
    "Allen", "pre-medical", "institute"
]

# Handle Forbidden Keywords
@app.on_message(filters.text & filters.group)
async def handle_message(_, message):
    if any(keyword in message.text for keyword in FORBIDDEN_KEYWORDS):
        logging.info(f"Deleting message with ID {message.id}")
        await message.delete()
        await message.reply_text(f"@{message.from_user.username} 𝖣𝗈𝗇'𝗍 𝗌𝖾𝗇𝖽 𝗇𝖾𝗑𝗍 𝗍𝗂𝗆𝖾!")
    elif message.caption and any(keyword in message.caption for keyword in FORBIDDEN_KEYWORDS):
        logging.info(f"Deleting message with ID {message.id}")
        await message.delete()
        await message.reply_text(f"@{message.from_user.username} 𝖣𝗈𝗇'𝗍 𝗌𝖾𝗇𝖽 𝗇𝖾𝗑𝗍 𝗍𝗂𝗆𝖾!")

# Delete long edited messages but keep short messages and emoji reactions
async def delete_long_edited_messages(client, edited_message: Message):
    if edited_message.text and len(edited_message.text.split()) > 15:
        await edited_message.delete()
    elif edited_message.sticker or edited_message.animation:
        return

@app.on_edited_message(filters.group & ~filters.me)
async def handle_edited_messages(_, edited_message: Message):
    await delete_long_edited_messages(_, edited_message)

# Delete long messages in groups and reply with a warning
MAX_MESSAGE_LENGTH = 50  # Define the maximum allowed length for a message

async def delete_long_messages(client, message: Message):
    if message.text and len(message.text.split()) > MAX_MESSAGE_LENGTH:
        await message.delete()

@app.on_message(filters.group & ~filters.me)
async def handle_messages(_, message: Message):
    await delete_long_messages(_, message)
