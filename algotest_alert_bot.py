import requests
import os
from dotenv import load_dotenv
import asyncio
from telethon import TelegramClient, events

load_dotenv()

# Your Telegram API credentials
api_id = os.getenv("APP_ID")
api_hash = os.getenv("API_HASH")
print(api_id)

# Initialize the Telegram client
client = TelegramClient('anon', api_id, api_hash)

async def call_link():
    # Make a GET request to the specified link
    response = requests.get(os.getenv("CALL_LINK"))
    # Check if the request was successful
    if response.status_code == 200:
        print('GET request successful!')
    else:
        print('GET request failed!')

@client.on(events.NewMessage(chats='AlgoTest_in_bot'))
async def handler(event):
    # Call the link before replying to the user
    await call_link()
    # Respond whenever someone says "Hello" and something else
    await event.reply('Strategy Went into error')

@client.on(events.NewMessage(chats='shubhamtheds'))
async def handler(event):
    # Call the link before replying to the user
    await call_link()
    # Respond whenever someone says "Hello" and something else
    await event.reply('Strategy Went into error')

async def main():
    # Start the client
    await client.start()
    # Run the client until it's disconnected
    await client.run_until_disconnected()

# Run the main function
with client:
    client.loop.run_until_complete(main())
