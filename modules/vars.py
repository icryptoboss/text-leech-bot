import os

API_ID    = os.environ.get("API_ID", "1931963")
API_HASH  = os.environ.get("API_HASH", "86fdcaf35d9cd6bfb18d990f96e855bd")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "1892684371:AAF3ojvVCFkicWXhusN6N_uPwo-zelbDPQI") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
