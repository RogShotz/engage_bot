# ENGAGE Discord bot

Engage discord bot uses discord.py 2.0, which added a lot of ui changes and new interactions like discord modals and buttons, and finally, the use of slash commands.

Here are a general description of what each COG does:

- Welcome COG: Welcomes students and DM's them TOS of the server
- Misc COG: Handles miscallaneous commands, such as !ping.

## Useful commands/ Dev Operation
- !help - displays all currently available hidden commands
- /commands - displays all the currently available commands
- **/send_roles - this is IMPORTANT, if roles are ever updated, please do /send_roles in the #roles channels to update the info. It is not required, but it will allow students to find what roles they can use in the server**

## extension_loader Cog
This cog allows for the loading, unloading, and reloading of cogs while the bot is running. This allows for the bot to run without needing to reboot to load up new cogs. Running the loader saves you from having to terminate and rerun the bot. Note, the files must be updated wherever the bot is running for the new code to run. In its current iteration you would have to pull from git on the EC2 instance it is running on.

## EC2 Instance - Running the bot

Running the bot is simple, right now it is hosted by a AWS EC2 micro instance. In order to access this bot please contact me (Luke Rowe) to get supplied the credentials for accessing the instance. Right now the bot is running, and it uses nohup in order to keep running even when logged out of the ssh instance. Seek NoHup documentation, however it is very simple to understand.

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

## Further Development

Please refer to the readthedocs documentation for discord and discord 2.0 features. Additionally joining the discord.py discord has been a huge help in the devolpment/ good coding practices put into this project. Please try to follow formatting conventions and the organization in this project. I would recommend making sure you understand what is happening in each cog and how you can make a new one. For the most part making a new cog is as simple as copying and editing some names, then adjusting the methods inside to do what you want.

For localized testing, please follow any number of youtube videos on how to make a bot and just clone this bot. If needbe, you can scp the .env file off of the EC2 instance to your local machine. **DO NOT SHARE THIS FILE WITH ANYONE**

## Staffing considerations for the discord bot

In general anyone can be staff to monitor the server without any programming experience. The code written should work indefinately, or until a major update with discord API's comes out which could break some functions (unlikely). A staff member like this would only be there to moderate channels, perform moderator related activities like keeping up with events, customizing the server, etc. If someone where to change this bot, I would recommend a junior level programmer (someone entering into their junior year), as a lot of the API related services can prove to be hard to handle. In general though any shown experience in discord development would overshadow that recommendation, as well as general knowledge of how to write clean, effective, and maintanable code.

Both positions should expect a 2-4 hour work week, unless further discord developement is happening.
