########################################################
####    Made by VL07
####    3/7-2021
########################################################


########################################################
####    Imports
########################################################

import discord
from discord_components import DiscordComponents
from discord_game import errors, events, screen



########################################################
####    Game
########################################################

class Game:
    def __init__(self, client: discord.Client, startCommand: str, background="#") -> None:

        if not isinstance(client, discord.Client):
            raise errors.InvalidParameterType("discord.Client", str(client))

        if not isinstance(startCommand, str):
            raise errors.InvalidParameterType("str", str(startCommand))
        

        self._client = client
        self.startCommand = startCommand
        self.event = events.Event(self)
        self._events = {"onStart": [], "onBotReady": []}

        # Options
        self.name = "Game"
        self.description = "A game made with the `discord_game` module"
        self.footer = "`discord_game` is made by VL07"
        self.color = 0x6ea5ff

        self.display = """Loading"""

        self.background = background

        ########################################################
        ####    Events
        ########################################################

        @self._client.event
        async def on_ready():
            DiscordComponents(self._client)

            for event in self._events["onBotReady"]:
                await event()

        @self._client.event
        async def on_message(message):
            if message.content == self.startCommand and not message.author.bot:

                embed = discord.Embed(title=self.name, description=self.description, color=self.color)
                embed.add_field(name="\u200B", value=self.display, inline=False)
                embed.add_field(name="\u200B", value=self.footer, inline=False)

                sentMessage = await message.channel.send(embed=embed)

                for event in self._events["onStart"]:
                    await event(screen.Display(sentMessage, message, self.name, self.description, self.footer, self.color, background=self.background))

        @self._client.event
        async def on_button_click(btn):
            for buttonId, button in screen.allButtons.items():
                print(buttonId)
                print(btn.custom_id)
                if buttonId == btn.custom_id:
                    await button._callFunc(btn)
                    break



