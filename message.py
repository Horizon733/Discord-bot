import discord
from discord.ext import commands
import discordConnector
class Message(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
    async def on_message(self,message):
        if message.author.id == self.user.id:
            return
        else:
            await message.reply(discordConnector.send_message(message.content))

client = Message()
client.run('NzgzNzQ4MTczNjg0MDE1MTU1.X8fQXQ.bK4O8bO2Ij8OjtwXHOeGRQcezZE')