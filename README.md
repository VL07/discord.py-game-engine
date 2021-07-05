# discord.py-game-engine

A game engine for discord

---

## How to use

If you want to see some examples go [here](https://github.com/VL07/discord.py-game-engine/tree/main/examples) or follow almong this tutorial to get a basic understanding of how this module works.

Start by importing the module

```python
import discord_game
from discord_game import screen
```

You will also need the discord libary to create the client

```python
import discord
```

Then you can start by creating the discord client

```python
client = discord.Client()
```

Now you can create the game and set its startcommand. Our is `!start`

```python
game = discord_game.Game(client, "!start")
```

Use the `onStart` event to run code when someone starts the game. The `onBotReady` runs when the bot/client is ready. 

```python
@game.event.onStart
async def onStart(display):
    print("The game is started")

@game.event.onBotReady
async def ready():
    print("bot is ready")
```

Don't forget to add `client.run(token)` at the end of the file

```python
client.run("Your token")
```

You can create a sprite like this

```python
mySprite = screen.Sprite(display, ["costume", "with", "multiple rows"], 0, 0) # and lastly x and y pos
```

Then you will need to update the display

```python
await display.update()
```

To create a button you do it like this

```python
myButton = await s.addButton("Click me!")
```

To get a button click put this code inside the onstart function

```python
@myButton.onClick
async def clicked(btn):
    print("You clicked me!")
```

The complete code

```python
import discord_game
from discord_game import screen
import discord

client = discord.Client()

game = discord_game.Game(client, "!start")

@game.event.onStart
async def onStart(display):
    print("The game is started")

@game.event.onBotReady
async def ready():
    print("bot is ready")

    mySprite = screen.Sprite(display, ["costume", "with", "multiple rows"], 0, 0) # and lastly x and y pos

    await display.update()

    myButton = await s.addButton("Click me!")

    @myButton.onClick
    async def clicked(btn):
        print("You clicked me!")
    
client.run("Your token")
```
