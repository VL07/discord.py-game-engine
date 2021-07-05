import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="discord_game",
    version="0.1.2",
    description="Create a discord game",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/VL07/discord.py-game-engine",
    author="VL07",
    author_email="victor.lundman.07@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=["discord", "discord_components"],
)