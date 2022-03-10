#!/usr/bin/env python3
import os
import sys
import discord
from clients.custom_bot_client import CustomBotClient
from cogs.listeners import Listeners
from cogs.command_err_handler import CommandErrHandler
from decouple import config


TOKEN = config('TOKEN')

def main():

	intents = discord.Intents.default()
	intents.members = True
	bot = CustomBotClient(
		command_prefix='/', 
		intents=intents
	)
	bot.add_cog(Listeners(bot))
	bot.add_cog(CommandErrHandler(bot))
	bot.run(TOKEN)


if __name__ == "__main__":
	main()