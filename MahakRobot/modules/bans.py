import html

from telegram import ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext, CommandHandler, Filters
from telegram.utils.helpers import mention_html

from MahakRobot import (
    DEMONS,
    DEV_USERS,
    DRAGONS,
    LOGGER,
    OWNER_ID,
    TIGERS,
    WOLVES,
    dispatcher,
)
from MahakRobot.modules.disable import DisableAbleCommandHandler
from MahakRobot.modules.helper_funcs.chat_status import (
    bot_admin,
    can_delete,
    can_restrict,
    connection_status,
    is_user_admin,
    is_user_ban_protected,
    is_user_in_chat,
    user_admin,
    user_can_ban,
)
from MahakRobot.modules.helper_funcs.extraction import extract_user_and_text
from MahakRobot.modules.helper_funcs.string_handling import extract_time
from MahakRobot.modules.log_channel import gloggable, loggable


@connection_status
@bot_admin
@can_restrict
@user_admin
@user_can_ban
@loggable
def ban(update: Update, context: CallbackContext) -> str:
    chat = update.effective_chat
    user = update.effective_user
    message = update.effective_message
    log_message = ""
    bot = context.bot
    args = context.args
    user_id, reason = extract_user_and_text(message, args)

    if not user_id:
        message.reply_text("❖ ɪ ᴅᴏᴜʙᴛ ᴛʜᴀᴛ's ᴀ ᴜsᴇʀ.")
        return log_message
    try:
        member = chat.get_member(user_id)
    except BadRequest as excp:
        if excp.message != "❖ User not found":
            raise
        message.reply_text("❖ ᴄᴀɴ'ᴛ sᴇᴇɴ ᴛᴏ ғɪɴᴅ ᴛʜɪs ᴘᴇʀsᴏɴ.")
        return log_message
    if user_id == bot.id:
        message.reply_text("❖ ᴏʜ ʏᴇᴀʜ, ʙᴀɴ ᴍʏsᴇʟғ ʙᴀʙʏ.")
        return log_message

    if is_user_ban_protected(chat, user_id, member) and user not in DEV_USERS:
        if user_id == OWNER_ID:
            message.reply_text("❖ ᴛʀʏɪɴɢ ᴛᴏ ᴘᴜᴛ ᴍᴇ ᴀɢᴀɪɴsᴛ ᴀ ɢᴏᴅ ʟᴇᴠᴇʟ ᴅɪsᴀsᴛᴇʀ ʜᴜʜ?")
        elif user_id in DEV_USERS:
            message.reply_text("❖ ɪ ᴄᴀɴ'ᴛ ᴀᴄᴛ ᴀɢᴀɪɴsᴛ ᴏᴜʀ ᴏᴡɴ.")
        elif user_id in DRAGONS:
            message.reply_text(
                "❖ ғɪɢʜᴛɪɴɢ ᴛʜɪs ᴅʀᴀɢᴏɴ ʜᴇʀᴇ ᴡɪʟʟ ᴘᴜᴛ ᴄɪᴠɪʟɪᴀɴ ʟɪᴠᴇs ᴀᴛ ʀɪsᴋ."
            )
        elif user_id in DEMONS:
            message.reply_text(
                "❖ ʙʀɪɴɢ ᴀɴ ᴏʀᴅᴇʀ ғʀᴏᴍ ʜᴇʀᴏᴇs ᴀssᴏᴄɪᴀᴛɪᴏɴ ᴛᴏ ғɪɢʜᴛ ᴀ ᴅᴇᴍᴏɴ ᴅɪsᴀsᴛᴇʀ."
            )
        elif user_id in TIGERS:
            message.reply_text(
                "❖ ʙʀɪɴɢ ᴀɴ ᴏʀᴅᴇʀ ғʀᴏᴍ ʜᴇʀᴏᴇs ᴀssᴏᴄɪᴀᴛɪᴏɴ ᴛᴏ ғɪɢʜᴛ ᴀ ᴛɪɢᴇʀ ᴅɪsᴀsᴛᴇʀ."
            )
        elif user_id in WOLVES:
            message.reply_text("❖ ᴡᴏʟғ ᴀʙɪʟɪᴛɪᴇs ᴍᴀᴋᴇ ᴛʜᴇᴍ ʙᴀɴ ɪᴍᴍᴜɴᴇ!")
        else:
            message.reply_text("❖ ᴡᴏʟғ ᴀʙɪʟɪᴛɪᴇs ᴍᴀᴋᴇ ᴛʜᴇᴍ ʙᴀɴ ɪᴍᴍᴜɴᴇ!")
        return log_message
    if message.text.startswith("/s"):
        silent = True
        if not can_delete(chat, context.bot.id):
            return ""
    else:
        silent = False
    log = (
        f"❖ <b>ᴜsᴇʀ ʙᴀɴɴᴇᴅ ғʀᴏᴍ {html.escape(chat.title)}</b>\n\n"
        f"● <b>ʙᴀɴɴᴇᴅ ʙʏ ➥</b> {mention_html(user.id, html.escape(user.first_name))}\n"
        f"● <b>ᴜsᴇʀ ➥</b> {mention_html(member.user.id, html.escape(member.user.first_name))}"
    )
    if reason:
        log += "\n\n❖ <b>ʀᴇᴀsᴏɴ ➥</b> {}".format(reason)

    try:
        chat.ban_member(user_id)

        if silent:
            if message.reply_to_message:
                message.reply_to_message.delete()
            message.delete()
            return log

        # bot.send_sticker(chat.id, BAN_STICKER)  # banhammer marie sticker
        reply = (
            f"<code> </code><b>❖ ᴀ ᴜsᴇʀ ʙᴀɴɴᴇᴅ ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ</b>\n\n"
            f"<code> </code><b>● ʙᴀɴɴᴇᴅ ʙʏ ➥</b> {mention_html(user.id, user.first_name)}\n"
            f"<code> </code><b>● ᴜsᴇʀ ➥</b> {mention_html(member.user.id, html.escape(member.user.first_name))}\n"
        )
        if reason:
            reply += f"\n\n<code> </code><b>❖ ʀᴇᴀsᴏɴ ➥</b> \n{html.escape(reason)}"
        bot.sendMessage(chat.id, reply, parse_mode=ParseMode.HTML)
        return log

    except BadRequest as excp:
        if excp.message == "❖ Reply message not found":
            # Do not reply
            if silent:
                return log
            message.reply_text("❖ ʙᴀɴɴᴇᴅ !", quote=False)
            return log
        else:
            LOGGER.warning(update)
            LOGGER.exception(
                "⬤ ERROR ʙᴀɴɴɪɴɢ ᴜsᴇʀ %s ɪɴ ᴄʜᴀᴛ %s (%s) ᴅᴜᴇ ᴛᴏ %s",
                user_id,
                chat.title,
                chat.id,
                excp.message,
            )
            message.reply_text("❖ ᴛʜᴀᴛ ᴅɪᴅɴ'ᴛ ᴡᴏʀᴋ ..")

    return log_message


@connection_status
@bot_admin
@can_restrict
@user_admin
@user_can_ban
@loggable
def temp_ban(update: Update, context: CallbackContext) -> str:
    chat = update.effective_chat
    user = update.effective_user
    message = update.effective_message
    log_message = ""
    bot, args = context.bot, context.args
    user_id, reason = extract_user_and_text(message, args)

    if not user_id:
        message.reply_text("❖ ɪ ᴅᴏᴜʙᴛ ᴛʜᴀᴛ's ᴀ ᴜsᴇʀ.")
        return log_message

    try:
        member = chat.get_member(user_id)
    except BadRequest as excp:
        if excp.message != "❖ User not found":
            raise
        message.reply_text("❖ ɪ ᴄᴀɴ'ᴛ sᴇᴇᴍ ᴛᴏ ғɪɴᴅ ᴛʜɪs ᴜsᴇʀ.")
        return log_message
    if user_id == bot.id:
        message.reply_text("❖ ɪ'ᴍ ɴᴏᴛ ɢᴏɴɴᴀ ʙᴀɴ ᴍʏsᴇʟғ, ᴀʀᴇ ʏᴏᴜ ᴄʀᴀᴢʏ?")
        return log_message

    if is_user_ban_protected(chat, user_id, member):
        message.reply_text("❖ ɪ ᴅᴏɴ'ᴛ ғᴇᴇʟ ʟɪᴋᴇ ɪᴛ.")
        return log_message

    if not reason:
        message.reply_text("❖ ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ sᴘᴇᴄɪғɪᴇᴅ ᴀ ᴛɪᴍᴇ ᴛᴏ ʙᴀɴ ᴛʜɪs ᴜsᴇʀ ғᴏʀ!")
        return log_message

    split_reason = reason.split(None, 1)

    time_val = split_reason[0].lower()
    reason = split_reason[1] if len(split_reason) > 1 else ""
    bantime = extract_time(message, time_val)

    if not bantime:
        return log_message

    log = (
        f"❖ <b>{html.escape(chat.title)}</b>\n"
        "❍ ᴛᴇᴍᴩ ʙᴀɴ\n"
        f"❍ <b>ʙᴀɴɴᴇᴅ ʙʏ ➛</b> {mention_html(user.id, html.escape(user.first_name))}\n"
        f"❍ <b>ᴜsᴇʀ ➛</b> {mention_html(member.user.id, html.escape(member.user.first_name))}\n"
        f"❍ <b>ᴛɪᴍᴇ ➛</b> {time_val}"
    )
    if reason:
        log += "\n❍ <b>ʀᴇᴀsᴏɴ ➛</b> {}".format(reason)

    try:
        chat.ban_member(user_id, until_date=bantime)
        # bot.send_sticker(chat.id, BAN_STICKER)  # banhammer marie sticker
        bot.sendMessage(
            chat.id,
            f"❖ ʙᴀɴɴᴇᴅ ! ᴜsᴇʀ {mention_html(member.user.id, html.escape(member.user.first_name))} "
            f"● ɪs ɴᴏᴡ ʙᴀɴɴᴇᴅ ғᴏʀ {time_val}.",
            parse_mode=ParseMode.HTML,
        )
        return log

    except BadRequest as excp:
        if excp.message == "❖ Reply message not found":
            # Do not reply
            message.reply_text(
                f"❖  ʙᴀɴɴᴇᴅ ! ᴜsᴇʀ ᴡɪʟʟ ʙᴇ  ʙᴀɴɴᴇᴅ ғᴏʀ  {time_val}.", quote=False
            )
            return log
        else:
            LOGGER.warning(update)
            LOGGER.exception(
                "⬤ ERROR ʙᴀɴɴɪɴɢ ᴜsᴇʀ %s ɪɴ ᴄʜᴀᴛ %s (%s) ᴅᴜᴇ ᴛᴏ %s",
                user_id,
                chat.title,
                chat.id,
                excp.message,
            )
            message.reply_text("❖ ɪ ᴄᴀɴ'ᴛ ʙᴀɴ ᴛʜᴀᴛ ᴜsᴇʀ.")

    return log_message


@connection_status
@bot_admin
@can_restrict
@user_admin
@user_can_ban
@loggable
def kick(update: Update, context: CallbackContext) -> str:
    chat = update.effective_chat
    user = update.effective_user
    message = update.effective_message
    log_message = ""
    bot, args = context.bot, context.args
    user_id, reason = extract_user_and_text(message, args)

    if not user_id:
        message.reply_text("❖ ɪ ᴅᴏᴜʙᴛ ᴛʜᴀᴛ's ᴀ ᴜsᴇʀ.")
        return log_message

    try:
        member = chat.get_member(user_id)
    except BadRequest as excp:
        if excp.message != "❖ User not found":
            raise

        message.reply_text("❖ ɪ ᴄᴀɴ'ᴛ sᴇᴇᴍ ᴛᴏ ғɪɴᴅ ᴛʜɪs ᴜsᴇʀ.")
        return log_message
    if user_id == bot.id:
        message.reply_text("❖ ɪ'ᴍ ɴᴏᴛ ɢᴏɴɴᴀ ᴅᴏ ᴛʜᴀᴛ.")
        return log_message

    if is_user_ban_protected(chat, user_id):
        message.reply_text("❖ I really wish I could kick this user....")
        return log_message

    res = chat.unban_member(user_id)  # unban on current user = kick
    if res:
        # bot.send_sticker(chat.id, BAN_STICKER)  # banhammer marie sticker
        bot.sendMessage(
            chat.id,
            f"❖ ᴜsᴇʀ ᴋɪᴄᴋᴇᴅ ᴛᴏ ɢʀᴏᴜᴘ ➥ {mention_html(member.user.id, html.escape(member.user.first_name))}.",
            parse_mode=ParseMode.HTML,
        )
        log = (
            f"❍ <b>{html.escape(chat.title)}</b>\n"
            f"❍ ᴋɪᴄᴋᴇᴅ\n"
            f"❍ <b>ᴋɪᴄᴋᴇᴅ ʙʏ ➛</b> {mention_html(user.id, html.escape(user.first_name))}\n"
            f"❍ <b>ᴜsᴇʀ ➛</b> {mention_html(member.user.id, html.escape(member.user.first_name))}"
        )
        if reason:
            log += f"\n❍ <b>ʀᴇᴀsᴏɴ ➛</b> {reason}"

        return log

    else:
        message.reply_text("❖ ɪ ᴄᴀɴ'ᴛ ᴋɪᴄᴋ ᴛʜᴀᴛ ᴜsᴇʀ.")

    return log_message


@bot_admin
@can_restrict
def kickme(update: Update, context: CallbackContext):
    user_id = update.effective_message.from_user.id
    if is_user_admin(update.effective_chat, user_id):
        update.effective_message.reply_text("❖ ʏᴏᴜ'ʀᴇ ᴀɴ ᴀᴅᴍɪɴ.")
        return

    res = update.effective_chat.unban_member(user_id)  # unban on current user = kick
    if res:
        update.effective_message.reply_text("*❖ ᴋɪᴄᴋs, ʏᴏᴜ ᴏᴜᴛ ᴏғ ᴛʜᴇ ɢʀᴏᴜᴘ*")
    else:
        update.effective_message.reply_text("❖ ɪ ᴄᴀɴ'ᴛ 🦶")


@connection_status
@bot_admin
@can_restrict
@user_admin
@user_can_ban
@loggable
def unban(update: Update, context: CallbackContext) -> str:
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat
    log_message = ""
    bot, args = context.bot, context.args
    user_id, reason = extract_user_and_text(message, args)

    if not user_id:
        message.reply_text("❖ ɪ ᴅᴏᴜʙᴛ ᴛʜᴀᴛ's ᴀ ᴜsᴇʀ.")
        return log_message

    try:
        member = chat.get_member(user_id)
    except BadRequest as excp:
        if excp.message != "❖ User not found":
            raise
        message.reply_text("❖ ɪ ᴄᴀɴ'ᴛ sᴇᴇᴍ ᴛᴏ ғɪɴᴅ ᴛʜɪs ᴜsᴇʀ.")
        return log_message
    if user_id == bot.id:
        message.reply_text("❖ ʜᴏᴡ ᴡᴏᴜʟᴅ ɪ ᴜɴʙᴀɴ ᴍʏsᴇʟғ ɪғ ɪ ᴡᴀsɴ'ᴛ ʜᴇʀᴇ...?")
        return log_message

    if is_user_in_chat(chat, user_id):
        message.reply_text("❖ ɪsɴ'ᴛ ᴛʜɪs ᴘᴇʀsᴏɴ ᴀʟʀᴇᴀᴅʏ ʜᴇʀᴇ ?")
        return log_message

    chat.unban_member(user_id)
    message.reply_text("❖ ʜᴇʜᴇ, ᴛʜɪs ᴜsᴇʀ ᴄᴀɴ ᴊᴏɪɴ ᴀɢᴀɪɴ.")

    log = (
        f"❍ <b>{html.escape(chat.title)}</b>\n"
        f"❍ ᴜɴʙᴀɴɴᴇᴅ\n"
        f"❍ <b>ᴜɴʙᴀɴɴᴇᴅ ʙʏ ➛</b> {mention_html(user.id, html.escape(user.first_name))}\n"
        f"❍ <b>ᴜsᴇʀ ➛</b> {mention_html(member.user.id, html.escape(member.user.first_name))}"
    )
    if reason:
        log += f"\n<b>ʀᴇᴀsᴏɴ:</b> {reason}"

    return log


@connection_status
@bot_admin
@can_restrict
@gloggable
def selfunban(context: CallbackContext, update: Update) -> str:
    message = update.effective_message
    user = update.effective_user
    bot, args = context.bot, context.args
    if user.id not in DRAGONS or user.id not in TIGERS:
        return

    try:
        chat_id = int(args[0])
    except:
        message.reply_text("❖ ɢɪᴠᴇ ᴀ ᴠᴀʟɪᴅ ᴄʜᴀᴛ ɪᴅ.")
        return

    chat = bot.get_chat(chat_id)

    try:
        member = chat.get_member(user.id)
    except BadRequest as excp:
        if excp.message == "❖ User not found":
            message.reply_text("❖ ɪ ᴄᴀɴ'ᴛ sᴇᴇᴍ ᴛᴏ ғɪɴᴅ ᴛʜɪs ᴜsᴇʀ.")
            return
        else:
            raise

    if is_user_in_chat(chat, user.id):
        message.reply_text("❖ ᴀʀᴇɴ'ᴛ ʏᴏᴜ ᴀʟʀᴇᴀᴅʏ ɪɴ ᴛʜᴇ ᴄʜᴀᴛ??")
        return

    chat.unban_member(user.id)
    message.reply_text("❖ ʏᴇᴘ, ɪ ʜᴀᴠᴇ ᴜɴʙᴀɴɴᴇᴅ ʏᴏᴜ.")

    log = (
        f"✦ <b>{html.escape(chat.title)}</b>\n\n"
        f"❍ ᴜɴʙᴀɴɴᴇᴅ\n"
        f"❍ <b>ᴜɴʙᴀɴɴᴇᴅ ʙʏ ➛</b> {mention_html(user.id, user.first_name)}\n"
        f"❍ <b>ᴜsᴇʀ ➛</b> {mention_html(member.user.id, html.escape(member.user.first_name))}"
    )

    return log





__help__ = """

 ⬤ /kickme *➥* ᴋɪᴄᴋs ᴛʜᴇ ᴜsᴇʀ ᴡʜᴏ ɪssᴜᴇᴅ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ

 ⬤ /ban <ᴜsᴇʀʜᴀɴᴅʟᴇ>* ➥* ʙᴀɴs ᴀ ᴜsᴇʀ. (ᴠɪᴀ ʜᴀɴᴅʟᴇ, ᴏʀ ʀᴇᴘʟʏ)
 ⬤ /sban  <ᴜsᴇʀʜᴀɴᴅʟᴇ>* ➥* sɪʟᴇɴᴛʟʏ ʙᴀɴ ᴀ ᴜsᴇʀ. ᴅᴇʟᴇᴛᴇs ᴄᴏᴍᴍᴀɴᴅ, ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇ ᴀɴᴅ ᴅᴏᴇsɴ'ᴛ ʀᴇᴘʟʏ. (ᴠɪᴀ ʜᴀɴᴅʟᴇ, ᴏʀ ʀᴇᴘʟʏ)
 ⬤ /tban  <ᴜsᴇʀʜᴀɴᴅʟᴇ> x(ᴍ/ʜ/ᴅ)* ➥* ʙᴀɴs ᴀ ᴜsᴇʀ ғᴏʀ `x` ᴛɪᴍᴇ. (ᴠɪᴀ ʜᴀɴᴅʟᴇ, ᴏʀ ʀᴇᴘʟʏ). `ᴍ` = `ᴍɪɴᴜᴛᴇs`, `ʜ` = `ʜᴏᴜʀs`, `ᴅ` = `ᴅᴀʏs`.
 ⬤ /unban  <ᴜsᴇʀʜᴀɴᴅʟᴇ>* ➥* ᴜɴʙᴀɴs ᴀ ᴜsᴇʀ. (ᴠɪᴀ ʜᴀɴᴅʟᴇ, ᴏʀ ʀᴇᴘʟʏ)
 ⬤ /kick <ᴜsᴇʀʜᴀɴᴅʟᴇ>* ➥* ᴋɪᴄᴋs ᴀ ᴜsᴇʀ ᴏᴜᴛ ᴏғ ᴛʜᴇ ɢʀᴏᴜᴘ, (ᴠɪᴀ ʜᴀɴᴅʟᴇ, ᴏʀ ʀᴇᴘʟʏ)
"""

BAN_HANDLER = CommandHandler(["ban", "sban"], ban, run_async=True)
TEMPBAN_HANDLER = CommandHandler(["tban"], temp_ban, run_async=True)
KICK_HANDLER = CommandHandler("kick", kick, run_async=True)
UNBAN_HANDLER = CommandHandler("unban", unban, run_async=True)
ROAR_HANDLER = CommandHandler("roar", selfunban, run_async=True)
KICKME_HANDLER = DisableAbleCommandHandler(
    "kickme", kickme, filters=Filters.chat_type.groups, run_async=True
)

dispatcher.add_handler(BAN_HANDLER)
dispatcher.add_handler(TEMPBAN_HANDLER)
dispatcher.add_handler(KICK_HANDLER)
dispatcher.add_handler(UNBAN_HANDLER)
dispatcher.add_handler(ROAR_HANDLER)
dispatcher.add_handler(KICKME_HANDLER)

__mod_name__ = "ʙᴀɴ"
__handlers__ = [
    BAN_HANDLER,
    TEMPBAN_HANDLER,
    KICK_HANDLER,
    UNBAN_HANDLER,
    ROAR_HANDLER,
    KICKME_HANDLER,
      ]
  
