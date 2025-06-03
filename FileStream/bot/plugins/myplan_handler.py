from pyrogram import Client, filters
from pyrogram.types import Message
from bot.premium_utils import is_premium, get_expiry, get_remaining_days

@Client.on_message(filters.command("myplan"))
async def myplan_handler(client, message: Message):
    user_id = str(message.from_user.id)
    if is_premium(user_id):
        expiry = get_expiry(user_id)
        days_left = get_remaining_days(user_id)
        await message.reply_text(f"You are a premium user. ✅\nYour access expires in {days_left} days (on {expiry}).")
    else:
        await message.reply_text("You are not a premium user ❌\nUse /plan to upgrade your access.")
