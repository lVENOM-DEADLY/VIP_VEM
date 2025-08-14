
# Copyright (C) 2024 by THE-VIP-BOY-OP@Github, <https://github.com/THE-VIP-BOY-OP>
#
# This file is part of <https://github.com/THE-VIP-BOY-OP/VIP-MUSIC> project,
# and is released under the MIT License.
# Please see <https://github.com/THE-VIP-BOY-OP/VIP-MUSIC/blob/master/LICENSE>
#
# All rights reserved.

from VIPMUSIC.core.bot import VIPBot
from VIPMUSIC.core.dir import dirr
from VIPMUSIC.core.git import git
from VIPMUSIC.core.userbot import Userbot
from VIPMUSIC.misc import dbb, heroku, sudo
from VIPMUSIC.platforms import (
    YouTubeAPI,
    CarbonAPI,
    SpotifyAPI,
    AppleAPI,
    RessoAPI,
    SoundAPI,
    TeleAPI
)
from .logging import LOGGER

def initialize_app():
    """Initialize and configure the VIP Music Bot application."""
    
    # Initialize directories
    LOGGER.info("Initializing directories...")
    dirr()
    
    # Check for Git updates
    LOGGER.info("Checking for Git updates...")
    git()
    
    # Initialize database
    LOGGER.info("Initializing database...")
    dbb()
    
    # Configure Heroku
    LOGGER.info("Configuring Heroku...")
    heroku()
    
    # Load sudo users
    LOGGER.info("Loading sudo users...")
    sudo()
    
    # Initialize main bot client
    LOGGER.info("Starting VIP Bot client...")
    app = VIPBot()
    
    # Initialize userbot client
    LOGGER.info("Starting Userbot client...")
    userbot = Userbot()
    
    # Initialize platform APIs
    LOGGER.info("Initializing platform APIs...")
    youtube = YouTubeAPI()
    carbon = CarbonAPI()
    spotify = SpotifyAPI()
    apple = AppleAPI()
    resso = RessoAPI()
    soundcloud = SoundAPI()
    telegram = TeleAPI()
    
    # Create HELPABLE dictionary
    HELPABLE = {}
    
    return {
        'app': app,
        'userbot': userbot,
        'youtube': youtube,
        'carbon': carbon,
        'spotify': spotify,
        'apple': apple,
        'resso': resso,
        'soundcloud': soundcloud,
        'telegram': telegram,
        'HELPABLE': HELPABLE
    }

# Initialize the application components
components = initialize_app()

# Make components available at package level
app = components['app']
userbot = components['userbot']
YouTube = components['youtube']
Carbon = components['carbon']
Spotify = components['spotify']
Apple = components['apple']
Resso = components['resso']
SoundCloud = components['soundcloud']
Telegram = components['telegram']
HELPABLE = components['HELPABLE']
