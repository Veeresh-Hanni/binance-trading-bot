from dotenv import load_dotenv
import os

if not os.path.exists("./logs"):
    os.makedirs("./logs")

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")