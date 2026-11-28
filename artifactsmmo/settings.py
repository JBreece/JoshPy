import os
import json
from dotenv import load_dotenv

# 1. Load the API key from .env
load_dotenv()
API_TOKEN = os.getenv("TOKEN")

# 2. Load the lists/settings from config.json
with open("config.json", "r") as f:
    _config = json.load(f)

CHARACTERS = _config["characters"]
DEFAULT_MAP = _config["default_map"]
