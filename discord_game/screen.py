########################################################
####    Made by VL07
####    3/7-2021
########################################################

########################################################
####    Imports
########################################################

from discord_game import errors
import discord
from discord_components import Button, ButtonStyle, InteractionType

class Embed:
    empty = "\u200B"

########################################################
####    Sprite
########################################################

class Sprite:
    def __init__(self, display, costume: list, posX: int, posY: int) -> None:
        if not isinstance(display, Display) or not isinstance(costume, list) or not isinstance(posX, int) or not isinstance(posY, int):
            raise errors.InvalidParameterType("display: Display, costume: list, posX: int, posY: int", "Invalid parameter")

        self.display = display
        self.costume = costume
        self.posX = posX
        self.posY = posY

        # [self.posX:(self.posX + len(row))]
        # [self.posY:(self.posY + (len(self.costume) - 1))]

        self.rerenderSpriteOnDisplay()

    def rerenderSpriteOnDisplay(self) -> None:
        for i in range(len(self.costume)):
            for col in range(len(self.costume[i])):
                self.display._textToDisplay[self.posY + i][self.posX + col] = self.costume[i][col]

    def setPos(self, x, y) -> None:
        self.posX = x
        self.posY = y
                
########################################################
####    Button
########################################################

allButtons = {}

class Btn:
    def __init__(self, display, id) -> None:
        self.display = display
        self.id = id

    def onClick(self, func):
        self.display._events["onButtonClick"][self.id] = func
        def wraper():
            func()
        return wraper

    async def _callFunc(self, btn):
        try:
            pass
        except NameError as err:
            print(err)

        await self.display._events["onButtonClick"][btn.custom_id](btn)



########################################################
####    Display
########################################################

class Display:
    def __init__(self, game, message, ctx, name, description, footer, color, background="#", spaceBetween=True):
        self.message = message
        self.ctx = ctx
        self._textToDisplay = [
            [[background], [background], [background], [background], [background], [background], [background], [background], [background], [background]],
            [[background], [background], [background], [background], [background], [background], [background], [background], [background], [background]],
            [[background], [background], [background], [background], [background], [background], [background], [background], [background], [background]],
            [[background], [background], [background], [background], [background], [background], [background], [background], [background], [background]],
            [[background], [background], [background], [background], [background], [background], [background], [background], [background], [background]],
            [[background], [background], [background], [background], [background], [background], [background], [background], [background], [background]],
            [[background], [background], [background], [background], [background], [background], [background], [background], [background], [background]],
            [[background], [background], [background], [background], [background], [background], [background], [background], [background], [background]],
            [[background], [background], [background], [background], [background], [background], [background], [background], [background], [background]],
            [[background], [background], [background], [background], [background], [background], [background], [background], [background], [background]]
        ]

        self.game = game

        self.name = name
        self.description = description
        self.footer = footer
        self.color = color

        self._components = []
        self._buttonIds = []

        self._events = {"onButtonClick": {}}

        self.spaceBetween = spaceBetween
        self.background = background



    async def update(self):
        textToDisplay = ""

        for row in self._textToDisplay:
            for column in row:
                textToDisplay += column[0] + "\t"
            textToDisplay += "\n"

        embed = discord.Embed(title=self.name if self.name else Embed.empty, description=self.description if self.description else Embed.empty, color=self.color)
        embed.add_field(name=Embed.empty, value=textToDisplay if textToDisplay else Embed.empty, inline=False)
        embed.add_field(name=Embed.empty, value=self.footer if self.footer else Embed.empty, inline=False)

        if self._components:
            await self.message.edit(embed=embed, components=self._components)
        else:
            await self.message.edit(embed=embed)

    async def addButton(self, label, emoji=None, url=None, style=ButtonStyle.gray, disabled=False, inline=True):
        global allButtons

        if emoji and url:
            btn = Button(style=style, label=label, disabled=disabled, emoji=emoji, url=url)
        elif emoji:
            btn = Button(style=style, label=label, disabled=disabled, emoji=emoji)
        elif url:
            btn = Button(style=style, label=label, disabled=disabled, url=url)
        else:
            btn = Button(style=style, label=label, disabled=disabled)

        if inline:
            if len(self._components):
                self._components[-1].append(btn)
            else:
                self._components.append([btn])
        else:
            self._components.append([btn])

        btnCls = Btn(self, btn.custom_id)

        allButtons[btn.custom_id] = btnCls

        return btnCls

    def setToBg(self):
        self._textToDisplay = [
            [[self.background], [self.background], [self.background], [self.background], [self.background], [self.background], [self.background], [self.background], [self.background], [self.background]],
            [[self.background], [self.background], [self.background], [self.background], [self.background], [self.background], [self.background], [self.background], [self.background], [self.background]],
            [[self.background], [self.background], [self.background], [self.background], [self.background], [self.background], [self.background], [self.background], [self.background], [self.background]],
            [[self.background], [self.background], [self.background], [self.background], [self.background], [self.background], [self.background], [self.background], [self.background], [self.background]],
            [[self.background], [self.background], [self.background], [self.background], [self.background], [self.background], [self.background], [self.background], [self.background], [self.background]],
            [[self.background], [self.background], [self.background], [self.background], [self.background], [self.background], [self.background], [self.background], [self.background], [self.background]],
            [[self.background], [self.background], [self.background], [self.background], [self.background], [self.background], [self.background], [self.background], [self.background], [self.background]],
            [[self.background], [self.background], [self.background], [self.background], [self.background], [self.background], [self.background], [self.background], [self.background], [self.background]],
            [[self.background], [self.background], [self.background], [self.background], [self.background], [self.background], [self.background], [self.background], [self.background], [self.background]],
            [[self.background], [self.background], [self.background], [self.background], [self.background], [self.background], [self.background], [self.background], [self.background], [self.background]],
        ]

    async def lose(self):
        self.name = "You lose: " + self.name

        self._components = None

        await self.update()


        
