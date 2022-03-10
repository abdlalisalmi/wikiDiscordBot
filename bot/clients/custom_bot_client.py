from discord.ext import commands


class CustomBotClient(commands.Bot):

    async def on_ready(self):
        print(f'{self.user.name} has connected to Discord!')




# import discord

# class EventsClient(discord.Client):
# 	async def on_ready(self):
# 		print(f'{self.user} has connected to Discord!')
	
# 	async def on_member_join(member):
# 		await member.create_dm()
# 		await member.dm_channel.send(
# 			f'Hi {member.name}, welcome to my Discord server!'
# 		)
	
# 	async def on_message(self, message):
# 		if message.author == self.user:
# 			return
# 		response = "wah hhh"
# 		await message.channel.send(response)



# from discord.ext import commands
# from discord.ext.commands import command

# class CommandClient(commands.Bot):

# 	async def on_ready(self):
# 		print(f'{self.user} has connected to Discord!')

# 	@command(name="wiki")
# 	async def wiki_command(ctx):
# 		print(ctx)
# 		# try:
# 		# 	if 'joke' in query or 'jokes' in query:
# 		# 		print(pyjokes.get_joke())
# 		# 	elif 'time' in query:
# 		# 		print("Current Time is", datetime.datetime.now().strftime("%H:%M:%S"))
# 		# 	elif 'date' in query:
# 		# 		print("Today's date is", datetime.date.today().strftime("%B %d, %Y"))
# 		# 	elif 'your name' in query:
# 		# 		print("My name is ****")
# 		# 	else:
# 		# 		summary = wikipedia.summary(query, 2)
# 		# 		print(summary)
# 		# except Exception as e:
# 		# 	print("Sorry, I didn't understand, Please enter an other command 😅")
# 		await ctx.send("response")
