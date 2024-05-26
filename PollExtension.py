import random
import discord
from discord.ext import commands, tasks
import os
import asyncio

# intents = discord.Intents.default()
# intents.message_content = True  

# bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)


class PollCog(commands.Cog):
  
  def __init__(self,bot):
    # self.context=None
    self.bot = bot
    self.numbers = ["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣","🔟"]
  #TODO add custom reactions for each option
  @commands.command()
  async def poll(self,context,minutes:int, title,*options):
    pollEmbed = discord.Embed(title= title,description=f"**{minutes} minutes remaining**")
    if len(options)==0:
      message = await context.send(embed =pollEmbed)
      await message.add_reaction("👍")
      await message.add_reaction("👎")
    else:
      for num, option in enumerate(options):
        pollEmbed.add_field(name=f"{self.numbers[num]}",value=f"**{option}**", inline =False)
      message = await context.send(embed=pollEmbed)
      for option in range(len(pollEmbed.fields)):
        await message.add_reaction(self.numbers[option])
    self.poll_timer.start(context, minutes, title, options, message)


  @tasks.loop(minutes=1)
  async def poll_timer(self, context,minutes,title,options,message):
    count =self.poll_timer.current_loop
    remaining_time =minutes - count
    pollEmbed = discord.Embed(title= title,description=f"**{remaining_time} minutes remaining**")

    for num, option in enumerate(options):
        pollEmbed.add_field(name=f"{self.numbers[num]}",value=f"**{option}**", inline =False)
    await message.edit(embed= pollEmbed)

    if(remaining_time==0):
      await context.send("Times UP!")
      counts =[]

      message = discord.utils.get(self.bot.cached_messages,id=message.id)
      reactions = message.reactions
      for reaction in reactions:
       counts.append(reaction.count)
      max_count = max(counts)
      num_max_count =0
      for stats in counts:
       if stats == max_count:
        num_max_count+=1
      if num_max_count >1:
       await context.send("Its a tie! Please create a new poll")
      else:
        winner_index = counts.index(max_count)
        if len(options) ==0:
         winner = reactions[winner_index]
         if winner.emoji == "👍":
           await context.send("The people have agreed")
         if winner.emoji == "👎":
          await context.send("I guess not")
        else:
         winner = options[winner_index]
         emoji = reactions[winner_index]
        # await context.send("Times UP!")
         await context.send(f"{emoji.emoji} - **{winner}** has won")
      self.poll_timer.stop()


async def setup(bot):
    await bot.add_cog(PollCog(bot))

