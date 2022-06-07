import os
import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from creds import Credentials
from telegraph import upload_file

logging.basicConfig(level=logging.WARNING)


akhil = Client(
    "Image Upload Bot",
    bot_token=Credentials.BOT_TOKEN,
    api_id=Credentials.API_ID,
    api_hash=Credentials.API_HASH
)


@akhil.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        text=f"Hello,{message.from_user.mention}, I am *Akira* Telegraph Uploader Bot which simply creates a *link* of the media sent in my PM.\n*How it works?*\nJust send me /start then provide me a image to create a link... Maintained by [Akira Dev](https://telegram.dog/Akira_News).",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Updates ", url=f"https://telegram.dog/Akira_News"
                    ),
                    InlineKeyboardButton(
                        text="Chat with us",
                        url=f"https://telegram.dog/Hell_X_Chats",
                    )
                ]
            ]
        )
    )
    

@akhil.on_message(filters.photo)
async def getimage(client, message):
    dwn = await message.reply_text("Connecting to the server....", True)
    img_path = await message.download()
    await dwn.edit_text("Uploading...")
    try:
        url_path = upload_file(img_path)[0]
    except Exception as error:
        await dwn.edit_text(f"Something went wrong 😐\n{error}")
        return
    await dwn.edit_text(
        text=f"<b>Link :-</b> <code>https://telegra.ph{url_path}</code>",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="get the telegra.ph image", url=f"https://telegra.ph{url_path}"
                    ),
                    InlineKeyboardButton(
                        text="share the telegra.ph image",
                        url=f"https://telegram.me/share/url?url=https://telegra.ph{url_path}",
                    )
                ]
            ]
        )
    )
    os.remove(img_path)


tgraph.run()
