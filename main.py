import discord
from discord_slash import SlashCommand
import youtube_dl
import random

client = discord.Client(intents=discord.Intents.all())
slash = SlashCommand(client, sync_commands=True)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


guild_ids = []  # Put your server ID in this array.
discord_bot_Key = 'discord_key'  # key for discord


@slash.slash(name="test", guild_ids=guild_ids, description='test latenency')
async def _test(ctx):
    await ctx.send(f"Pong! ({client.latency * 1000}ms)")


@slash.slash(name="connect", guild_ids=guild_ids, description="The bot is ready to party.")
async def _connect(ctx):
    await ctx.send('attempting to join')
    if ctx.author.voice is None:
        await ctx.send("User not in voice channel")
    voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
        await voice_channel.connect()
        await ctx.send("Joining")
    else:
        await ctx.voice_client.move_to(voice_channel)


@slash.slash(name="disconnect", guild_ids=guild_ids, description="Bot has work tomorrow.")
async def _disconnect(ctx):
    await ctx.send('Time to head home')
    await ctx.voice_client.disconnect()


@slash.slash(name="m_play", guild_ids=guild_ids, description="Bot has work tomorrow.")
async def _m_play(ctx, url):
    ctx.voice_client.stop()
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    YDL_OPTIONS = {'format': 'bestaudio'}
    vc = ctx.voice_client

    await ctx.send("try to play music")

    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']
        source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
        vc.play(source)


@slash.slash(name="m_pause", guild_ids=guild_ids, description="The error is a future not a bug.")
async def _pause(ctx):
    await ctx.send('pausing music')
    await ctx.voice_client.pause()


@slash.slash(name="m_resume", guild_ids=guild_ids, description="This error is also future not a bug.")
async def _resume(ctx):
    await ctx.send('resuming music')
    await ctx.voice_client.resume()


@slash.slash(name="no", guild_ids=guild_ids, description="no")
async def _no(ctx):
    url_dict = {0: 'https://www.youtube.com/watch?v=C-BGuM83LnY',
                1: 'https://www.youtube.com/watch?v=qWwb8S02f_c',
                2: 'https://www.youtube.com/watch?v=LbAxSWqJrOc',
                3: 'https://www.youtube.com/watch?v=tKIKY0CuAKo'}

    url = url_dict[random.randint(0, len(url_dict))]
    ctx.voice_client.stop()

    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    YDL_OPTIONS = {'format': 'bestaudio'}
    vc = ctx.voice_client

    await ctx.send("NoooOOOooooo")

    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']
        source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
        vc.play(source)


@slash.slash(name="yes", guild_ids=guild_ids, description="yes")
async def _yes(ctx):
    url_dict = {0: 'https://www.youtube.com/watch?v=jA3VPFBh6Lk',
                1: 'https://www.youtube.com/watch?v=5OIl24aOFMM'}

    url = url_dict[random.randint(0, len(url_dict))]
    ctx.voice_client.stop()

    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    YDL_OPTIONS = {'format': 'bestaudio'}
    vc = ctx.voice_client

    await ctx.send("Yes")

    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']
        source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
        vc.play(source)


@slash.slash(name="congrats", guild_ids=guild_ids, description="Congrats")
async def _congrats(ctx):
    url_dict = {0: 'https://www.youtube.com/watch?v=3cuQT1YZfVc'}

    url = url_dict[random.randint(0, len(url_dict))]
    ctx.voice_client.stop()

    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    YDL_OPTIONS = {'format': 'bestaudio'}
    vc = ctx.voice_client

    await ctx.send("Congrats")

    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']
        source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
        vc.play(source)


@slash.slash(name="Sussy_Baka", guild_ids=guild_ids, description="Sussy BAKA")
async def _Sussy_Baka(ctx):
    url_dict = {0: 'https://www.youtube.com/watch?v=vAwG0KfB83I'}

    url = url_dict[random.randint(0, len(url_dict))]
    ctx.voice_client.stop()

    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    YDL_OPTIONS = {'format': 'bestaudio'}
    vc = ctx.voice_client

    await ctx.send("Sussy BAKA")

    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']
        source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
        vc.play(source)


@slash.slash(name="Good_Job", guild_ids=guild_ids, description="The more you use this the more it is disvalued")
async def _Good_Job(ctx):
    url_dict = {0: 'https://www.youtube.com/watch?v=3uobf8l4qMc'}

    url = url_dict[random.randint(0, len(url_dict))]
    ctx.voice_client.stop()

    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    YDL_OPTIONS = {'format': 'bestaudio'}
    vc = ctx.voice_client

    await ctx.send("Wow")

    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False)
        url2 = info['formats'][0]['url']
        source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
        vc.play(source)


# @slash.slash(name="Local_playlist", guild_ids=guild_ids, description="Playing off the local playlist")
# async def _Local_playlist(ctx):


@slash.slash(name="agree", guild_ids=guild_ids, description="Max is my owner and I don't want to get scraped.")
async def _agree(ctx):
    await ctx.send('I agree with Max')


@slash.slash(name="command_list", guild_ids=guild_ids, description="List of commands")
async def _command_list(ctx):
    await ctx.send('__**BOT COMMANDS**__\n'
                   '/connect : connecting to voice chat \n'
                   '/disconnect : disconnecting the bot from voice chat \n'
                   '__**Music_bot commands**__\n'
                   '/m_play : Add url of youtube to play the music \n'
                   '/m_pause : Pauses the music Bot\n'
                   '/m_resume : Resumes the music after \n'
                   '__**Random Sound Effects**__\n'
                   '/yes : Random Yes\n'
                   '/no : Random NO\n'
                   '/congrats : we only have one line for this one\n'
                   '/good_job : one line for this \n'
                   '__**Feature that will be added**__\n'
                   '/m_loop : Loops current song\n'
                   '/mp_loop : Loops current playlist\n'
                   '/m_queue : Queue the song from given url\n'
                   '/m_skip : Skips current song \n'
                   'With more to come\n'
                   'if you have ideas do tell')


client.run(discord_bot_Key)

