import os
from pathlib import Path
from dotenv import load_dotenv

# Project root
ROOT_DIR = Path(__file__).resolve().parents[1]

# Load .env
load_dotenv(ROOT_DIR / ".env")

ENV = os.getenv("ENV", "development")

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    f"sqlite:///{ROOT_DIR / 'data' / 'dev.db'}",
)
