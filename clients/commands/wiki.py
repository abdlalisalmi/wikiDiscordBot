import wikipedia
import pyjokes
import datetime
import discord
import random
wikipedia.set_lang("en")

smile_emojies = ["😄", "😂", "🤣"]

def createEmbed(title, description, color=0xff881a):
	return discord.Embed(
		title=title,
		description=description,
		color=color
	)

def wiki_command(ctx, args) -> str:
	query = ' '.join(args)
	if not query:
		return createEmbed(title="", description=f'Hey {ctx.author.mention}, how can i help you 😃')
	else :
		try:
			if 'joke' in query or 'jokes' in query:
				return createEmbed(title="", description=f"{pyjokes.get_joke()} {smile_emojies[random.randint(0, 3)]}")
			elif 'time' in query:
				return createEmbed(title="", description=f"Current Time is {datetime.datetime.now().strftime('%H:%M:%S')}")
			elif 'date' in query:
				return createEmbed(title="", description=f"Today's date is {datetime.date.today().strftime('%B %d, %Y')}")
			elif 'your name' in query:
				return createEmbed(title="", description="My name is Wiki 😄")
			else:
				summary = wikipedia.summary(query, 3)
				return createEmbed(title=query, description=summary)
		except Exception as e:
			return createEmbed(title="", description="Sorry, I didn't understand, Please try again 😅")