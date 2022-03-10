import discord


from clients.commands.wiki import wiki_command

class Listeners(discord.ext.commands.Cog, name='Listeners module'):
	def __init__(self, bot):
		self.bot = bot

	@discord.ext.commands.command(name="wiki")
	async def wiki_command(self, ctx, *args):
		await ctx.send(embed=wiki_command(ctx, args))
		
	@discord.ext.commands.Cog.listener()
	async def on_member_join(self, member):
		channel = member.guild.system_channel
		if channel is not None:
			await channel.send(f'A wild {member.mention} has appeared!')

	# @discord.ext.commands.Cog.listener()
	# async def on_message(self, message):
	# 	if message.author == self.user:
	# 		return
	# 	response = "wah hhh"
	# 	await message.channel.send(response)
