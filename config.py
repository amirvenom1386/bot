import os

# مقدار API_ID و API_HASH رو از Environment Variable می‌خونیم
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session_name = "news_forwarder"

# کانال‌ها (فقط یوزرنیم، بدون https://t.me/)
SOURCE_ALL = "source_all_channel"
SOURCE_MEDIA = "source_media_channel"

# مقصد
TARGET = "your_target_channel_or_bot"
