from functions import *
from settings import *
from discord.ext import commands

description = '''A bot focused on alerting for Emergency Quests on PSO2.'''

bot = commands.Bot(command_prefix=['!', '`', '_'], description=description,
                   command_not_found='Command not recognized. Try the ``help`` command.')
extensions = [
    'cogs.general',
    'cogs.eq',
    'cogs.macro'
]


@bot.event
async def on_ready():
    botInfo = await bot.application_info()
    oauthlink = discord.utils.oauth_url(botInfo.id)

    print('---------')
    print('Username: {}'.format(bot.user.name))
    print('ID: {}'.format(bot.user.id))
    print('Server count: {}'.format(str(len(bot.servers))))
    print('Member count: {}'.format(str(len(set(bot.get_all_members())))))
    print('OAuth URL: {}'.format(oauthlink))
    print('Cogs: {}'.format(bot.cogs))
    print('---------')


if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print('Failed to load extension {}\n{}: {}'.format(extension, type(e).__name__, e))

    loop = asyncio.get_event_loop()

    bot.loop.create_task(background_task(bot))
    bot.run(token)
