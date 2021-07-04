########################################################
####    Made by VL07
####    3/7-2021
########################################################

########################################################
####    Imports
########################################################

########################################################
####    Events
########################################################

class Event:
    def __init__(self, game) -> None:
        self._game = game

    def onStart(self, func):
        self._game._events["onStart"].append(func)
        def wrapper():
            func()
        return wrapper

    def onBotReady(self, func):
        self._game._events["onBotReady"].append(func)
        def wrapper():
            func()
        return wrapper

