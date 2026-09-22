import os
from dotenv import load_dotenv


load_dotenv()
SECRET_KEY = os.environ["SECRET_KEY"]
DATABASE_URL = os.environ["DATABASE_URL"]
ALGORITHM = "HS256"
