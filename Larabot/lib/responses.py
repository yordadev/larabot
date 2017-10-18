import discord

def kicked(message, user):
    embed = discord.Embed(title=message.server.name + " :: Notification", url='https://discord.gg/Ec6ArRf',
                          description="You have been kicked from message.server.name")
    embed.set_author(name="Larabot", url='https://github.com/Devitgg/larabot',
                     icon_url='https://png.icons8.com/wired/1600/D32F2F/source-code')
    embed.set_thumbnail(url='https://www.shareicon.net/download/2015/11/13/671320_people_512x512.png')
    embed.add_field(name="Server Invite Code", value='Ec6ArRf', inline=False)
    embed.set_footer(text=user.name + " your welcome to join back at as long as you follow our rules.")
    return embed