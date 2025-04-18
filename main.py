from telethon.sync import TelegramClient
from telethon import functions
from datetime import datetime
import time
import os

# اطلاعات تلگرام خودتو اینجا وارد کن
api_id = int(os.environ.get("383244"))  # به نام درست متغیر محیطی تغییر کنه
api_hash = os.environ.get("0abb6c73099af28084bfa507e6f26191")   # به نام درست متغیر محیطی تغییر کنه

# اگر هنوز مقدار None دریافت شد، خطا ایجاد می‌کنه
if not api_id or not api_hash:
    raise ValueError("API_ID or API_HASH is not set properly in environment variables.")

client = TelegramClient('session', api_id, api_hash)

with client:
    while True:
        now = datetime.now().strftime('%H:%M')
        name = f"BbK | {now}"  # ← اینجا اسمتو بذار
        client(functions.account.UpdateProfileRequest(first_name=name))
        print(f"نام بروزرسانی شد: {name}")
        time.sleep(60)
