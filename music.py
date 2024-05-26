# #TODO fix ffmpeg path issue

# import discord
# import yt_dlp as youtube_dl
# from discord.ext import commands
# import os
# import asyncio


# # ffmpeg_path = r"C:\Users\astra\Desktop\discord Bot attempt1\ffmpeg\ffmpeg-2024-05-23-git-ece95dc3dc-full_build\bin"

# intents = discord.Intents.default()
# intents.message_content = True  

# bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)
# queuelist = []
# filestodelete = []

# @bot.command()
# @commands.has_role("DJ")
# async def join(ctx):
#     channel = ctx.author.voice.channel
#     if ctx.voice_client is not None:
#         await ctx.voice_client.move_to(channel)
#     else:
#         await channel.connect()

# @bot.command()
# @commands.has_role("DJ")
# async def leave(ctx):
#     await ctx.voice_client.disconnect()

# @bot.command()
# @commands.has_role("DJ")
# async def play(ctx, *, searchword):
#     ydl_opts = {}
#     voice = ctx.voice_client

#     if searchword.startswith("http") or searchword.startswith("www"):
#         with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#             info = ydl.extract_info(searchword, download=False)
#             title = info["title"]
#             url = searchword
#     else:
#         with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#             info = ydl.extract_info(f"ytsearch:{searchword}", download=False)["entries"][0]
#             title = info["title"]
#             url = info["webpage_url"]

#     ydl_opts = {
#         'format': 'bestaudio/best',
#         'outtmpl': f'{title}.mp3',
#         'postprocessors': [{
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'mp3',
#             'preferredquality': '192',
#         }],
#     }

#     def download(url):
#         with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#             ydl.download([url])

#     loop = asyncio.get_event_loop()
#     await loop.run_in_executor(None, download, url)

#     if voice.is_playing():
#         queuelist.append(title)
#         await ctx.send(f"Added to Queue: ** {title} **")
#     else:
#         voice.play(discord.FFmpegPCMAudio(f"{title}.mp3"), after=lambda e: check_queue(ctx))
#         await ctx.send(f"Playing ** {title} ** :musical_note:")
#         filestodelete.append(title)
#         await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=title))

# def check_queue(ctx):
#     voice = ctx.voice_client
#     try:
#         if queuelist[0] is not None:
#             next_title = queuelist.pop(0)
#             voice.play(discord.FFmpegPCMAudio(f"{next_title}.mp3"), after=lambda e: check_queue(ctx))
#             coro = bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=next_title))
#             fut = asyncio.run_coroutine_threadsafe(coro, bot.loop)
#             fut.result()
#             filestodelete.append(next_title)
#     except IndexError:
#         for file in filestodelete:
#             os.remove(f"{file}.mp3")
#         filestodelete.clear()

# @bot.command()
# @commands.has_role("DJ")
# async def pause(ctx):
#     voice = ctx.voice_client
#     if voice.is_playing():
#         voice.pause()
#     else:
#         await ctx.send("Bot is not playing Audio!")

# @bot.command(aliases=["skip"])
# @commands.has_role("DJ")
# async def stop(ctx):
#     voice = ctx.voice_client
#     if voice.is_playing():
#         voice.stop()
#     else:
#         await ctx.send("Bot is not playing Audio!")

# @bot.command()
# @commands.has_role("DJ")
# async def resume(ctx):
#     voice = ctx.voice_client
#     if not voice.is_playing():
#         voice.resume()

# @bot.command()
# async def viewqueue(ctx):
#     await ctx.send(f"Queue:  ** {str(queuelist)} ** ")

# @join.error
# async def join_error(ctx, error):
#     if isinstance(error, commands.errors.CommandInvokeError):
#         await ctx.send("You have to be connected to a Voice Channel first.")
#     if isinstance(error, commands.errors.MissingRole):
#         await ctx.send("You have to have the DJ Role to use this bot.")

# @leave.error
# async def leave_error(ctx, error):
#     if isinstance(error, commands.errors.CommandInvokeError):
#         await ctx.send("Bot is not connected to a Voice Channel.")
#     if isinstance(error, commands.errors.MissingRole):
#         await ctx.send("You have to have the DJ Role to use this bot.")

# @play.error
# async def play_error(ctx, error):
#     if isinstance(error, commands.errors.CommandInvokeError):
#         await ctx.send("Bot is not connected to a Voice Channel.")
#     if isinstance(error, commands.errors.MissingRole):
#         await ctx.send("You have to have the DJ Role to use this bot.")

# @stop.error
# async def stop_error(ctx, error):
#     if isinstance(error, commands.errors.CommandInvokeError):
#         await ctx.send("Bot is not connected to a Voice Channel.")
#     if isinstance(error, commands.errors.MissingRole):
#         await ctx.send("You have to have the DJ Role to use this bot.")

# @resume.error
# async def resume_error(ctx, error):
#     if isinstance(error, commands.errors.CommandInvokeError):
#         await ctx.send("Bot is not connected to a Voice Channel.")
#     if isinstance(error, commands.errors.MissingRole):
#         await ctx.send("You have to have the DJ Role to use this bot.")

# @pause.error
# async def pause_error(ctx, error):
#     if isinstance(error, commands.errors.CommandInvokeError):
#         await ctx.send("Worldhopper is not connected to any of the Voice Channels.")
#     if isinstance(error, commands.errors.MissingRole):
#         await ctx.send("You have to have the DJ Role to use this bot.")




# bot.run("MTI0MzUzMjY0NTI5NjUwODk5OA.GcDw7J.-IWdkEEx-fhwFz8XZyW8m7H8l4AL_a_wQ0aSPw")
