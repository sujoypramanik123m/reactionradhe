from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("repo"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_photo(
        chat_id=msg.chat.id,
        photo="https://envs.sh/Amn.jpg",
        caption=f"""**  ʜᴇʏ  {msg.from_user.mention}  ✤,

✪ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ˹ ᴛᴏᴘᴘᴇʀs ʀᴇᴀᴄᴛɪᴏɴ ʙᴏᴛ ✪
 
 ❍ • ʙsᴅᴋ ᴋᴇᴛᴀɴɪ ʙᴀʀʀ ʀᴇᴘᴏ ʟᴇɢᴀ ◉‿◉ •
 
 ❍ • ᴘᴇʜʟᴇ ʀᴇᴘᴏ ʜᴇ ᴅᴀ ᴅᴇʏᴀ ʜᴜ•
 
 ❍ • ᴄʜᴜᴘ ᴄʜᴜᴘ ʙᴏᴛ ʟᴇᴋᴇ ɴɪᴋᴀʟ •
 
 ❍ • ᴀᴜʀ ʀᴇᴘᴏs ᴛᴏ ɴᴀʜɪ ᴍɪʟᴇɢᴀ ʙᴇᴛᴀ ⊂◉‿◉ •
 
 ❍ • ᴀɢʀ ᴄʜᴀʜɪʏᴇ ᴛᴏ ɴɪʜᴀʟ ᴋᴏ ᴘᴀᴘᴀ ʙᴏʟɴᴀ ᴘᴀᴅᴇɢᴀ •
 
 ❍ • ʀᴀᴅʜᴇ ʀᴀᴅʜᴇ • ** """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="❍ 𝐀ᴅᴅ 𝐌ᴇ 𝐘ᴏᴜʀ 𝐆ʀᴏᴜᴘ ❍", url="https://t.me/ReactionCloner_bot?startgroup=true")
                ],
                [
                    InlineKeyboardButton(text="❍ 𝐒ᴛʀɪɴɢ ❍", url="https://t.me/StringSession_GenBot")
                ],
                [
                    InlineKeyboardButton("❍ 𝐒ᴜᴘᴘᴏʀᴛ ❍", url="https://t.me/supertoppers0"),
                    InlineKeyboardButton("❍ 𝐔ᴘᴅᴀᴛᴇ ❍", url="https://t.me/supertoppers")
                ],
                [
                    InlineKeyboardButton("❍ 𝐀ʟʟ 𝐁ᴏᴛ𝐬 ❍", url="https://t.me/supertoppers"),
                    InlineKeyboardButton("❍ 𝐌ᴜ𝐬ɪᴄ 𝐁ᴏᴛ ❍", url="https://t.me/MusicToppersBot")
                ],
                [
              InlineKeyboardButton("❍ 𝐌ᴜ𝐬ɪᴄ 𝐁ᴏᴛ ❍", url=f"https://t.me/MusicToppersBot"),
              InlineKeyboardButton("︎❍ 𝐌ᴜ𝐬ɪᴄ 𝐁ᴏᴛ ❍", url=f"https://t.me/MusicToppersBot"),
              ],
              [
              InlineKeyboardButton("❍ 𝐌ᴜ𝐬ɪᴄ 𝐁ᴏᴛ ❍", url=f"https://t.me/MusicToppersBot"),
InlineKeyboardButton("❍ 𝐂ʜᴀᴛ 𝐁ᴏᴛ ❍", url=f"https://t.me/Chatbot_ToppersBot"),
],
[
InlineKeyboardButton("❍ 𝐒ᴛʀɪɴɢ 𝐁ᴏᴛ ❍", url=f"https://t.me/StringSession_GenBot"),
InlineKeyboardButton("❍ 𝐂ᴀᴍᴇʀᴀ 𝐇ᴀᴄᴋ ❍", url=f"https://t.me/CameraHack_Robot"),
],
[
              InlineKeyboardButton("❍ 𝐏ʜɪ𝐬ʜɪɴɢ 𝐁ᴏᴛ ❍", url=f"https://t.me/Rishabh_hackbot"),
              InlineKeyboardButton("❍ 𝐅ɪʟᴇ 𝐒ʜᴀʀɪɴɢ ❍", url=f"https://t.me/Share_file_robot"),
              ],
              [
              InlineKeyboardButton("❍ 𝐂ʜᴀᴛ 𝐈ɴғᴏ ❍", url=f"https://t.me/supertoppers"),
InlineKeyboardButton("❍ 𝐌ᴏᴠɪᴇ ʙᴏᴛ ❍", url=f"https://t.me/supertoppers"),
],
[
InlineKeyboardButton("❍ 𝐅ᴏɴᴛ 𝐂ʜᴀɴɢᴇ ❍", url=f"https://t.me/supertoppers"),
InlineKeyboardButton("❍ 𝐂ʜᴀᴛ 𝐆ᴘᴛ ❍", url=f"https://t.me/supertoppers"),
]               
            ]
        )
    )
