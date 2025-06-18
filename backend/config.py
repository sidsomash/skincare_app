import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file

SECRET_KEY = os.getenv("SECRET_KEY", "default-secret-key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
