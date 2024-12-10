import os
from dotenv import load_dotenv

def get_token():
    load_dotenv("token.env")
    return os.environ.get('TOKEN')
