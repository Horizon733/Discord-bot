import discord
from dicord.ext import commands
from dotenv import load_dotenv
from chitchat import Chitchat

load_dotenv()

bot = commands.Bot(command_prefix=["."],case_insensitive=True,help_command=None)

rasa_bot_id = "Nzc1NzI2ODEwNjExOTc0MTU0.X6qh4w.DjsKmnj-220AbkmWnq-cOVdeM-0"
channel_id = 714114451065798737

client = dicord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to discord!')
@bot.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("missing perms, get gud kid")
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online,activity=discord.Activity(name="Looking you",type=3))
    print(f'{bot.user.name} is running...')

bot.add_cog(Chitchat(bot))
bot.run(rasa_bot_id)

