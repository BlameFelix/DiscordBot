import discord
import time

TOKEN = 'your token' #Add Bot token

client = discord.Client()

@client.event
async def on_message(message):
    # prevent bot from reacting to his own messages
    if message.author == client.user:
        return
    #saing hello back to user
    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    #sascha ;)
    if message.content.startswith("!Sascha"):
        msg = 'Der hat doch kein Aim :joy:'.format(message)
        await client.send_message(message.channel, msg)
    #function to interact with RedditBot, EndlessLoop
    if message.content.startswith("!reddit"):
        msg = 'reddit new DestinyMemes 1'.format(message)
        while(True):
            await client.send_message(message.channel, msg)
            time.sleep(10000) #sleep time, ajust depending on ur usage

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
