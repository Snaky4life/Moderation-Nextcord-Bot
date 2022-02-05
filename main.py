import nextcord
from nextcord.ext import commands
import os
from keep_alive import keep_alive

client = commands.Bot(command_prefix = ';;')

@client.event
async def on_ready():
	await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="Gamer Club"))
	print(f"Logged in")

@client.command()
async def ban(ctx, user: nextcord.User, reason):
	guild = ctx.guild
	embed=nextcord.Embed(
		title="Success!",
		description=f"{user} has been successfully banned for {reason}.",
		color=0x2c00ff
	)
	if ctx.author.guild_permissions.ban_members:
		await ctx.send(embed=embed)
		await guild.ban(user=user, reason=reason)
		await user.send(f"You have been banned in {ctx.guild.name} for {reason}")

@client.command()
async def unban(ctx, user: nextcord.User):
	guild = ctx.guild
	embed = nextcord.Embed(
		title="Success!",
		description=f"{user} has been successfully unbanned",
		color=0x2c00ff
	)
	if ctx.author.guild_permissions.ban_members:
		await ctx.send(embed=embed)
		await guild.unban(user=user)
		await user.send(f"You have been unbanned in {ctx.guild.name}\nHere is the invitation: https://discord.gg/FbkA7vGNrE")

@client.command()
async def kick(ctx, user: nextcord.User, reason=None):
	guild = ctx.guild
	embed = nextcord.Embed(
		title="Success!",
		description=f"{user} has been successfully kicked for {reason}",
		color=0x2c00ff
	)
	if ctx.author.guild_permissions.kick_members:
		await ctx.send(embed=embed)
		await guild.kick(user=user, reason=reason)
		await user.send(f"You have been kicked in {ctx.guild.name}\nHere is the invitation: https://discord.gg/FbkA7vGNrE")


keep_alive()
client.run(os.getenv("TOKEN"))