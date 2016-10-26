import time
import random
import datetime
import telepot
from CommandParser import CommandParser

"""
```
- `/roll` - reply with a random integer between 1 and 6, like rolling a dice.
- `/time` - reply with the current time, like a clock.
"""

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    if command == '/roll':
        bot.sendMessage(chat_id, random.randint(1,6))
    elif command == '/time':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))
    elif command == '/info':
	bot.sendMessage(chat_id, 'I am a bot. My name is DemuthBot')
    elif command == '/uptime':
      	 bot.sendMessage(chat_id, cp.runAndReturn(cp.getCommand("load")))
    elif command == '/ip':
         bot.sendMessage(chat_id, cp.runAndReturn(cp.getCommand("publicIP")))
    elif command == '/zemuniz':
  	bot.sendMessage(chat_id, 'Um musico brasileiro porreta!')




cp = CommandParser()
bot = telepot.Bot('<<your Telegram Bot token>>')
bot.message_loop(handle)
print 'I am listening ...'

while 1:
    time.sleep(10)

