import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ENV_MODEL_NAME = os.getenv("ENV_MODEL_NAME")