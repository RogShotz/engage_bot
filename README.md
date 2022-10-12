# ENGAGE Discord bot

Engage discord bot uses discord.py 2.0, which added a lot of ui changes and new interactions like discord modals and buttons, and finally, the use of slash commands.

Here are a general description of what each COG does:

- Welcome COG: Welcomes students and DM's them TOS of the server
- Misc COG: Handles miscallaneous commands, such as !ping.

## Useful commands/ Dev Operation
- !help - displays all currently available hidden commands
- /commands - displays all the currently available commands

## extension_loader Cog
This cog allows for the loading, unloading, and reloading of cogs while the bot is running. This allows for the bot to run without needing to reboot to load up new cogs.

## Bot Setup

1. Install discord modules
    1. pip install -r requirements.txt
1. Install Rapptz discord.py 2.0
    1. ```pip install -U git+https://github.com/Rapptz/discord.py```
1. Obtain .env file for sensitive data (ask contributors)
    1. NEVER SHARE OUTSIDE OF Engage
    1. DO NOT UPLOAD TO GIT
1. Run main bot.py to start bot


## Contributors

Luke Rowe
