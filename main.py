import os
import random
import discord
from keep_alive import keep_alive

# The core PUBG drop locations list
PUBG_DROPS = [
    "Pochinki (Erangel)", "School (Erangel)", "Mylta Power (Erangel)", "Georgopol (Erangel)", 
    "Novorepnoye (Erangel)", "Gatka (Erangel)", "Severny (Erangel)", "Prison (Erangel)", 
    "El Pozo (Miramar)", "Pecado (Miramar)", "Hacienda del Patrón (Miramar)", "Minas Generales (Miramar)", 
    "Los Leones (Miramar)", "San Martín (Miramar)", "Campo Militar (Miramar)", "Valle del Mar (Miramar)",
    "Camp Alpha (Sanhok)", "Paradise Resort (Sanhok)", "Bootcamp (Sanhok)", "Ruins (Sanhok)", 
    "Docks (Sanhok)", "Pai Nan (Sanhok)", "Mongnai (Sanhok)", "Sahmee (Sanhok)",
    "Cosmodrome (Vikendi)", "Castle (Vikendi)", "Winery (Vikendi)", "Dino Park (Vikendi)",
    "Villa (Vikendi)", "Hot Springs (Vikendi)", "Coal Mine (Vikendi)", "Tarmac (Vikendi)"
]

# Set up the bot
intents = discord.Intents.default()
intents.message_content = True # Required because we enabled MESSAGE CONTENT INTENT
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    """Confirms the bot is online and ready."""
    print(f'Bot is logged in as {client.user}')
    # Set the bot's status
    await client.change_presence(activity=discord.Game(name="PUBG Drop Roulette | !drop"))

@client.event
async def on_message(message):
    """Handles incoming messages and commands."""
    
    # Ignore messages sent by the bot itself
    if message.author == client.user:
        return

    # Check for the !drop command
    if message.content.lower().startswith('!drop'):
        # Pick a random location from the list
        drop_location = random.choice(PUBG_DROPS)
        
        # Send the message back to the channel
        await message.channel.send(
            f'**Landing Zone Selected!** 🚁\n'
            f'You are dropping at: **{drop_location}**\n'
            f'Good luck! May the Blue Zone be kind.'
        )

# Start the Flask web server to keep the bot alive
keep_alive()

# Run the bot using the token stored in the environment variables
# Note: The os.environ['TOKEN'] fetches the secret we set in Render
try:
    client.run(os.environ['TOKEN'])
except Exception as e:
    print(f"Error when running bot: {e}")
    print("Is your Discord TOKEN correct and the bot added to a server?")

