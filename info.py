import discord, base64
from pystyle import Colors, Colorate
from discord.ext import commands
proxies = []
good_codes = [200, 201, 204]
proxy = open("proxies.txt").readlines()
for xd in proxy:
  finalproxy = xd.replace('\n', '')
  proxies.append(finalproxy)

def returnplaintext(textsex=["CP","SB"]):
    text = f'''
```┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n'''
    for shit in textsex:
        text += f"┃  {shit} \n"
    text += f"┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n```"
    return text

icon = f"\u001b[0m[\u001b[30;1mC\u001b[0mP]"


class info(commands.Cog):

    @commands.command(description="Gets member's info", usage="<member id or mention>")
    async def whois(self, ctx, member:discord.User=None):
        if member == None:
            return await ctx.message.edit(content=returnplaintext(["""
┃    ______   _______          ______          __  __                  __ 
┃   /      \ /       \        /      \        /  |/  |                /  |
┃  /$$$$$$  |$$$$$$$  |      /$$$$$$  |_____  $$/ $$ |  ______    ____$$ |
┃  $$ |  $$/ $$ |__$$ |      $$ |_ $$/      \ /  |$$ | /      \  /    $$ |
┃  $$ |      $$    $$/       $$   |  $$$$$$  |$$ |$$ |/$$$$$$  |/$$$$$$$ |
┃  $$ |   __ $$$$$$$/        $$$$/   /    $$ |$$ |$$ |$$    $$ |$$ |  $$ |
┃  $$ \__/  |$$ |            $$ |   /$$$$$$$ |$$ |$$ |$$$$$$$$/ $$ \__$$ |  ___
┃  $$    $$/ $$ |            $$ |   $$    $$ |$$ |$$ |$$       |$$    $$ | /   |
┃   $$$$$$/  $$/             $$/     $$$$$$$/ $$/ $$/  $$$$$$$/  $$$$$$$/   $$/
┃"""]))
        firsttok = str(base64.b64encode(str(member.id).encode("utf-8")), "utf-8")
        await ctx.message.edit(content=returnplaintext([f"Name: {member}",f"ID: {member.id}",f"Created: {member.created_at}",f"PFP: {member.avatar_url}",f"First Part of Token: {firsttok}"]))
    
    
def setup(bot):
    bot.add_cog(info())