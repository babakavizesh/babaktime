from telethon.sync import TelegramClient
from telethon import functions
from datetime import datetime
import time
import os

# دریافت api_id و api_hash از متغیرهای محیطی
api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")

# مقدار داخل پرانتز باید دقیقاً همون اسم فایل session بدون پسوند باشه
client = TelegramClient('session', api_id, api_hash)

with client:
    while True:
        now = datetime.now().strftime('%H:%M')
        name = f"BbK | {now}"  # ← اینجا اسمت رو می‌تونی عوض کنی
        client(functions.account.UpdateProfileRequest(first_name=name))
        print(f"نام بروزرسانی شد: {name}")
        time.sleep(60)
