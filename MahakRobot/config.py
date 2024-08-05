
class Config(object):
    LOGGER = True

    #####

    ANILIST_CLIENT = "8679"
  
    ANILIST_SECRET =  "NeCEq9A1hVnjsjZlTZyNvqK11krQ4HtSliaM7rTN"
  
    API_ID =  "28689465"
   
    API_HASH = "fedd61d8e38f8afaed63c01b8438cbe4"
   
    TOKEN =  "6911638837:AAGr-N1or_-anS4fd6o4oAJQr8pqb4onZtg"
  
    OWNER_ID =  "6454209118" 

    OWNER_USERNAME =  "itz_Asuraa"
    
    SUPPORT_CHAT =  "Ravan_Lankaa"
   
    START_IMG =  "https://graph.org/file/eaa3a2602e43844a488a5.jpg"

    JOIN_LOGGER =  "-1002100219353"
   
    EVENT_LOGS =   "-1002100219353"
  
    ERROR_LOGS =  "-1002100219353"

    MONGO_DB_URI=  "mongodb+srv://BWFMUSIC:BWFMUSIC@cluster0.xwnup2l.mongodb.net/?retryWrites=true&w=majority"
   
    LOG_CHANNEL =  "-1002100219353"
   
    BOT_USERNAME = "" , "MahakxBot"
   
    DATABASE_URL =  "postgresql://asuraa_user:HWv7mxtIxuFbdq9nFUYPmKk6wgDWZxlU@dpg-cq8babmehbks738glhs0-a/asuraa"

    CASH_API_KEY =  "V48U2FLLKRHSVD4X"
    
    TIME_API_KEY =  "1CUBX1HXGNHW"

    SPAMWATCH_API =  "3624487efd8e4ca9c949f1ab99654ad1e4de854f41a14afd00f3ca82d808dc8c"
    
    SPAMWATCH_SUPPORT_CHAT =  "Ravan_Lankaa"
    
    WALL_API =  "2455acab48f3a935a8e703e54e26d121"
    
    REM_BG_API_KEY =  "xYCR1ZyK3ZsofjH7Y6hPcyzC"
    
    OPENWEATHERMAP_ID =  "887da2c60d9f13fe78b0f9d0c5cbaade"

    BAN_STICKER =  "CAACAgEAAxkBAAIrTWYljyX_lqcubkAzg0jy45CRvxAFAAKvAgACrLHoRU50VVvh3xWwNAQ"

    HEROKU_APP_NAME =  ""

    HEROKU_API_KEY =  ""

    LASTFM_API_KEY =  "8f3315b5806c21004b2822f07825187d"
    
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

  