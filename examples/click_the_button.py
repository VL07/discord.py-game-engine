import discord_game
from discord_game import screen
import discord
from discord_components import InteractionType

def getToken() -> str:
    f = open("secret/token.txt", "r")
    d = f.read()
    f.close()

    return d

client = discord.Client()

game = discord_game.Game(client, "!start", background="")

clicks = 0
@game.event.onStart
async def onStart(display):
    global clicks
    mySprite = screen.Sprite(display, ["Clicks:", str(clicks)], 0, 0)
    myButton = await display.addButton("Click me!")

    @myButton.onClick
    async def click(btn):
        global clicks
        print("pressed1")
        clicks += 1
        print(clicks)
        mySprite.costume = ["Clicks:", str(clicks)]
        mySprite.rerenderSpriteOnDisplay()
        await display.update()

        await btn.respond(
            type=InteractionType.ChannelMessageWithSource, content="You pressed the button"
        )


@game.event.onBotReady
async def onStart2():
    print("bot is ready")



client.run(getToken())
