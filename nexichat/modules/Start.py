from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message



def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_photo(
        chat_id=msg.chat.id,
        photo="https://files.catbox.moe/y9c134.jpg",
        caption=f"""❍ ʜᴇʏ  {msg.from_user.mention}  ✤,
❍ ɪ ᴀᴍ {me2},

❍ ɪ'ᴍ ʏᴏᴜʀ ʀᴇᴀᴄᴛɪᴏɴ ʙᴏᴛ! I'ʟʟ ʀᴇᴀᴄᴛ ᴛᴏ ᴇᴠᴇʀʏ ᴍᴇssᴀɢᴇ ɪɴ ɢʀᴏᴜᴘs, ᴄʜᴀɴɴᴇʟs, ᴀɴᴅ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛs ᴡɪᴛʜ ᴀ ᴇᴍᴏɪɪ

❍ ɪғ ʏᴏᴜ ɴᴇᴇᴅ ᴀɴʏ ʜᴇʟᴘ, ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ ᴏᴡɴᴇʀ: [ᯓ𓆰𝅃 ꯭꯭↬꯭ᬃ꯭ ⃪꯭ ꯭⁢⁣⁤⁣⁣⁢⁣⁤⁢⁤⁣⁢⁤⁣⁤᪳᪳🇷꯭𝚰𝛅꯭꯭ʜ꯭֟፝፝֟ᴜ ꯭꯭༗꯭»꯭݅݅݅݅𓆪 ](t.me/rishu1286) !""",
        reply_markup=InlineKeyboardMarkup(
            [
 
                [
                    InlineKeyboardButton("˹ sᴜᴘᴘᴏʀᴛ ˼", url="https://t.me/rishu1286"),
                   ], 
            [
InlineKeyboardButton("˹ ᴜᴘᴅᴀᴛᴇs ˼", url="https://t.me/rishu1286")
                ]
                                
            ]
        )
    )