import discord
from discord.ext import commands
from discord.ext.commands import Bot
TOKEN = 'YOUR-BOT-TOKEN'
PREFIX = '!'
INTENTS = discord.Intents.all()
client = commands.Bot(command_prefix=PREFIX, intents=INTENTS)



@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="YOUR-ACTIVITY"))
    print(f'Logged in as: {client.user.name}')
    print(f'With ID: {client.user.id}')
@client.event
async def on_member_join(member):
    canal=client.get_channel(CHANNEL-ID-OF-WELCOME-CHANNEL)
    embed=discord.Embed(color=0x000000, title="BOT-NAME")
    embed.set_thumbnail(url="PASTE-A-LINK-FOR-THE-AVATAR")
    embed.add_field(name="**Welcome Message**", value=(f"Hey {member.mention}, welcome on {server}"), inline=True)
    await canal.send(embed=embed)
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, limit: int=None):
    async for msg in ctx.message.channel.history(limit=limit+1):
        await msg.delete()
@client.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def ban(context, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await context.send(f'The user **{member}** has been banned')
client.run(TOKEN)