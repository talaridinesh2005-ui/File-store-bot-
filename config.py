import os
import logging
from logging.handlers import RotatingFileHandler




BOT_TOKEN = os.environ.get("BOT_TOKEN", "8389235583:AAEV_W5gCVrs0NcbwvybX9ES2cHS6YdD8SM")
API_ID = int(os.environ.get("API_ID", "28961091"))
API_HASH = os.environ.get("API_HASH", "fa3796dbdec1efdf151aca5f14815d06")


OWNER_ID = int(os.environ.get("OWNER_ID", "8475661555"))
DB_URL = os.environ.get("DB_URL", "mongodb+srv://tdanimehub_db_user:cPdMT253KSZpE11Z@helper.wallqjf.mongodb.net/?retryWrites=true&w=majority&appName=Helper")
DB_NAME = os.environ.get("DB_NAME", "tdanimehub")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003314714851")

FORCE_SUB_CHANNEL_1 = int(os.environ.get("FORCE_SUB_CHANNEL_1", "0"))

FORCE_SUB_CHANNEL_2 = int(os.environ.get("FORCE_SUB_CHANNEL_2", "0"))

FORCE_SUB_CHANNEL_3 = int(os.environ.get("FORCE_SUB_CHANNEL_3", "0"))

FORCE_SUB_CHANNEL_4 = int(os.environ.get("FORCE_SUB_CHANNEL_4", "0"))

START_PIC = os.environ.get("START_PIC", "https://ibb.co/CK3TrSsj")
F_PIC = os.environ.get("FORCE_PIC", "https://ibb.co/CK3TrSsj")

FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "1800")) # auto delete in seconds


PORT = os.environ.get("PORT", "8050")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))



try:
    ADMINS=[1573111356]
    for x in (os.environ.get("ADMINS", "8475661555").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")









CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', None) == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"







USER_REPLY_TEXT = "❌Sry You can't Able to Message me !\n\n» My Owner 👉 "

START_MSG = os.environ.get("START_MESSAGE", "<b>Hi {first} Friend I am a Advance File Store bot 😈 \n\n I was created by 👉 @TD_Public_Bots </b>")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "𝐒𝐨𝐫𝐫𝐲 {first} You must join the given channels ..\n\n 𝐒𝐨 please join and  “𝐍𝐨𝐰 𝐂𝐥𝐢𝐜𝐤 𝐡𝐞𝐫𝐞” 𝐛𝐮𝐭𝐭𝐨𝐧....!")




ADMINS.append(OWNER_ID)
ADMINS.append(1573111356)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   

class Txt(object):
    about = f"""<b>😈 My Name :</b> <a href=''>[AW] File store bot 😈 </a>
<b>📝 Owner :</b> <a href='https://t.me/TD_Public_Bots'>TD Public Bots</a>
<b>📡 update  :</b> <a href='https://t.me/TD_Public_Bots'>TD Public Bots</a>
<b>💫 YouTube :</b> <a href='https://youtube.com/@tdbotdev?si=j3HVY4E69-C4ZDcw'>channel Link</a>
<b> 🧩 Animes :</b> <a href='https://t.me/Team_TD_Links'>channel Link</a>
<b>♻️ Discussion :</b> <a href='https://t.me/Team_TD_Links'>Group Linkr</a>
    
<b>😈 Bot Made By :</b> @TD_Public_Bots"""


# @TD_Public_Bots
# Don't Remove Credit!!!
#YouTube channel link https://youtube.com/@tdbotdev?si=j3HVY4E69-C4ZDcw
# Telegram Channel @TD_Public_Bots
# Developer @TD_Public_Bots
