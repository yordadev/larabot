####################################################################################
# Larabot Discord Bot
# MIT License
# Copyright (c) 2017 Devitgg
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
####################################################################################
from Larabot.lib import config as configureThe
import discord

########### Configuration ###########
anonCommand             = configureThe.anonCommand()
showRoleCommand         = configureThe.showRoleCommand()
searchCommand           = configureThe.searchCommand()
codeCommand             = configureThe.codeCommand()
googleResultCount       = configureThe.googleResultCount()
plusRepCommand          = configureThe.plusRepCommand()
viewRepCommand          = configureThe.viewRepCommand()

########### Configuration ###########

########### Responses ###########
def kicked(message, user):
    embed = discord.Embed(title=message.server.name + " :: Notification", url='https://github.com/Devitgg/larabot',
                          description="You have been kicked from message.server.name")
    embed.set_author(name="Larabot", url='https://github.com/Devitgg/larabot',
                     icon_url='https://png.icons8.com/wired/1600/D32F2F/source-code')
    embed.set_thumbnail(url='https://www.shareicon.net/download/2015/11/13/671320_people_512x512.png')
    embed.add_field(name="Server Invite Code", value='Ec6ArRf', inline=False)
    embed.set_footer(text=user.name + " your welcome to join back at as long as you follow our rules.")
    return embed

def helpThing(message):
    embed = discord.Embed(title=message.server.name + " :: Notification", url='https://discord.gg/Ec6ArRf',
                          description="Here are all available commands you have access too!")
    embed.set_author(name="Larabot", url='https://github.com/Devitgg/larabot',
                     icon_url='https://png.icons8.com/wired/1600/D32F2F/source-code')
    embed.set_thumbnail(url='https://www.shareicon.net/download/2015/11/13/671320_people_512x512.png')
    embed.add_field(name='Command: ' + codeCommand, value='Easily show syntax highlighting for specific languages \n'
                                                                                   'Example: ```> php \n<code here>```', inline=False)
    embed.add_field(name='Command: ' + searchCommand, value='Just google it and displays top ' + str(googleResultCount)
                                                            + ' Results. \n `' + searchCommand + ' how do i google this?`', inline=False)
    embed.add_field(name='Command: ' + anonCommand, value='Private message Larabot directly with \n `' + anonCommand + ' <a confession>`', inline=False)
    embed.add_field(name='Command: ' + plusRepCommand, value='Helped by someone? Plus rep them! \n'
                                                             '`' + plusRepCommand + ' @DΞVITGG#4809`', inline=False)
    embed.add_field(name='Command: ' + viewRepCommand, value='Check out a users rep! \n'
                                                             '`' + viewRepCommand + ' @DΞVITGG#4809`', inline=False)
    embed.add_field(name='Abusing Rep', value='Abusing Rep or purposely trolling someone by @mention them will result in a kick', inline=False)
    embed.set_footer(text="Created with <3 by Devitgg")
    return embed

def anonMessage(message, anonCommand, subject):
    theMessage = message.content.split()
    theMessage.remove(anonCommand)
    theMessage = ' '.join(theMessage)

    embed = discord.Embed(title="Fuck my life :: Confessions of a Developer", url='https://discord.gg/Ec6ArRf',
                          description='Subject: ' + subject)
    embed.set_author(name="Larabot", url='https://github.com/Devitgg/larabot',
                     icon_url='https://png.icons8.com/wired/1600/D32F2F/source-code')
    embed.set_thumbnail(url='https://www.shareicon.net/download/2015/11/13/671320_people_512x512.png')
    embed.add_field(name='The Confession', value='```' + theMessage + '```', inline=False)
    embed.set_footer(text="Created with <3 by Devitgg")
    return embed

def codeType(message, codeCommand):
    codeTypes = ['css', 'html', 'python', 'php', 'javascript', 'java']
    for code in codeTypes:
        if code in message.content:
            return 'Here you go' + message.author.mention + '\n```' + code + '\n' + message.content + '```'

    return 'Fix your formatting please! Its `> <coding language> <code>` .. Very simple ' + message.author.mention + '..'


def accessServer():
    embed = discord.Embed(title="JustDev[it] :: Welcome Message",  description='Please read & understand our rules.\n'
                                                                               'Add a role to gain access to '
                                                                               'our server.\n\n')
    embed.set_author(name="Larabot", url='https://github.com/Devitgg/larabot',
                     icon_url='https://png.icons8.com/wired/1600/D32F2F/source-code')
    embed.set_thumbnail(url='https://www.shareicon.net/download/2015/11/13/671320_people_512x512.png')
    embed.add_field(name='Available Roles', value='`junior dev` -  Still learning \n'
                                                  '`senior dev` -  Guru', inline=False)
    embed.add_field(name='How to add a role', value='Type the following: \n'
                                                    '`add> <role>` \n \n'
                                                    'example: \n'
                                                    '`add> junior dev`', inline=False)
    embed.set_footer(text="Created with <3 by Devitgg")
    return embed


def accessAdded(role):
    embed = discord.Embed(title="JustDev[it] :: Access Granted",  description='You have been given access to JustDev[it].')
    embed.set_author(name="Larabot", url='https://github.com/Devitgg/larabot',
                     icon_url='https://png.icons8.com/wired/1600/D32F2F/source-code')
    embed.set_thumbnail(url='https://www.shareicon.net/download/2015/11/13/671320_people_512x512.png')
    embed.add_field(name='Role Added', value='You have been added to ' + role + '. \n Enjoy your stay!', inline=False)
    embed.set_footer(text="Created with <3 by Devitgg")
    return embed
########### Responses ###########