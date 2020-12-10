import discord
from discord.ext import commands
import requests



class Chitchat(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command(name="hi")
    async def greet(self, ctx):
        url = "ngrok_ip/webhooks/rest/webhook"
        mes = {"message":"/greet","sender":"me"}
        x = requests.post(url,json=mes)
        msg = x.json()[0]['text']
        await ctx.send(msg)
    
    @commands.commands(name="rank")
    async def rank(self,ctx):
        url = "ngrok_ip/webhooks/rest/webhook"
        mes = {"message":"/rank","sender":"me"}
        x = requests.post(url,json=mes)
        msg = x.json()[0]['text']
        await ctx.send(msg)
    @commands.commands(name="help")
    async def rank(self,ctx):
        embed= discord.Embed(title="rasa_bot",description=f"Running on PC",color=16761095)
        embed.add_field(name='"hi"', value="'Want to greet just type Hi'")
        embed.add_field(name='"rank"', value="'want to know your rank type it'")
        await ctx.send(embed=embed)
