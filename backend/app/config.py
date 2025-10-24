# config.py
import os
from dotenv import load_dotenv

# Charger le fichier .env
load_dotenv()

# --- APPLICATION ---
PROJECT_NAME = os.getenv("PROJECT_NAME", "Chatbot_Medical_IA")
APP_ENV = os.getenv("APP_ENV", "dev")
SECRET_KEY = os.getenv("SECRET_KEY", "defaultsecret")

# --- DATABASE ---
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/dbname")

# --- LLM ---
LLM_MODEL_NAME = os.getenv("LLM_MODEL_NAME", "gpt4all")
LLM_MODEL_PATH = os.getenv("LLM_MODEL_PATH", "chatbot/model/gpt4all-lora-quantized.bin")

# --- VECTOR DATABASE ---
VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH", "data/faiss_index")

# --- DOCUMENTS ---
DOCS_PATH = os.getenv("DOCS_PATH", "data/docs")
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 500))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 50))

# --- SERVER CONFIG ---
HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", 8000))
