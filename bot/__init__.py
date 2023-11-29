import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID", "27385225"))
    API_HASH = os.environ.get("API_HASH", "841ac6a2c18172854b93bcfdadfdebb5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5820508322:AAGqmvdR5xg044Ua_op83LDBTMy48ZiaHG8")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "JunedMarkINFINITY_bot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
