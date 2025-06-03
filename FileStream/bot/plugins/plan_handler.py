from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

qr_url = "https://your-qr-image-link-here"
payment_link = "https://t.me/yourusername"

@Client.on_message(filters.command("plan"))
async def plan_handler(client, message: Message):
    await message.reply_photo(
        photo=qr_url,
        caption=(
            "📜 Premium Plans:\n\n"
            "🟢 Trial – 7 days – ₹FREE\n"
            "🟢 30 Days – ₹XYZ\n\n"
            "👇 Scan the QR above to pay:"
        ),
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📤 Send Payment Here", url=payment_link)]
        ])
    )
