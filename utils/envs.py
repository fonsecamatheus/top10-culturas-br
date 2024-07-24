import os

from dotenv import load_dotenv

load_dotenv()
DEST_DB = os.getenv(r'DEST_DB')
