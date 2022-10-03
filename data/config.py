from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('TOKEN')

admins_id = [
    440206915
]

ip = os.getenv('ip')
PGUSER = os.getenv('PGUSER')
PGPASSWORD = os.getenv('PGPASSWORD')
DATABASE = os.getenv('DATABASE')

POSTGRES_URI = f'postgresql://{PGUSER}:{PGPASSWORD}@{ip}/{DATABASE}'
