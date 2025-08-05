from dotenv import load_dotenv
import os

load_dotenv()

secret = os.environ.get("SECRET_KEY")
print("SECRET_KEY:", secret)
