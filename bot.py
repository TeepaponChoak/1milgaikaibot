import os
import discord
import replicate
from discord.ext import commands

client = commands.Bot(command_prefix='~')

input = {
    "image": "https://replicate.delivery/pbxt/KW7Getr2zD5ECxySdBZtLmPa322lNkXrpkMdKcmxeaDmq2b1/MTk4MTczMTkzNzI1Mjg5NjYy.webp",
    "style": "Clay",
    "prompt": "a person in a post apocalyptic war game",
    "instant_id_strength": 0.8
}

output = replicate.run(
    "fofr/face-to-many:4912b99b3b101a70ae4af66c989d98f5b354c63fb8c4b5a248a299ac244242ed",
    input=input
)

@client.event
async def on_ready():
    print('Bot online!')

@client.command()
async def ping(ctx):
    await ctx.send(f'ping : ``{round(client.latency * 1000)}ms``')
async def pap(ctx):
    await ctx.send(output)