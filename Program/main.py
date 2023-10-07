# Discord bot import
import discord
from discord import app_commands
from discord import ui
import os
from dotenv import load_dotenv
#import glob
#import ndjson
#import time

# Bot start
load_dotenv()

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print("接続しました！")
    # await client.change_presence(activity=discord.Game(name="/help"))
    await tree.sync()#スラッシュコマンドを同期
    print("グローバルコマンド同期完了！")
    # await tree.sync(guild=discord.Object(your_guild_id)) 
    # print("ギルドコマンド同期完了！")

#Bot commands
# /test
@tree.command(name="test",description="テストコマンドです。")
async def test_command(interaction: discord.Interaction,text:str):
    await interaction.response.defer(ephemeral=False)

    await interaction.followup.send(text)

    #await interaction.response.send_message(text, ephemeral=False)



client.run(os.environ['token'])