import os

import src.classes.client

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

client = src.classes.client.MyClient()

client.run(TOKEN)