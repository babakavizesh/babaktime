from telethon.sync import TelegramClient
from telethon import functions
from datetime import datetime
import time
import os
import pytz

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")

client = TelegramClient('session', api_id, api_hash)

# منطقه زمانی ایران
iran_timezone = pytz.timezone("Asia/Tehran")

with client:
    while True:
        now = datetime.now(iran_timezone).strftime('%H:%M')
        name = f"BbK | {now}"  # ← اسم دلخواهت
        client(functions.account.UpdateProfileRequest(first_name=name))
        print(f"نام بروزرسانی شد: {name}")
        time.sleep(60)
