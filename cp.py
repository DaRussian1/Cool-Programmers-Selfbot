
import discord, json, os, time, random, requests
import asyncio
from asyncio import sleep
from discord.ext import commands
from pystyle import Colors, Colorate, Center
os.system("title Cool Programmers")
with open("config.json", "r") as f:
    data = json.load(f)
icon = f"\u001b[37;1m[\u001b[30;1mC\u001b[0mP\u001b[37;1m]\u001B[0m"
client = commands.Bot(command_prefix="cp.",self_bot=True,intents=discord.Intents.all(),help_command=None)
token = data["TOKEN"]
def returnplaintext(textsex=["CP","SB"], prefixandcount=False):
    text = f'''
```
    ┏━━━━━━━━━━━━━━━━━━━━━━━━\n'''
    if prefixandcount:
        text += f"    ┃ ⬞ Prefix: {client.command_prefix}\n"
        text += f"    ┃ ⬞ Command Count: {len(client.commands)}\n"
        text += f"    ┃ ⬞ [] = Optional | <> = Required\n"
    for shit in textsex:
        text += f"    ┃ ⬞ {shit}\n"
    text += f"    ┗━━━━━━━━━━━━━━━━━━━━━━━━\n```"
    return text

for file in os.listdir("./cogs"):
  if file.endswith('.py'): 
        try:
            client.load_extension(f"cogs.{file[:-3]}")
            print(f"{icon} loaded {file}")
        except Exception as E:
            print(f"{icon} {file} error: {E}")

@client.event
async def on_command_error(ctx, error):
    try:
        await ctx.message.edit(returnplaintext("""  ______   _______          ______          __  __                  __ 
 /      \ /       \        /      \        /  |/  |                /  |
/$$$$$$  |$$$$$$$  |      /$$$$$$  |_____  $$/ $$ |  ______    ____$$ |
$$ |  $$/ $$ |__$$ |      $$ |_ $$/      \ /  |$$ | /      \  /    $$ |
$$ |      $$    $$/       $$   |  $$$$$$  |$$ |$$ |/$$$$$$  |/$$$$$$$ |
$$ |   __ $$$$$$$/        $$$$/   /    $$ |$$ |$$ |$$    $$ |$$ |  $$ |
$$ \__/  |$$ |            $$ |   /$$$$$$$ |$$ |$$ |$$$$$$$$/ $$ \__$$ |
$$    $$/ $$ |            $$ |   $$    $$ |$$ |$$ |$$       |$$    $$ |
 $$$$$$/  $$/             $$/     $$$$$$$/ $$/ $$/  $$$$$$$/  $$$$$$$/ 
                                                                       """,error))
    except:
        print(f"{icon} {error}")

@client.event
async def on_error(event, *args, **kwargs):
    pass

@client.event
async def on_ready():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Center.XCenter(Colorate.Vertical(Colors.blue_to_purple, f"""
  ______   _______          ______                                                      __                         
 /      \ /       \        /      \                                                    /  |                        
/$$$$$$  |$$$$$$$  |      /$$$$$$  |  ______   _______    ______    ______   ______   _$$ |_     ______    ______  
$$ |  $$/ $$ |__$$ |      $$ | _$$/  /      \ /       \  /      \  /      \ /      \ / $$   |   /      \  /      \ 
$$ |      $$    $$/       $$ |/    |/$$$$$$  |$$$$$$$  |/$$$$$$  |/$$$$$$  |$$$$$$  |$$$$$$/   /$$$$$$  |/$$$$$$  |
$$ |   __ $$$$$$$/        $$ |$$$$ |$$    $$ |$$ |  $$ |$$    $$ |$$ |  $$/ /    $$ |  $$ | __ $$ |  $$ |$$ |  $$/ 
$$ \__/  |$$ |            $$ \__$$ |$$$$$$$$/ $$ |  $$ |$$$$$$$$/ $$ |     /$$$$$$$ |  $$ |/  |$$ \__$$ |$$ |    __  
$$    $$/ $$ |            $$    $$/ $$       |$$ |  $$ |$$       |$$ |     $$    $$ |  $$  $$/ $$    $$/ $$ |   /  | 
 $$$$$$/  $$/              $$$$$$/   $$$$$$$/ $$/   $$/  $$$$$$$/ $$/       $$$$$$$/    $$$$/   $$$$$$/  $$/    $$/   

____________________________________________________________________________________________________________________________________________________________________________________________


Connected to  {client.user}.

____________________________________________________________________________________________________________________________________________________________________________________________
 """, 1)))


@client.command()
async def friend(ctx, id):
    await ctx.message.delete()
    user = await client.get_user_info(id)
    try:
      await sleep(.305)
      await user.send_friend_request()
    except (discord.Forbidden, discord.HTTPException):
      print(f"ooga booga this shit stupid and it couldnt friend {id}")


@client.command(description=f"Automated help command without using dpy's default command")
async def help(ctx, shit=None):
    if shit == None:
        cogs = []
        for cog in client.cogs:
            cogs.append(f"help {cog}")
        await ctx.message.edit(content=returnplaintext(cogs,True),delete_after=15)
    else:
        try:
            cmds = []
            for cmd in client.get_cog(shit).get_commands():
                if cmd.usage:
                    cmds.append(f"{cmd.name} {cmd.usage} - {cmd.description or 'No Description'}")
                else:
                    cmds.append(f"{cmd.name} - {cmd.description or 'No Description'}")
            await ctx.message.edit(content=returnplaintext(cmds,True),delete_after=15)
        except:
            for cmd in client.commands:
                if cmd.name == shit:
                    await ctx.message.edit(content=returnplaintext([f"Name: {cmd.name}",f"Description: {cmd.description or 'No Description'}",f"Usage: {cmd.name} {cmd.usage or '(NO USAGE)'}"],True),delete_after=15)

@client.command(description="spam messages", alias="spammer", usage="(amount) (message)")
async def spam(ctx, amount, *, message):
    await ctx.message.delete()
    x = 0
    for childpoem in range(int(amount)):
      await ctx.send(f"{message}")
      x+=1
    print(Colorate.Horizontal(Colors.blue_to_purple, f"Sent {message} {x} times.", 1))

@client.command(description="get letency of bot ok", usage="Ok")
async def ping(ctx):
  try:
    await ctx.message.delete()
  except:
    pass
  before = time.monotonic()
  message = await ctx.send("Pinging...")
  ping = (time.monotonic() - before)*1000
  await message.edit(content=f"{int(ping)} ms")
  
@client.command(description="purge dms so no more kal momnr real", usage="(amount)")
async def purge(ctx, amount: int):
    async for message in ctx.message.channel.history(limit=amount+1).filter(
            lambda m: m.author == client.user).map(lambda m: m):
        try:
            await message.delete()
        except:
            pass

@client.command(description="load templates", usage="(TemplateName)")
async def load(ctx, template=None):
  if template == "cp":
    for deez in ctx.guild.channels:
      try:
        await deez.delete()
      except:
        pass
#    for cp in ctx.guild.roles:
#      try:
#        await cp.delete()
#      except:
#        pass
      try:
        await ctx.guild.edit(name="ད¢₱ཌ  COOL PROGRAMMERS", icon='https://cdn.discordapp.com/attachments/971030594718949436/976459973150261248/seepee.png?size=4096')
      except:
        pass
    try:
      cpz = await ctx.guild.create_category("z")
      await ctx.guild.create_text_channel("cp-whalecum", category=cpz)
      cpi = await ctx.guild.create_category("read pls!!!")
      await ctx.guild.create_text_channel(f"cp-rules", category=cpi)
      await ctx.guild.create_text_channel(f"cp-announcements", category=cpi)
      cps = await ctx.guild.create_category("sesso ah ah sesso")
      await ctx.guild.create_text_channel(f"cp general", category=cps)
      await ctx.guild.create_text_channel(f"cp tool talk", category=cps)
      cpv = await ctx.guild.create_category("help my mic broke")
      await ctx.guild.create_voice_channel(f"cp vc real", category=cpv)
      await ctx.guild.create_text_channel(f"help my mic broke", category=cpv)
      cpa = await ctx.guild.create_category("admin stuff")
      await ctx.guild.create_text_channel(f"cp admins talk here", category=cpa)
      cp0 = await ctx.guild.create_role(name = "unverified jew", color='white')
      cp1 = await ctx.guild.create_role(name = "average slave", color='white')
      cp2 = await ctx.guild.create_role(name = "above average slave", color='black')
      cp3 = await ctx.guild.create_role(name = "slave owners", color='red')
      await cpz.set_permissions(cp0, send_messages=False, read_messages=True)
      await cpz.set_permissions(send_messages=False)
      await cps.set_permissions(cp1, send_messages=True, mention_everyone=False,read_messages=True, attach_files=False, embed_links=False)
      await cps.set_permissions(cp2, send_messages=True, mention_everyone=False,read_messages=True, attach_files=False, embed_links=False)
      await cps.set_permissions(cp3, send_messages=True, mention_everyone=False,read_messages=True, attach_files=False, embed_links=False)
      await cpa.set_permissions(cp1, send_messages=False)
      await cpa.set_permissions(cp2, read_messages=False)
      await cpa.set_permissions(cp3, read_messages=False)
      await cp3.set_permissions(administrator=True)
      await cp0.set_permissions(send_messages=False)

    except:
      pass
    print(Colorate.Horizontal(Colors.blue_to_purple, "Loaded CP",1))

#taken from GKK SB
@client.command()
async def ukk(ctx):
  await ctx.message.delete()
  quotes = [
    "You are **N-grader**, im **CC-grader**\n - Arminius",
    "yall being attention sluts today im kinda happy idk y\n - Kal",
    "im mad at yuri for being a lazy fuck so im gonna take out my anger on you\n - Kal",
    "your on my list yknow\n - Kal",
    "how old are you?\n*13*\nYou are too old ima leave you to yuri then\n\n - Arminius",
    "i thought you were cipher but you are a cunt with lower iq\n - Kal",
    "you need to unmonkey your brain yourself\n - Apollyon",
    "Steiggar is main cp supplier\njk its kanzar\n\n - Arminius",
    "i licked my foreskin\n - Sonical",
    "Tell him I said we are uploading his info on doxbin\n - Kingston",
    "I will tell kanzar to slap your dick\n - Arminius Von Ritter :japanese_goblin:",
    "Surely stop being autistic and if you do tox us you are banned from UKK 🍺\n - Kanzar",
    "Feferant trying to be funny\n - Kanzar",
    "I've literraly got someone address and credit card information and phone number\n - Kanzar",
    "Kanzar: Show me your dick cunt or I will ban you full homo\nSir Saint: im a higher rank\nKanzar: ?ban @Sir Saint Your banned!!!!!\nSir Saint: im telling yurian on you",
    "3 blocked messages who is it\n - Larry",
    "You are m graders D grader is no longer a thing its 'mussie grade' I have your doxx you remeber? we leak them soon ¯\_(ツ)_/¯",
    "@everyone I wanna admit something I have very strong crush onto @Sociopath\nbut she dosnt want me, its alright\ni understand her\nshe had trouble childhood,\nwell at least i can help her with that.\n\n - Rei",
    "bro you skid everything you see\nthat was my old shit and i was scraping LMFAO YOU THINK I SKIDDED YOUR SKIDDED BOT\n - Larry",
    "get the fuck off my dms script kiddie\n - Larry",
    "I wont verify you apes\n - Arminius",
    "Then we will invade HA in November\n - Arminius",
    "billal is dark, abo is reporting himself\n - Arminius",
    "I wanked to Arminius and im proud of it\n - Kanzar",
    "Arminius: Hi Doja\nArminius: I still wank to your nudes\nArminius: i want to them everyday\nFeferant: Isnt she like 11\nArminius: 12*",
    "Wack facks christmassssss soon, gonna buy D graders new diapers\n - Arminius",
    "Rivalite show me ur nudes\n - Theseus",
    "you believe kal now?\n - Larry",
    "i know a lot of people who can dox feferant\n - Kenny",
    "you are all dead unless I have ownership\n - Kingston",
    "pee pax has 10 alts into this server.....my timbers are shivered rn......\n - KristanP",
    "ew pooskin\n - Larry",
    "I kept this since i was fucking nuked by feferant\nScrew you\nScrew riaz\nScrew dylan\nScrew all of you\n\n - Zenith",
    "IM A FUCKING ELITE (Instagram) RAIDER\n - Kanzar",
    "yo takaso do be chad lets recruit him into ukk and get his chad tools\n - Kal",
    "tocksy o tocksy fix yourself or ill fix you \n - Kal"
    "not with u got stolen genocide s@lfbot\n i litery found it on github\n now i own it\n sorry bozo\n - Rei"
    "if you really wish to engage in a systematic from of negotiotion in which we both show our mutual resentment of one another, whilst trying to assert domminance by carrying out a test of verbal communication then we will get nowhere will we Roover.\n - Kingston"
  ]
  await ctx.send(random.choice(quotes))

  
@client.command(description="Clones channel that it is typed in")
async def clone(ctx):
  await ctx.message.delete()
  sessoahahsesso = await ctx.channel.clone(reason="cp")
  await ctx.channel.delete()
  await sessoahahsesso
  print(Colorate.Horizontal(Colors.blue_to_purple, "Channel cloned." , 1))

@client.command()
async def gay(ctx, member:discord.User=None):
  if member == None:
     member = ctx
  gay = random.randrange(101)
  if gay < 25:
      await ctx.message.edit(content=returnplaintext([f"{member.name} is {gay}% gay", f"good"]))
  elif gay < 50:
    await ctx.message.edit(content=returnplaintext([f"{member.name} is {gay}% gay", f"stop"]))
  elif gay < 75:
     await ctx.message.edit(content=returnplaintext.plaintext([f"{member.name} is {gay}% gay", f"i will find ur location"]))
  elif gay < 100:
     await ctx.message.edit(content=returnplaintext([f"{member.name} is {gay}% gay", f"retard"]))

@client.command()
async def simp(ctx, member:discord.User=None):
  if member == None:
     member = ctx
  simp = random.randrange(101)
  if gay < 25:
    await ctx.message.edit(content=returnplaintext([f"{member.name} is {simp}% simp", f"good"]))
  elif gay < 50:
    await ctx.message.edit(content=returnplaintext([f"{member.name} is {simp}% simp", f"stop"]))
  elif gay < 75:
    await ctx.message.edit(content=returnplaintext([f"{member.name} is {simp}% simp", f"i will find ur location and eat your dick"]))
  elif gay < 100:
    await ctx.message.edit(content=returnplaintext([f"{member.name} is {simp}% simp[", f"stop simp YOU NIGGA!! "]))

@client.command()
async def tokeninfo(ctx, token):
    try:
        await ctx.message.delete()
    except:
        pass
    r = requests.get(f"https://discord.com/api/v9/users/@me", headers = {'Authorization':token})
    if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
        try:
            await ctx.send(f"""```css
[Token Info]

Token - {token}
ID - {r.json()['id']}
User - {r.json()['username']}#{r.json()['discriminator']}
Phone - {r.json()['phone']}
Email - {r.json()['email']}
Mfa - {r.json()['mfa_enabled']}
            ```""")
        except:
            pass
    else:
        r = requests.get(f"https://discord.com/api/v9/users/@me", headers = {'Authorization':f"Bot {token}"})
        if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
            try:
                await ctx.send(f"""```css
[Bot]

Token - Ok
ID - {r.json()['id']}
User - {r.json()['username']}#{r.json()['discriminator']}
                ```""")
            except:
                pass
        else:
            try:
                await ctx.send(f"""```diff
- Invalid token
                ```""")
            except:
                pass


@client.command(aliases=["copyguild", "copyserver"])
async def c(ctx):
    #await ctx.message.delete()
    await client.create_guild(f'backup-{ctx.guild.name}')
    await asyncio.sleep(2)
    for g in client.guilds:
        if f'backup-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}", overwrites=cate.overwrites)
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}", overwrites=chann.overwrites)
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}", overwrites=chann.overwrites, topic=chann.topic)
            for role in ctx.guild.roles:
              if role.name == '@everyone':
                pass
              else:
                await g.create_role(name=role.name, color=role.color, permissions=role.permissions)
    try:
        await g.edit(icon=ctx.guild.icon_url)
    except:
        pass


client.run(data["TOKEN"], bot=False)
