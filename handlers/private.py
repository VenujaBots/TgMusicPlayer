from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import other_filters2

STICKER = "CAACAgQAAx0CQ2C8OgACsqNhiisoWUQROohUrpaGzDsHsot3dQACVxYAAtqjlSznBlAxygdMwyIE"


START_TEXT = """
👋 Hey {} I am an Vnd Groups Music Bot, Made by @Venuja_Sadew, I let you play music in your group's voice chat.

**Commands** /dsong Anthem and /splay anthem **Working in Groups**

Join @vndbotsupport. 🔥
"""

START_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Group ', url="https://t.me/vndbotsupport"),
        InlineKeyboardButton('YTChannle', url="https://www.youtube.com/channel/UCL8PI42TZ_uaQWVVKUJx9Eg")
        InlineKeyboardButton('➕ Add Me To Your Group ➕', url="http://t.me/VndGroupMusicBot?startgroup=true")
        ]]
  
)

@Client.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_sticker(STICKER)
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        reply_markup=START_BUTTON,
        disable_web_page_preview=True,
        quote=True
    )

