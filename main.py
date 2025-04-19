from telethon import TelegramClient, functions
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

async def update_name():
    while True:
        try:
            # دریافت زمان جاری به وقت ایران
            now = datetime.now(iran_timezone).strftime('%H:%M')
            name = f"BbK | {now}"  # ← اینجا می‌تونی اسم دلخواهت رو بذاری

            # بروزرسانی پروفایل
            await client(functions.account.UpdateProfileRequest(first_name=name))
            print(f"نام بروزرسانی شد: {name}")
            time.sleep(60)  # هر دقیقه یک بار
        except Exception as e:
            print(f"خطا در بروزرسانی پروفایل: {e}")
            time.sleep(60)  # اگه خطا پیش بیاد، 60 ثانیه صبر می‌کنه و دوباره تلاش می‌کنه

async def main():
    await client.start()
    await update_name()

if __name__ == "__main__":
    client.loop.run_until_complete(main())
