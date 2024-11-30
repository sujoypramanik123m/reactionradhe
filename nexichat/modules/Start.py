from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from nexichat import nexichat

@nexichat.on_message(filters.command("start"))
async def start_message(client: Client, message: Message):
    # Sending a photo along with the reply text
    await message.reply_photo(
        photo="https://envs.sh/Ylh.jpg",  # Replace with the actual photo URL or local file path
        caption=(
            f"""**Hello {message.from_user.first_name}! 👋\n\n
            I'm your Reaction Bot! I'll react to every message in groups, channels, and private chats with a 👍 emoji.\n\n
            Add me to your group or channel and watch me in action! 🚀\n\n
            You can make your bot by /clone😁**"""
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("❖ ᴀᴅᴅ ᴍᴇ ɪɴ ɢʀᴏᴜᴘ ❖", url="https://t.me/ReactionByBot?startgroup=true")],
                [InlineKeyboardButton("• sᴜᴘᴘᴏꝛᴛ •", url="https://t.me/ur_rishu_143")]
            ]
        )
    )