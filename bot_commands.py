import os
import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!!', intents=intents)

index = 0  # Initialize index as a global variable

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def save_image(ctx):
    global index

    if ctx.message.attachments:
        for index, attachment in enumerate(ctx.message.attachments):
            if attachment.content_type.startswith('image'):
                if not os.path.exists('images'):
                    os.makedirs('images')
                filename = f'images/{index}_{attachment.filename}'
                async with attachment.open() as file:
                    async with open(filename, 'wb') as f:
                        await file.read()
                        f.write(file.getbuffer())
                await ctx.send(f'Image saved as: {filename}')
                await ctx.send(f'Attachment URL: {attachment.url}')

        if index == 0:
            await ctx.send('No images found in attachments.')
    else:
        await ctx.send('No attachments found in the message.')

@bot.command()
async def check_images(ctx):
    if os.path.exists('images'):
        files = os.listdir('images')
        image_urls = []

        if files:
            for file in files:
                file_path = os.path.join('images', file)
                if os.path.isfile(file_path) and file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                    attachment_url = f'attachment://{file}'
                    image_urls.append(attachment_url)
                    file_obj = discord.File(file_path)
                    await ctx.send(file=file_obj)

            if image_urls:
                await ctx.send("List of image URLs:")
                await ctx.send("\n".join(image_urls))
            else:
                await ctx.send('No images found in the images directory.')
        else:
            await ctx.send('No images found in the images directory.')
    else:
        await ctx.send('The images directory does not exist.')

