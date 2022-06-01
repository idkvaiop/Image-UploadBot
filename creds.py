import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Credentials:
    BOT_TOKEN = os.getenv("BOT_TOKEN")  # from @botfather
    API_ID = int(os.getenv("API_ID"))  # API ID from Telegram Web
    API_HASH = os.getenv("API_HASH")  # API Hash from Telegram Web
