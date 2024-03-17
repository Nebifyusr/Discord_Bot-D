"""
Created by: UmbraScript
Start-Date: 17/03/2024
Latest-Version: A.101
Description: Python Discord Python Bot
"""

import os
import discord
from discord.ext import commands
import requests
pythonmode = 0
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!!', intents=intents)

index = 0  # Initialize index as a global variable






@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def testing_mode(ctx):
    global pythonmode
    await ctx.send('==========================')
    pythonmode += 1
    if pythonmode == 2:
        pythonmode = 0
        await ctx.send('testing mode not')
    elif pythonmode == 1:
        await ctx.send("testing mode")
    else:
        pythonmode = 0
    await ctx.send('==========================')


@bot.command()
async def test_1(ctx):
    if pythonmode == 0:
        try:
            await ctx.send(f'Successfully logged in as: {bot.user}!')
        except Exception as e:
            print(f"Error while executing test_1: {e}")
            # You can log the error to a file or other logging mechanism here
    else:
        await ctx.send('command not in python language!')


@bot.command()
async def save_image(ctx):
    if pythonmode == 0:
        global index

        if ctx.message.attachments:
            for index, attachment in enumerate(ctx.message.attachments):
                if attachment.content_type.startswith('image'):
                    if not os.path.exists('images'):
                        os.makedirs('images')
                    filename = f'images/{index}_{attachment.filename}'
                    image_data = await attachment.read()  # Read the attachment data
                    with open(filename, 'wb') as f:
                        f.write(image_data)
                    await ctx.send(f'Image saved as: {filename}')
                    await ctx.send(f'Attachment URL: {attachment.url}')

            if index == 0:
                await ctx.send('No images found in attachments.')
        else:
            await ctx.send('No attachments found in the message.')
    else:
        await ctx.send('command not in python language!')

@bot.command()
async def change_prefix(ctx, new_prefix: str):
    if pythonmode == 0:
        # Zmiana prefiksu bota
        bot.command_prefix = new_prefix
        await ctx.send(f"Prefiks został zmieniony na: {new_prefix}")
    else:
        await ctx.send('Komenda nie jest obsługiwana w trybie Pythona.')

@bot.command()
async def check_images(ctx):
    if pythonmode == 0:
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
    else:
        await ctx.send('command not in python language!')

@bot.command()
async def print(ctx, *, expression):
    if pythonmode == 1:
        try:
            result = eval(expression)
            await ctx.send(f'Result: {result}')
        except:
            if len(ctx.message.content) > 8:  # Ensure there are at least 9 characters
                await ctx.send(ctx.message.content[8:])  # Send the content starting from the 9th character
    else:
        await ctx.send('Command not available in this mode.')

bot.run('MTIxODg2Nzk2Mzg4NTY1NDA4Ng.G1KWtb.33STOQuxN7qMW62QnhnThOPWTneWeDUDaRppU0')
