from binance.client import Client
from config import API_KEY, API_SECRET

client = Client(
    api_key=API_KEY,
    api_secret=API_SECRET,
    testnet=True
)
