from pyrogram import Client, filters
from pyrogram.types import Message
from bot.premium_utils import add_premium

@Client.on_message(filters.command("addpremium") & filters.user(YOUR_TELEGRAM_USER_ID))
async def addpremium_handler(client, message: Message):
    try:
        _, user_id, days = message.text.split()
        add_premium(user_id, int(days))
        await message.reply_text(f"✅ Added user {user_id} to premium for {days} days.")
    except:
        await message.reply_text("❌ Usage: /addpremium <user_id> <days>")
