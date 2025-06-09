import discord
import requests
import json

def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']

class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  async def on_reaction_add(self, reaction, user): #tells you when you reacted on the messeage
    await reaction.message.channel.send('you reacted')

  async def on_message(self, message): #shows you meme to lighten up your mood
    if message.author == self.user:
      return
    if message.content.startswith('$meme'):
      await message.channel.send(get_meme())
    if message.content.startswith('hello'): #it greets you
      await message.channel.send(f'Hi there {message.author}')
    if message.content.startswith('how are you'): 
      await message.channel.send(f'i am great , what about you {message.author}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTM4MTY4Nzk4MzI3ODY1NzY0Nw.Gfwqam.GA1Gav562aPcZ5OD3_9zyh5sTiw67eqfL8Leyw') # Give your own token own token.
# type python3 bot.py to get the bot online and running 