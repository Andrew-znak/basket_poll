from telethon import TelegramClient, events
from dotenv import load_dotenv
import logging, re, os

load_dotenv()
api_id = os.environ['TG_API_ID']
api_hash = os.environ['TG_API_HASH']
client = TelegramClient('my_session', api_id, api_hash)
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)


@client.on(events.NewMessage())
async def handler(event):
    msg = event.message.media.poll.question
    if re.search(r'Об отмене предупрежу за два часа или штраф', msg):
        me = await client.get_me()
        time = re.search(r'\d\d\.\d\d', msg).group(0)
        weekday = re.search(r'понедельник|вторник|средy|четверг|пятницу|субботу|воскресенье', msg).group(0)
        await client.send_message('me',f"Голосование баскет на {weekday} {time} началось!")


client.start()
client.run_until_disconnected()