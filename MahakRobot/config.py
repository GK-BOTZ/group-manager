
class Config(object):
    LOGGER = True

    #####

    ANILIST_CLIENT = "8679"
  
    ANILIST_SECRET =  "NeCEq9A1hVnjsjZlTZyNvqK11krQ4HtSliaM7rTN"
  
    API_ID =  ""
   
    API_HASH = ""
   
    TOKEN =  ""
  
    OWNER_ID =  "6454209118" 

    OWNER_USERNAME =  "itz_Asuraa"
    
    SUPPORT_CHAT =  "AsuraaSupport"
   
    START_IMG =  "https://graph.org/file/eaa3a2602e43844a488a5.jpg"

    JOIN_LOGGER =  "-1002100219353"
   
    EVENT_LOGS =   "-1002100219353"
  
    ERROR_LOGS =  "-1002100219353"

    MONGO_DB_URI=  ""
   
    LOG_CHANNEL =  "-1002100219353"
   
    BOT_USERNAME = "" , "MahakxBot"
   
    DATABASE_URL =  ""

    CASH_API_KEY =  ""
    
    TIME_API_KEY =  ""

    SPAMWATCH_API =  ""
    
    SPAMWATCH_SUPPORT_CHAT =  "AsuraaSupport"
    
    WALL_API =  ""
    
    REM_BG_API_KEY =  ""
    
    OPENWEATHERMAP_ID =  ""

    BAN_STICKER =  "CAACAgEAAxkBAAIrTWYljyX_lqcubkAzg0jy45CRvxAFAAKvAgACrLHoRU50VVvh3xWwNAQ"

    HEROKU_APP_NAME =  ""

    HEROKU_API_KEY =  ""

    LASTFM_API_KEY =  "
    "
    
    # Optional fields
    
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

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

  