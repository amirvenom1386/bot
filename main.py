# main.py
import asyncio
from telethon import TelegramClient
from config import api_id, api_hash, session_name
from forwarder import register_handlers

client = TelegramClient(session_name, api_id, api_hash)

async def main():
    register_handlers(client)
    await client.start()
    print("Userbot is running permanently 🤖📡")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
