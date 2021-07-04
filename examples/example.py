import discord_game
from discord_game import screen
import discord

def getToken() -> str:
    f = open("secret/token.txt", "r")
    d = f.read()
    f.close()

    return d

client = discord.Client()

game = discord_game.Game(client, "!start")

@game.event.onStart
async def onStart(s):
    mySprite = screen.Sprite(s, ["ABCDEFG"], 0, 0)
    await s.update()
    myButton = await s.addButton("test")

    @myButton.onClick
    async def yey(btn):
        print("pressed")

@game.event.onBotReady
async def onStart2():
    print("bot is ready")



client.run(getToken())
