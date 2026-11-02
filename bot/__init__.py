import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID", "34042473"))
    API_HASH = os.environ.get("API_HASH", "10c6e1b569bc97e59e089711fc911d0d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "9216116082:AAH2BUlVgDwxEaywKF3cJ7cHjGCkeQr7nTE")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Restlive21bot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
