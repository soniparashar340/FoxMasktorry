try:
    from .ExecVars import ExecVars
except:

    class ExecVars:
        # Set true if its VPS
        IS_VPS = False

        API_HASH = "fda406cc4f648c303a0fb77255f2a026"
        API_ID = 2712818
        BOT_TOKEN = "5510665590:AAFcFzMFCMhFJXqGthXX7ZGMlipMlUbc4tw"
        BASE_URL_OF_BOT = "https://t.me/ttl_x_ft_bot"

        # Edit the server port if you want to keep it default though.
        SERVPORT = 80

        # ALLOWED USERS [ids of user or supergroup] seperate by commas
        ALD_USR = [-1001511877602, -1001154122336]
        OWNER_ID = 1517181772

        # Google Drive Index Link should include the base dir also See readme for more info
        GD_INDEX_URL = False

        # Time to wait before edit message
        EDIT_SLEEP_SECS = 5

        # Telegram Upload Limit (in bytes)
        TG_UP_LIMIT = 1700000000

        # Should force evething uploaded into Document
        FORCE_DOCUMENTS = False

        # Chracter to use as a completed progress
        COMPLETED_STR = "▰"

        # Chracter to use as a incomplete progress
        REMAINING_STR = "▱"

        # DB URI for access
       # DATABASE_URL = (
            ""
        )

        # UNCOMMENT THE BELOW LINE WHEN USING CONTAINER AND COMMENT THE UPPER LINE
        DATABASE_URL = "postgres://xplqssywfuztot:8e5b57b98783704be0cb5577225d779db3d97f1c2a21d7ef7819f357a6879dbc@ec2-44-194-54-123.compute-1.amazonaws.com:5432/d826nb3pb6rnkg"

        # MEGA CONFIG
        MEGA_ENABLE = True
        MEGA_API = "s5Y10S4b"
        MEGA_UNAME = "cooldudex0369@gmail.com"
        MEGA_PASS = "parasharsoni"

        # The base direcory to which the files will be upload if using RCLONE
        RCLONE_BASE_DIR = "/"
        
        # Instagram Credentials Stuff [( if you want InstaDL to work :)]
        INSTA_UNAME = ""
        INSTA_PASS = ""

        # This value will be considered only if Rclone is True - this may be defied now ;)
        # Cuz at least one needs to be Ture at a time either RCLONE or Leech.
        LEECH_ENABLED = True

        # Will be enabled once its set
        # For vps change it to True if config loaded
        RCLONE_ENABLED = False

        # If the user fails to select whether to use rclone or telegram to upload this will be the deafult.
        DEFAULT_TIMEOUT = "leech"

        # For vps set path here or you can use runtime too
        RCLONE_CONFIG = False

        # Name of the RCLONE drive from the config
        DEF_RCLONE_DRIVE = ""

        # Max size of a playlist that is allowed (Number of videos)
        MAX_YTPLAYLIST_SIZE = 20

        # Max size of the torrent allowed
        MAX_TORRENT_SIZE = 10

        # Custom Trackers for QBT..
        ADD_CUSTOM_TRACKERS = True
        TRACKER_SOURCE = "https://raw.githubusercontent.com/XIU2/TrackersListCollection/master/all.txt"

        # Set this to your bot username if you want to add the username of your bot at the end of the commands like
        # /leech@TorToolkitBot so the value will be @TorToolkitBot
        BOT_CMD_POSTFIX = "@TTK_X_FT_BOT"

        # Time out for the status Delete.
        STATUS_DEL_TOUT = 20

        # Allow the user settings to be accessed in private
        USETTINGS_IN_PRIVATE = False

        # Torrent max time to collect metadata in seconds
        TOR_MAX_TOUT = 180

        # This is to stop someone from abusing the system by imposing the limit
        # [<GBs of total torrent sapce>, <Number of youtube videos allowed to download>, <Number of youtube playlists allowed to download>]
        USER_CAP_ENABLE = False
        USER_CAP_LIMIT = [50, 10, 2]

        # No need to worry about these
        # CHANGE THESE AT YOUR RISK
        LOCKED_USERS = False
        RSTUFF = False
        FORCE_DOCS_USER = False
        FAST_UPLOAD = True
        METAINFO_BOT = False
        EXPRESS_UPLOAD = True
