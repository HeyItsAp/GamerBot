import discord
import responses
import hehe

# Determin where the message is going
async def send_message(message, user_message, is_private):
    print('Message is ', message, ' User_message: ', user_message, 'Is_priveae? ', is_private)
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
        # print('The Response from bot: ', response)
        # if is_private:
        #     await message.author.send(response)
        # else:
        #     await message.channel.send(response)
    except Exception as e:
        print('Found Error:', e)

# Run the bot
def run_discord_bot():
    TOKEN = hehe.TOKEN
    # Complicated but i think its making the intents for the discord bot work?
    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)
    
    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

        
    @client.event
    # When the running discord bot sees a message
    async def on_message(message):
        # If the message sent the bot is checking is a message by the bot: Nothing
        if message.author == client.user:
            return
        
        username = str(message.author.name)
        user_message = str(message.content)
        channel = str(message.channel.name)

        print(f"{username} said '{user_message}' ({channel})")

        # check if the first four letters
        if user_message[0:4] == "GGWP":
            user_message = user_message[5:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)
    client.run(TOKEN)