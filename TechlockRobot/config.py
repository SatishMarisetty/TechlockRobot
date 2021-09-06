# Create a new config.py or rename this to config.py file in same dir and import,  then extend this class.
import json
import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


def get_user_list(config, key):
    with open("{}/TechlockRobot/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID =  5099305 # integer value, dont use ""
    BOT_ID = 1476311937
    API_HASH = "01bbc17714f0bc7be8ae7649bd1e192c"
    ARQ_API = "APOEQJ-SMZPYL-PNOTUX-CBDOTI-ARQ"
    TOKEN = "1476311937:AAHjwyUrXY8Kv1vB-UkkG7ovkzAAfOTfkQw"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1060459378 # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "SatishMarisettyTG"
    SUPPORT_CHAT = "techlockgram_bot"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001497115469
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001399944384
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    DATABASE_URL = "postgres://fsvdwsju:VMcn6ORRnil1rWqyRVCyyMiXuClmZHHE@queenie.db.elephantsql.com/fsvdwsju"  # needed for any database modules # its "URI" and not "URL" as herok and similar ones only accept it as such
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    MONGO_DB = "SaitamaRobot"
    MONGO_DB_URI = "mongodb+srv://SATISH:SATISH123@cluster0.3haan.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    MONGO_PORT = 27017
    REDIS_URL = "redis://SATISH1234:Satish1234$@redis-10438.c10.us-east-1-3.ec2.cloud.redislabs.com:10438/SATISH1234"
    STRING_SESSION = "1AZWarzYBuwnFf1Yajr_Ta0CZPbf5rA_YGpQFlKTJQiTlNv3eM5oi3biDp8zRQ4jVqdXzrnMZDYqRsBWdR3VkofwJjrqBZi_MSaaAo1Y9yTNpSfrK6PbWIYlirtvyFVMfycpIFvZUdn8pxBIrfa8ko4JthXVzHx9Xbh-qGp9T7TOnmS1z6mNifmvM7dwuywiyZeA1jpHrjASbSyNpga-INHEYAKGUOqHtwxGiVjc4pQImpPOVh1N5PL1hNpgJhVgFAI2buUTKDqVOyAVUNtffDx0V7hZBuOMoaj_n5x8iBK82OuXyIF5W8JeM503WtcpIsL1E2EYWtg3mwHYtdfnJKxkj_9CVfN8="
    TEMP_DOWNLOAD_DIRECTORY = "./"
    SPAMWATCH_API = "Rz_AQyrEv7IE8sCwEgKtrLqAhia~ICOPZIo2y_B_lXewOHodbg8O2jXwebllUUhV"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = set(int(x) for x in getenv("DEV_USERS", "").split())
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    ENV = "ANYTHING"
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_CHATS = True
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "BTWJL4YF4J6E69D0"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "M53Y1JYT0JVT"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "awoo"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
