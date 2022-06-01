import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Credentials:
    OWNER_USERNAME = os.getenv("OWNER_USERNAME") # Your Telegram Username
    START_PIC = os.getenv("START_PIC") # A Telegraph link of the pic to display when give /start command
    BOT_TOKEN = os.getenv("BOT_TOKEN")  # from @botfather
    API_ID = int(os.getenv("API_ID"))  # API ID from Telegram Web
    API_HASH = os.getenv("API_HASH")  # API Hash from Telegram Web
