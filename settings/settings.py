import os
from dotenv import load_dotenv

load_dotenv()

class Settings():
    api_key = os.getenv("api_key")
    gmail_password = os.getenv("gmail_password")
    api_astro_key = os.getenv("api_astro_key")

settings = Settings()