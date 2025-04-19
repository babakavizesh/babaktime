from telethon.sync import TelegramClient
from telethon import functions
from datetime import datetime
import time
import os
import pytz

# اطلاعات api_id و api_hash از متغیرهای محیطی
api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")

# منطقه زمانی ایران (تهران)
iran_timezone = pytz.timezone("Asia/Tehran")

# اتصال به تلگرام
client = TelegramClient('session', api_id, api_hash)

with client:
    while True:
        # دریافت زمان جاری به وقت ایران
        now = datetime.now(iran_timezone).strftime('%H:%M')
        name = f"BbK | {now}"  # ← اینجا می‌تونی اسم دلخواهت رو بذاری
        client(functions.account.UpdateProfileRequest(first_name=name))
        print(f"نام بروزرسانی شد: {name}")
        time.sleep(60)  # هر دقیقه یک بار
