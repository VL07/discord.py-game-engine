########################################################
####    Made by VL07
####    3/7-2021
########################################################


########################################################
####    Imports
########################################################

########################################################
####    Errors
########################################################

class Error(Exception):
    """Base class for other exceptions"""
    
    def __init__(self, message):
        super().__init__(message)


class Type(Error):
    """Base class for type exceptions"""
    def __init__(self, expected, got) -> None:
        self.e = expected
        self.g = got

        super().__init__(str(self))

    def __str__(self):
        return f"Exepted '{str(self.e)}' not '{str(self.g)}'"

########################################################
####    Prefix errors
########################################################

class InvalidParameterType(Type):
    """When the prefix is invalid"""

    def __init__(self, expected, got) -> None:
        self.e = expected
        self.g = got

        super().__init__(self.e, self.g)