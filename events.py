import discord
import requests

BOTNAME = "WORLDHOPPER"
intents = discord.Intents.all()
intents.message_content = True


bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
  print("WORLDHOPPER IS ONLINE!")

@bot.event
async def on_message(msg):
    if msg.author == bot.user:
       return
    username = msg.author.display_name
    if "hello" in msg.content.lower():
        await msg.channel.send("WORLDHOPPER SAYS HI "+username)

@bot.event
async def on_member_join(member):
  print(f"New member joined: {member.name}")
  guild = member.guild
  guildName = guild.name
  print(f"Guild: {guildName}")
  dmchannel = await member.create_dm()
  print(f"DM channel created for {member.name}")
  await dmchannel.send(f"Hello {member.name}! {BOTNAME} welcomes you to {guildName}!")
  print(f"Message sent to {member.name}")


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

@bot.event
async def on_raw_reaction_remove(payload):

    userId = payload.user_id
    emoji = payload.emoji.name
    msg_id = payload.message_id
    guild_id = payload.guild_id
    guild = bot.get_guild(guild_id)
    member = guild.get_member(userId)
    role = None
    if emoji == "🌫️" and msg_id == 1243575022078001163:
        role = discord.utils.get(guild.roles, name="Kelsier Stan")
    elif emoji == "🔥" and msg_id == 1243575069289087028:
        role = discord.utils.get(guild.roles, name="Spook Stan")
    await member.remove_roles(role)
  

bot.run("MTI0MzUzMjY0NTI5NjUwODk5OA.GcDw7J.-IWdkEEx-fhwFz8XZyW8m7H8l4AL_a_wQ0aSPw")