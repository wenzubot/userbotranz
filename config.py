import os
from os import getenv
from dotenv import load_dotenv
from distutils.util import strtobool as sb
from base64 import b64decode


load_dotenv()



DEVS = [
    7903962929, # Ranz
    7269190670, # vortex
]


GCAST_BLACKLIST = [
    -1002929292773,  # CHANNEL RANZ ( NEW ) 
    -1002921687791,  # GROUP C WEB FREE
    -1002673312182,  # SHARE SC UBOT
]


class Config:
    # Telegram App KEY and HASH
    API_KEY = int(getenv("API_KEY") or 0)
    API_HASH = str(getenv("API_HASH") or None)

    # Inline bot helper
    BOT_TOKEN = getenv("BOT_TOKEN", None)
    BOT_USERNAME = getenv("BOT_USERNAME", None)

    OPENAI_API_KEY = getenv("OPENAI_API_KEY", None)

    SUDO_USERS = {int(x) for x in getenv("SUDO_USERS", "").split()}
    BL_CHAT = {int(x) for x in getenv("BL_CHAT", "").split()}
    BLACKLIST_GCAST = {
        int(x) for x in getenv(
            "BLACKLIST_GCAST",
            "").split()}

    # For Blacklist Group Support
    BLACKLIST_CHAT = getenv("BLACKLIST_CHAT", None)
    if not BLACKLIST_CHAT:
        BLACKLIST_CHAT = [-1002929292773, -1002921687791, -1002673312182]

    # Userbot Session String
    STRING_SESSION = getenv("STRING_SESSION", None)

    # Logging channel/group ID configuration.
    BOTLOG_CHATID = int(getenv("BOTLOG_CHATID", "0"))

    # Load or No Load modules
    LOAD = getenv("LOAD", "").split()
    NO_LOAD = getenv("NO_LOAD", "").split()

    # Bleep Blop, this is a bot ;)
    PM_AUTO_BAN = sb(getenv("PM_AUTO_BAN", "True"))
    PM_LIMIT = int(getenv("PM_LIMIT", 6))

    # Custom Handler command
    CMD_HANDLER = getenv("CMD_HANDLER") or "."
    SUDO_HANDLER = getenv("SUDO_HANDLER", r"$")

    # Support
    GROUP = getenv("GROUP", "AyiinChats")
    CHANNEL = getenv("CHANNEL", "AyiinChannel")

    # Heroku Credentials for updater.
    HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)
    HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)

    # JustWatch Country
    WATCH_COUNTRY = getenv("WATCH_COUNTRY", "ID")

    # Github Credentials for updater and Gitupload.
    GIT_REPO_NAME = getenv("GIT_REPO_NAME", None)
    GITHUB_ACCESS_TOKEN = getenv("GITHUB_ACCESS_TOKEN", None)

    # Custom (forked) repo URL for updater.
    UPSTREAM_REPO_URL = getenv("UPSTREAM_REPO_URL", "https://github.com/AyiinXd/Ayiin-Userbot.git")

    # Custom Name Sticker Pack
    S_PACK_NAME = getenv("S_PACK_NAME", None)

    # SQL Database URI
    DB_URI = getenv("DATABASE_URL", None)
    DATABASE_PATH = os.path.join("ayiin.db")

    # OCR API key
    OCR_SPACE_API_KEY = getenv("OCR_SPACE_API_KEY", None)

    # remove.bg API key
    REM_BG_API_KEY = getenv("REM_BG_API_KEY", "jK9nGhjQPtd2Y5RhwMwB5EMA")

    # Chrome Driver and Headless Google Chrome Binaries
    CHROME_DRIVER = getenv("CHROME_DRIVER") or "/usr/bin/chromedriver"
    GOOGLE_CHROME_BIN = getenv(
        "GOOGLE_CHROME_BIN") or "/usr/bin/google-chrome"

    # OpenWeatherMap API Key
    OPEN_WEATHER_MAP_APPID = getenv("OPEN_WEATHER_MAP_APPID", None)
    WEATHER_DEFCITY = getenv("WEATHER_DEFCITY", "Jakarta")

    # Anti Spambot Config
    ANTI_SPAMBOT = sb(getenv("ANTI_SPAMBOT", "False"))
    ANTI_SPAMBOT_SHOUT = sb(getenv("ANTI_SPAMBOT_SHOUT", "False"))

    # untuk perintah teks costum .alive
    ALIVE_TEKS_CUSTOM = getenv(
        "ALIVE_TEKS_CUSTOM",
        "Hey, Saya pengguna Ayiin-Userbot")

    # Default .alive name
    ALIVE_NAME = getenv("ALIVE_NAME", "AyiinXd")

    # Custom Emoji Alive
    ALIVE_EMOJI = getenv("ALIVE_EMOJI", "✧")

    # Time & Date - Country and Time Zone
    COUNTRY = str(getenv("COUNTRY", "ID"))
    TZ_NUMBER = int(getenv("TZ_NUMBER", 1))

    # Clean Welcome
    CLEAN_WELCOME = sb(getenv("CLEAN_WELCOME", "True"))

    # Zipfile module
    ZIP_DOWNLOAD_DIRECTORY = getenv("ZIP_DOWNLOAD_DIRECTORY", "./zips")

    # bit.ly module
    BITLY_TOKEN = getenv("BITLY_TOKEN", None)

    # Bot version
    BOT_VER = getenv("BOT_VER", "5.0.0")

    # Default .alive logo
    ALIVE_LOGO = (getenv("ALIVE_LOGO")
                or "https://files.catbox.moe/k2fxyq.jpeg")

    INLINE_PIC = (getenv("INLINE_PIC")
                or "https://files.catbox.moe/k2fxyq.jpeg")

    # Picture For VCPLUGIN
    PLAY_PIC = (getenv("PLAY_PIC")
                or "https://files.catbox.moe/k2fxyq.jpeg")

    QUEUE_PIC = (getenv("QUEUE_PIC")
                or "https://files.catbox.moe/k2fxyq.jpeg")

    DEFAULT = list(map(int, b64decode("MTkwNTA1MDkwMw==").split()))

    TEMP_DOWNLOAD_DIRECTORY = getenv(
        "TMP_DOWNLOAD_DIRECTORY", "./downloads/")

    # Deezloader
    DEEZER_ARL_TOKEN = getenv("DEEZER_ARL_TOKEN", None)

    # NSFW Detect DEEP AI
    DEEP_AI = getenv("DEEP_AI", None)
    
    # Sosmed Vars
    SOSMED_API_KEY = getenv("SOSMED_API_KEY", None)
    SOSMED_SECRET = getenv("SOSMED_SECRET", None)


var = Config()
