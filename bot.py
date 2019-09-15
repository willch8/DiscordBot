#Author: Yong Woon Chung
#Date: September 14th, 2019
#Filename: bot.py
#Description: setting client event for discord bot. on_ready method

import discord
from discord.ext import commands
from discord.utils import get

import youtube_dl
import os

DEFAULT_ROLE = "bums"

client = commands.Bot(command_prefix = '/')

#client as instance of Bot
@client.event
async def on_ready(): 
    print('YongBot Ready!')

@client.event
async def on_member_join(member): 
    print(f'{member} has joined the OGSQUAD server!')
    role = get(member.guild.roles, name=DEFAULT_ROLE)
    await member.add_roles(role)
    print(f'{member} was given default role {role}')

@client.event
async def on_member_remove(member): 
    print(f'(member) is GONE!')

@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')

@client.command(aliases=['Nigin', 'Will'])
async def Nitin(ctx):
    await ctx.send('Nitin is a :snowflake:')

@client.command()
async def Jacob(ctx):
    await ctx.send('Jacob eats GRASS!')

@client.command(pass_context=True, aliases=['j', 'enter'])
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    #bug?
    await voice.disconnect()

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f'Yongbot connected to {channel}!\n')

    await ctx.send(f'Yongbot connected to {channel}!')

@client.command(pass_context=True, aliases=['l', 'dc'])
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f'Yongbot disconnected from {channel}!\n')
        await ctx.send(f'Yongbot disconnected from {channel}!')
    else:
        await ctx.send("I don't even know where you sitting at")

#add token
client.run('NjIyMzQ4MjQzMjc5MjgyMTg4.XXym4A.ud1RvEr-o20PszyzlXEyciVbHyg')
