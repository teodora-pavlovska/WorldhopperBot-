import random
from bs4 import BeautifulSoup
import discord
from discord.ext import commands
from datetime import datetime
import requests


intents = discord.Intents.default()
intents.message_content = True  # Enable intents for message content

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)



    



 
def authenthicate_me(context):
   return context.author.id == 965222615088246854

def starts_with_a(msg):
   return msg.content.lower().startswith("a")

@bot.command()
async def ping(contex):
  await contex.send("Pong!")

@bot.command()
async def coin_flip(context):
  num = random.randint(1,2)
  if(num==1):
    await context.send("Head")
  elif (num==2):
     await context.send("Tails")

@bot.command()
async def cosmere_order(context):
  booksInOrder = f"""
  Cosmere Reading Order:
  1. Mistborn: The Final Empire
  2. Mistborn: The Well of Ascension
  3. Mistborn: The Hero of Ages
  4. Mistborn: The Alloy of Law
  5. Mistborn: Shadows of Self
  6. Mistborn: The Bands of Mourning
  7. Elantris
  8. The Emperor's Soul
  9. Warbreaker
  10. The Stormlight Archive: The Way of Kings
  11. The Stormlight Archive: Words of Radiance
  12. The Stormlight Archive: Edgedancer (Novella)
  13. The Stormlight Archive: Oathbringer
  14. The Stormlight Archive: Dawnshard (Novella)
  15. The Stormlight Archive: Rhythm of War
  16. White Sand (Graphic Novel)
  """
  await context.send(booksInOrder)
  
@bot.command()
async def generate_OC(ctx):
    names = ["Aragorn", "Eowyn", "Frodo", "Gandalf", "Legolas", "Thorin", "Tauriel", "Sauron","Hoid","Kelsier","Caden"]
    races = ["Human", "Elf", "Dwarf", "Hobbit", "Wizard", "Orc","Skaa","Kundra","Koloss"]
    classes = ["Warrior", "Ranger", "Mage", "Rogue", "Cleric", "Bard"]
    abilities = ["Strength", "Agility", "Intelligence", "Charisma", "Stealth", "Endurance","Humor"]
    backstories = [
        "A hero with a gloomy past seeking revenge.",
        "A wizard with amnesia.",
        "A skilled barista who is also an assasin.",
        "An exiled noble seeking to cause trouble.",
        "A cunning spirit with a heart of gold.",
        "A powerful mage with a thirst for knowledge."
    ]

    name = random.choice(names)
    race = random.choice(races)
    char_class = random.choice(classes)
    ability = random.choice(abilities)
    backstory = random.choice(backstories)

    character_profile = f"""
    **Character Profile**
    **Name:** {name}
    **Race:** {race}
    **Class:** {char_class}
    **Primary Ability:** {ability}
    **Backstory:** {backstory}
    """
    await ctx.send(character_profile)

# def determineRPC(player1, player2):
#   if player1 == player2:
#     return "It's a draw!"
#   elif (player1 == "✊" and player2 == "✌️") or (player1 == "✋" and player2 == "✊") or (player1 == "✌️" and player2 == "✋"):
#     return "You win!"
#   else:
#     return "I won!"



@bot.command()
async def rpsls(ctx, hand):
    # Rock crushes Scissors and Lizard
    # Paper covers Rock and disproves Spock
    # Scissors cuts Paper and decapitates Lizard
    # Lizard eats Paper and poisons Spock
    # Spock smashes Scissors and vaporizes Rock
    hands = ["🪨", "📜", "✂️", "🦎", "🖖"]
    outcomes = {
        ("🪨", "✂️"), ("🪨", "🦎"),("📜", "🪨"), ("📜", "🖖"),("✂️", "📜"),
        ("✂️", "🦎"),("🦎", "📜"), ("🦎", "🖖"),("🖖", "✂️"), ("🖖", "🪨") }
    
    if hand not in hands:
        await ctx.send("Invalid hand!")
        return

    bot_hand = random.choice(hands)
    await ctx.send(f"{bot_hand}")

    if hand == bot_hand:
        result = "It's a draw!"
    elif (hand, bot_hand) in outcomes:
        result = "You win!"
    else:
        result = "I won!"

    await ctx.send(result)

#multiple aliases
@bot.command(aliases=["about","more","info"])
async def help(context):

  MyEmbed = discord.Embed(title="Commands",description="These are the commands that you cna use for this bot!",color=discord.Color.dark_purple())

  MyEmbed.set_thumbnail(url="https://static.wikia.nocookie.net/mistborn/images/8/80/Tin.png/revision/latest/scale-to-width-down/503?cb=20140214083846")
  MyEmbed.add_field(name = "!ping", value="This is a simple ping command that helps you establish a connection with the bot!")
  MyEmbed.add_field(name = "!coin_flip", value="This command helps you by flipping a coin for you. Making decisions has never been easier")
  MyEmbed.add_field(name = "!rpsls", value="Rock Paper Scissors Lizard Spock BBT:S2:E18")
  MyEmbed.add_field(name = "!cosmere_order", value="Gives you the PROPER reading order for the cosmere novels")
  MyEmbed.add_field(name = "!generate_OC", value="A command that generates a random fantasy OC + their backstory!")
  await context.send(embed =MyEmbed)


@bot.group()
async def edit(context):
   pass
@edit.command()

async def servername(context,*,input):
   await context.guild.edit(name=input)

@edit.command()
async def region(context,*,input):
   await context.guild.edit(region=input)

@edit.command()
async def create_text_channel(context,*,input):
   await context.guild.create_text_channel(name=input)   

@edit.command()
async def create_voice_channel(context,*,input):
   await context.guild.create_voice_channel(name=input)   

@edit.command()
async def create_role(context,*,input):
   await context.guild.create_role(name=input) 

@bot.command()
async def kick(context, member:discord.Member,*,reason=None):

   await context.guild.kick(member, reason= reason)


@bot.command()
async def ban(context, member:discord.Member,*,reason=None):

   await context.guild.ban(member, reason= reason)




@bot.command()
@commands.check(authenthicate_me)
async def purge(context,amount,day:int=None,month:int=None,year:int=datetime.now().year):
   if amount =="/":

      if day == None or month == None:
         return
      else:
         await context.channel.purge(after = datetime(year,month,day), check= starts_with_a)
   else:
      await context.channel.purge(limit = int(amount)+1,check= starts_with_a)


# @purge.error
# async def errorHandler(context, error):
#    if isinstance(error,commands.MissingRequiredArgument):
#       await context.send("You have to specify a date or an amount")
#    if isinstance(error,commands.CommandInvokeError):
#       await context.send("Opps! You can only giva date in the typical date format or ..........")

# @kick.error
# async def errorHandler(context, error):
   
    

#basic commands for voice channels

@bot.command()
@commands.check(authenthicate_me)
async def mute(context, user:discord.Member):
   await user.edit(mute=True)

@bot.command()
@commands.check(authenthicate_me)
async def unmute(context, user:discord.Member):
   await user.edit(mute=False)  

@bot.command()
@commands.check(authenthicate_me)
async def deafen(context, user:discord.Member):
   await user.edit(deafen=True)

@bot.command()
@commands.check(authenthicate_me)
async def undeafen(context, user:discord.Member):
   await user.edit(deafen=False)  


@bot.command()
@commands.check(authenthicate_me)
async def voicekick(context, user:discord.Member):
   await user.edit(voice_channel=None)  

@bot.command(aliases=["hi","howdy"])
async def hello(msg):
    if msg.author == bot.user:
       return
    username = msg.author.display_name
    if "hello" in msg.content.lower():
        await msg.channel.send("WORLDHOPPER SAYS HI "+username)




@bot.command()
async def embed_text(ctx):
    url = "https://www.brandonsanderson.com/mistborn-the-eleventh-metal/"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        content_div = soup.find('div', class_='entry-content') 
        if content_div:
            paragraphs = content_div.find_all('p')
            text_content = "\n\n".join([p.get_text() for p in paragraphs])

            embed = discord.Embed(title="Mistborn: The Eleventh Metal", url=url, description=text_content[:2048])

            await ctx.send(embed=embed)
        else:
            await ctx.send("Contents not found!")
    else:
        await ctx.send(f"ERROR: {response.status_code}")


@bot.event
async def on_raw_reaction_add(payload):
    emoji = payload.emoji.name
    msg_id = payload.message_id
    guild_id = payload.guild_id
    guild = bot.get_guild(guild_id)
    
    role = None
    if emoji == "🌫️" and msg_id == 1243575022078001163:
        role = discord.utils.get(guild.roles, name="Kelsier Stan")
    elif emoji == "🔥" and msg_id == 1243575069289087028:
        role = discord.utils.get(guild.roles, name="Spook Stan")

    if role is None:
        print(f"Role not found for emoji {emoji} and message ID {msg_id}")
        return

    try:
        member = await guild.fetch_member(payload.user_id)
        await member.add_roles(role)
        print(f"Added role {role.name} to {member.name}")
    except Exception as e:
        print(f"Error adding role: {e}")


@bot.command()
@commands.has_role("Kelsier Stan")
async def kelsier_shoutout(context):
   await context.send("Shoutout to Kelsier!")

#TODO chekc bans again
#unbanning users ( updated version)
# Check this later 
# @bot.command()
# async def unban(ctx, id: int):
#     user = await bot.fetch_user(id)
#     await ctx.guild.unban(user)

# @bot.command()
# async def _unban(context,*,input):
#    name,discriminator = input.split("#")
#    banned_members = await context.guild.bans()
#    for member in banned_members:
#       if name == banned_members.user.name and discriminator == banned_members.user.discriminator:
#          await context.guild.unban(banned_members.user)
         
         

@bot.command()
async def quote(ctx):
    response = requests.get("http://api.forismatic.com/api/1.0/")
    data = response.json()
    quote_text = data["quoteText"]
    quote_author = data["quoteAuthor"] or "Unknown"

    embed = discord.Embed(
        title="Random Quote",
        description=f"\"{quote_text}\"",
        color=discord.Color.purple()
    )
    embed.set_footer(text=f"― {quote_author}")

    await ctx.send(embed=embed)

@bot.event
async def on_ready():
    await bot.load_extension("cogs")
    await bot.load_extension("PollExtension")
    print(f'Logged in as {bot.user}')

@bot.command()
async def unload(context):
   bot.unload_extension("cogs")

@bot.command()
async def reload(context):
   await bot.reload_extension("cogs")
# # does not work since the coroutine update
# bot.add_cog(MyFirstCog(bot))

bot.run("MTI0MzUzMjY0NTI5NjUwODk5OA.GcDw7J.-IWdkEEx-fhwFz8XZyW8m7H8l4AL_a_wQ0aSPw")

