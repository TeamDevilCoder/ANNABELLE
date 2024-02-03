
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 12227067 # integer value, dont use ""
    API_HASH = "b463bedd791aa733ae2297e6520302fe"
    TOKEN = "6582690640:AAHvFJleFjzegJHMIA4MwExyAsjufSGRPpA"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 5360305806 # If you dont know, run the bot and do /id in your private chat with it, also an integer
    CHANNEL = "dcbotz" 
    SUPPORT_CHAT = "DC_BOT_Support"  # Your own group for support, do not add the @
    START_IMG = "https://graph.org/file/955c11885d9572ed684a6.jpg"
    EVENT_LOGS = ("-1002062281574")
    JOIN_LOGGER = ("-1001531647177")  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    MONGO_DB_URI= "mongodb+srv://MusicRoboXBot:3yDvdQqJfWkfQxXP@musicroboxbot.jbt7hzl.mongodb.net/?retryWrites=true&w=majority"
    # RECOMMENDED
    DATABASE_URL = "postgres://aguhselxrktjou:8041b95575ab3bfa5376dc1d3919579d22f1ee97a7ad3689030085cbcbe5d2cf@ec2-44-206-204-65.compute-1.amazonaws.com:5432/d4d6drik95opt0"  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        "PNNU99H3W9KDLKVM"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "9HK7J0H25AKQ"
    # Get your API key from https://timezonedb.com/api
    OPENAI_KEY = "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"
    # Optional fields
    CHATBOT_API="" # get it from @FallenChat_Bot using /token
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = ["5360305806","6109442416","736041718"]  # User id of sudo users
    DEV_USERS = ["5360305806","6109442416","736041718","5916859256","5946148765"]  # User id of dev users
    DEMONS = ["5360305806","6109442416","736041718"]  # User id of support users
    TIGERS = ["5360305806","6109442416","736041718"]  # User id of tiger users
    WOLVES = ["5360305806","6109442416","736041718"]  # User id of whitelist users
    DEVIL = 5946148765
    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
