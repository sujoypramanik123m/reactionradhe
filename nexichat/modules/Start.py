from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from nexichat import nexichat

@nexichat.on_message(filters.command("start"))
async def start_message(client: Client, message: Message):
    # Sending a photo along with the reply text
    await message.reply_photo(
        photo="https://envs.sh/Ylh.jpg",  # Replace with the actual photo URL or local file path
        caption=(
            f"""**❖ нᴇʏ  {message.from_user.first_name} !, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ !
━━━━━━━━━━━━━━━━━━━━━━━━━━━

● ɪ ᴀᴍ  {(await client.get_me()).mention} !


⦿━━━━━━━━━━━━━━━━━━━━━⦿
❍ •  ɪ'ʟʟ ʀᴇᴀᴄᴛ ᴛᴏ ᴇᴠᴇʀʏ ᴍᴇssᴀɢᴇ  •
│❍ • ʙᴇsᴛ ǫᴜɪʟɪᴛʏ ᴍᴜsɪᴄ sᴏᴜɴᴅ •
│❍ • ɴᴏ ʟᴀɢs + ɴᴏ ᴀᴅs •
│❍ • 24x7 ᴏɴʟɪɴᴇ sᴜᴘᴘᴏʀᴛ •
│❍ • ᴀ ᴘᴏᴡᴇʀғᴜʟ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ •
❍ • ɪ ʜᴀᴠᴇ sᴘᴇᴄɪᴀʟ ғᴇᴀᴛᴜʀᴇs •
⦿━━━━━━━━━━━━━━━━━━━━━⦿

❖ ᴛʜɪs ɪs ᴘᴏᴡᴇʀғᴜʟ ʙᴏᴛ, ғᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ  •\n\n
            You can make your bot by /clone😁**"""
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("❖ ᴀᴅᴅ ᴍᴇ ɪɴ ɢʀᴏᴜᴘ ❖", url="https://t.me/ReactionByBot?startgroup=true")],
                [InlineKeyboardButton("• sᴜᴘᴘᴏꝛᴛ •", url="https://t.me/ur_rishu_143")]
            ]
        )
    )