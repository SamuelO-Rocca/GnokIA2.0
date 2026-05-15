import os

from dotenv import load_dotenv
load_dotenv()
from google import genai

OPENAI_API_KEY = os.getenv("GEMMA_API_KEY")
OPENAI_API_BASE = os.getenv("GEMMA_API_BASE", "https://openrouter.ai/google/gemma-4-26b-a4b-it:free")

client = genai.Client(
    base_url=OPENAI_API_BASE,
    api_key=OPENAI_API_KEY
)

MODEL_NAME = os.getenv("MODEL_NAME")
DEPLOYMENT_NAME = os.getenv("DEPLOYMENT_NAME", MODEL_NAME)
EMBEDDING_MODEL_NAME = os.getenv("EMBEDDING_MODEL_NAME", "text-embedding-3-small")
EMBEDDING_DEPLOYMENT_NAME = os.getenv("EMBEDDING_DEPLOYMENT_NAME", EMBEDDING_MODEL_NAME)

LIMIT_TOKENS = int(os.getenv("LIMIT_TOKENS", "4096"))
MAX_RESPONSE_TOKENS = int(os.getenv("MAX_RESPONSE_TOKENS", "1024"))