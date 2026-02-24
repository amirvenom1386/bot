import os

# مقدار API_ID و API_HASH رو از Environment Variable می‌خونیم
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session_name = "news_forwarder"

# کانال‌ها (فقط یوزرنیم، بدون https://t.me/)
SOURCE_ALL = "https://t.me/Cyber_News_ir"
SOURCE_MEDIA = "https://t.me/MW_HACK"
SOURCE_TEST = "https://t.me/+cVcxTIMzGmM1MzFk"


# مقصد
TARGET = "https://t.me/+E_c0md8177Q2MTE0"
