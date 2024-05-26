from discord.ext import commands, tasks
from datetime import datetime

class MyFirstCog(commands.Cog):
   def __init__(self,bot):
      self.bot = bot
      self.context = None

   @commands.Cog.listener()
   async def on_message(self,message):
      if message.content =="hello":
         await message.channel.send("go awat")

  #  @tasks.loop(seconds=5)
  #  async def hello(self,context):
  #     await context.send("Test stuff")

   @tasks.loop(seconds=5)
   async def hello(self,context):
      if self.context:
        await context.send("Test task")

   @tasks.loop(seconds=1)
   async def alarm(self,context,hour,minute):
      now = datetime.now().time()
      if now.hour == hour and now.minute==minute:
         await context.author.create_dm()
         await context.author.dm_channel.send("Tick Tock Your Time has come!")
         self.alarm.stop()

   @commands.command()
   async def start(self,context):
      self.context = context
      self.hello.start(context)
      
   @commands.command()
   async def stop(self,context):
      self.hello.stop()
      self.context= None

   @commands.command()
   async def startalarm(self,context,date):
      hour,min= date.split(":")
      hour = int(hour)
      min=int(min)
      self.context = context
      self.alarm.start(context,hour,min)
      


async def setup(bot):
    await bot.add_cog(MyFirstCog(bot))
