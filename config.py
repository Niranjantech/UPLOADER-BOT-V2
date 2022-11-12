import os

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5700794069:AAEX53T5GLlimcjBPXI9AF6RU6yqrrfuRUE")
    
    API_ID = int(os.environ.get("API_ID", 952608))
    
    API_HASH = os.environ.get("API_HASH", "8d8d0ad8e3d4bcd54420190f57da78ad")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 50000000

    TG_MAX_FILE_SIZE = 2097152000

    FREE_USER_MAX_FILE_SIZE = 50000000
    
    CHUNK_SIZE = int(128)

    HTTP_PROXY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 3600
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "818269274"))

    SESSION_NAME = "UploadLinkToFileBot"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://NiruTech:Niru#123@cluster0.itmxbk1.mongodb.net/?retryWrites=true&w=majority")

    MAX_RESULTS = "50"
