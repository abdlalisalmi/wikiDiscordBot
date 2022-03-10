import sys
import traceback
import discord
from discord.ext import commands


class CommandErrHandler(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		"""The event triggered when an error is raised while invoking a command.
		Parameters
		------------
		ctx: commands.Context
			The context used for command invocation.
		error: commands.CommandError
			The Exception raised.
		"""
		if isinstance(error, discord.ext.commands.CommandNotFound):
			embed = discord.Embed(
				title="",
				description="Sorry I don't know that command 🙂",
				color=0xff881a
			)
			await ctx.send(embed=embed)
		else:
			print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
			traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)