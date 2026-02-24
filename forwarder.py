# forwarder.py
from telethon import events
from config import SOURCE_ALL, SOURCE_MEDIA, TARGET

def register_handlers(client):
    # کانال اول: همه پیام‌ها
    @client.on(events.NewMessage(chats=SOURCE_ALL))
    async def forward_all(event):
        try:
            await client.forward_messages(TARGET, event.message)
            print("Forwarded from SOURCE_ALL ✅")
        except Exception as e:
            print("Error SOURCE_ALL:", e)

    # کانال دوم: فقط مدیا (عکس، ویدئو، فایل)
    @client.on(events.NewMessage(chats=SOURCE_MEDIA))
    async def forward_media(event):
        try:
            msg = event.message
            if msg.photo or msg.video or msg.document:
                await client.forward_messages(TARGET, msg)
                print("Forwarded media from SOURCE_MEDIA 📸🎥📄")
            else:
                print("Ignored non-media message ⏭")
        except Exception as e:
            print("Error SOURCE_MEDIA:", e)
    @client.on(events.NewMessage(chats=SOURCE_TEST))
    async def test(event):
        try:
            awit client.forward_messages(TARGET, event.message)
            print("Forwarded from SOURCE_TEST ✅")
        except Exception as e:
            print("Error :",e)
