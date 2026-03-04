"""
OpenCrypto — Configuration

Loads settings from environment variables. All API keys are optional.
Copy .env.example to .env and fill in your values.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

_env_path = Path(__file__).parent.parent.parent / ".env"
if _env_path.exists():
    load_dotenv(_env_path)

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "")
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

USE_LLM = bool(GROQ_API_KEY) and os.getenv("USE_LLM", "true").lower() != "false"
USE_TELEGRAM = bool(TELEGRAM_BOT_TOKEN)

BINANCE_FUTURES_URL = "https://fapi.binance.com"
BINANCE_SPOT_URL = "https://api.binance.com"

DATA_DIR = Path(__file__).parent.parent.parent / "data"
DATA_DIR.mkdir(exist_ok=True)
