from pyrogram import filters, enums
from pyrogram.types import Message
from bot import Bot




@Bot.on_message(filters.command("id") & filters.private)
async def showid(client, message):
    chat_type = message.chat.type

    if chat_type == enums.ChatType.PRIVATE:
        user_id = message.chat.id
        await message.reply_text(
            f"<b>Your User ID Is :</b> <code>{user_id}</code>", 
            quote=True
        )
        





# TD Bot Dev
# Don't Remove Credit!!!
#YouTube channel link https://youtube.com/@tdbotdev?si=j3HVY4E69-C4ZDcw
# Telegram Channel @TD_Public_Bots
# Developer @TD_Public_Bots

