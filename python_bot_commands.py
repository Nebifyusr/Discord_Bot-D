import discord
from discord.ext import commands

pythonmode = 0

error_id = {
    "p01": "command not in python",
    "p02": "problem at python",
    "s01": "server error while executing"
}
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!!', intents=intents)


@bot.command()
async def python_mode(ctx):
    global pythonmode
    await ctx.send('==========================')
    pythonmode += 1
    if pythonmode == 2:
        pythonmode = 0
        await ctx.send('python mode not')
    elif pythonmode == 1:
        await ctx.send("python mode")
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

