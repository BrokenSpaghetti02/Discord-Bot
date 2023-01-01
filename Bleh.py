import discord
import random

def update_encouragements(encouraging_message):
  em_file = open("em.txt", "a")
  em_file.write(encouraging_message)
  em_file.write("\n")
  em_file.close()
 
def update_sad_words(sad_words):
  sw_file = open("sw.txt", "a")
  sw_file.write(sad_words)
  sw_file.write("\n")
  sw_file.close()

greet = ["Yee, I'm alive!", "What do you want? Off course I'm alive", "What's up dwag?", "Sometimes", "Nope", "If I was alive, would I be able to have sex?"]

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

  msg = message.content

  if message.author == client.user:
    return
  
  if msg.startswith('-alive?'):
    await message.channel.send(random.choice(greet))

  if msg.startswith('-bj'):
    channel = message.author.voice.channel
    await channel.connect()
  
  if msg.startswith('-bdc'):
    await message.guild.voice_client.disconnect()
  
  sw_list = []
  sw_list_imrpoved = []
  for sw in open("sw.txt", "r").readlines():
    sw_list.append(sw)
  for swi in sw_list:
    sw_list_imrpoved.append(swi.strip())
  
  em_list = []
  em_list_improved = []
  for em in open("em.txt", "r").readlines():
    em_list.append(em)
  for emi in em_list:
    em_list_improved.append(emi.strip())

  if any(word in msg.lower() for word in sw_list_imrpoved):
    await message.channel.send(random.choice(em_list_improved))

  if msg.startswith("-new"):
    encouraging_message = msg.split("-new ", 1)[1]
    if encouraging_message in em_list_improved:
      await message.channel.send("Encouraging message already added!")
    else:
      update_encouragements(encouraging_message)
      await message.channel.send("New encouraging message added!")
  
  if msg.startswith("-addsw"):
    sad_words = msg.split("-addsw ", 1)[1]
    if sad_words in sw_list_imrpoved:
      await message.channel.send("Sad already added!")
    else:
      update_sad_words(sad_words)
      await message.channel.send("New sad word added!")
  
  if msg.startswith("-emlist"):
    await message.channel.send(em_list_improved)

  if msg.startswith("-swlist"):
    await message.channel.send(sw_list_imrpoved)

  if msg.lower().startswith("naughty america"):
    await message.channel.send("Nobody, nobody does it better... 😉")
  
client.run("INSERT TOKEN HERE")