from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("start"))
async def start_handler(client, message: Message):
    await message.reply_text(
        "👋 Welcome XYZ!\n\n⚠️ Only premium users can use this bot.\n\n💳 To access features, please check the plans by clicking /plan."
    )
