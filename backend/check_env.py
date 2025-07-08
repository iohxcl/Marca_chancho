from dotenv import load_dotenv
import os

load_dotenv()
print("App ID:", os.getenv("ALIEXPRESS_APP_ID"))