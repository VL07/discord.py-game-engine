import discord_game
from discord_game import screen
import discord
import asyncio
import random

def getToken() -> str:
    f = open("secret/token.txt", "r")
    d = f.read()
    f.close()

    return d

client = discord.Client()

game = discord_game.Game(client, "!", background="⬛", spaceBetween=False)

class Direction:
    pass
class Score:
    pass

@game.event.onStart
async def onStart(display):
    print("start")

    #display.name = "Snake - press a button to start"
    
    snake = [screen.Sprite(display, ["🟥"], 5, 5), screen.Sprite(display, ["🟥"], 5, 6)]
    apple = screen.Sprite(display, ["🍏"], 5, 4)

    upBtn = await display.addButton("Up", emoji="⬆", style=screen.ButtonStyle.green, inline=False)
    leftBtn = await display.addButton("Left", emoji="⬅", style=screen.ButtonStyle.green, inline=False)
    rightBtn = await display.addButton("Right", emoji="➡", style=screen.ButtonStyle.green, inline=True)
    downBtn = await display.addButton("Down", emoji="⬇", style=screen.ButtonStyle.green, inline=False)


    d = Direction()
    d.direction = "up"

    s = Score()
    s.score = 0

    display.name = "Snake | " + str(s.score)
    display.description = "A minigame made by `VL07`"
    display.footer = "Please report bugs [here](https://github.com/VL07/discord.py-game-engine/issues)"

    await display.update()

    @upBtn.onClick
    async def moveUp(btn):
        d.direction = "up" if d.direction != "down" else "down"

        await btn.respond(
            type=screen.InteractionType.UpdateMessage, content="-"
        )


    @leftBtn.onClick
    async def moveLeft(btn):
        d.direction = "left" if d.direction != "right" else "right"

        await btn.respond(
            type=screen.InteractionType.UpdateMessage, content="-"
        )


    @rightBtn.onClick
    async def moveRight(btn):
        d.direction = "right" if d.direction != "left" else "left"

        await btn.respond(
            type=screen.InteractionType.UpdateMessage, content="-"
        )

    @downBtn.onClick
    async def moveDown(btn):
        print(d.direction)
        d.direction = "down" if d.direction != "up" else "up"

        await btn.respond(
            type=screen.InteractionType.UpdateMessage, content="-"
        )


    lose = False

    while True:
        await asyncio.sleep(2)

        lastPosX = snake[0].posX
        lastPosY = snake[0].posY

        if d.direction == "up": 
            if snake[0].posY - 1 < 0 or display._textToDisplay[snake[0].posY - 1][snake[0].posX] == "🟥":
                lose = True
                break

            snake[0].posY -=1

            print(snake[0].posY)

            display.setToBg()

            snake[0].rerenderSpriteOnDisplay()




        elif d.direction == "down":

            if snake[0].posY + 1 > 9 or display._textToDisplay[snake[0].posY + 1][snake[0].posX] == "🟥":
                lose = True 
                break

            snake[0].posY +=1

            print(snake[0].posY)

            display.setToBg()

            snake[0].rerenderSpriteOnDisplay()

           

        elif d.direction == "left": 

            if snake[0].posX - 1 < 0 or display._textToDisplay[snake[0].posY][snake[0].posX - 1] == "🟥":
                lose = True
                break

            snake[0].posX -=1

            print(snake[0].posY)

            display.setToBg()

            snake[0].rerenderSpriteOnDisplay()

            

        elif d.direction == "right":
            if snake[0].posX + 1 > 9 or display._textToDisplay[snake[0].posY][snake[0].posX + 1] == "🟥":
                lose = True
                break

            snake[0].posX +=1

            print(snake[0].posY)

            display.setToBg()

            snake[0].rerenderSpriteOnDisplay()

        

        for snakePart in snake[1:]:
            lastPosX2 = snakePart.posX
            lastPosY2 = snakePart.posY

            snakePart.posX = lastPosX
            snakePart.posY = lastPosY

            snakePart.rerenderSpriteOnDisplay()

            lastPosX = lastPosX2
            lastPosY = lastPosY2

        print(display._textToDisplay[apple.posY])

        print(display._textToDisplay[apple.posY][apple.posX])
        if display._textToDisplay[apple.posY][apple.posX][0] == "🟥":
            snake.append(screen.Sprite(display, ["🟥"], lastPosX, lastPosY))

            s.score = s.score + 1

            while display._textToDisplay[apple.posY][apple.posX][0] == "🟥":
                apple.posX = random.randint(0, 9)
                apple.posY = random.randint(0, 9)

            apple.rerenderSpriteOnDisplay()
        else:
            apple.rerenderSpriteOnDisplay()

        
       
        display.name = "Snake | " + str(s.score)
        await display.update()
    await display.update()

    if lose:
        await display.lose()



@game.event.onBotReady
async def onStart2():
    print("bot is ready")





client.run(getToken())
