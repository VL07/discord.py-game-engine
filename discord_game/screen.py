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

    def rerenderSpriteOnDisplay(self):
        for i in range(len(self.costume)):
            for col in range(len(self.costume[i])):
                self.display._textToDisplay[self.posY + i][self.posX + col] = self.costume[i][col]
                
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
            print(self.display._events)
            await self.display._events["onButtonClick"][btn.custom_id](btn)
        except Exception as err:
            print(error)
            print(err)


########################################################
####    Display
########################################################

class Display:
    def __init__(self, message, ctx, name, description, footer, color, background="#"):
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

        self.name = name
        self.description = description
        self.footer = footer
        self.color = color

        self._components = []
        self._buttonIds = []

        self._events = {"onButtonClick": {}}



    async def update(self):
        textToDisplay = ""

        for row in self._textToDisplay:
            for column in row:
                textToDisplay += column[0] + "\t"
            textToDisplay += "\n"

        embed = discord.Embed(title=self.name, description=self.description, color=self.color)
        embed.add_field(name=Embed.empty, value=textToDisplay, inline=False)
        embed.add_field(name=Embed.empty, value=self.footer, inline=False)

        await self.message.edit(embed=embed, components=self._components)

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


        await self.update()

        btnCls = Btn(self, btn.custom_id)

        allButtons[btn.custom_id] = btnCls

        return btnCls

        