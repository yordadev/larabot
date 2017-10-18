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
from Larabot.lib import responses as fetchThis
import discord



########### Configuration ###########

client                  = discord.Client()
payTheBridgeToll        = configureThe.token()
helpCommand             = configureThe.helpCommand()
anonCommand             = configureThe.anonCommand()
anonChannel             = configureThe.anonChannel()
roleChannel             = configureThe.roleChannel()
addRoleCommand          = configureThe.addRoleCommand()
removeRoleCommand       = configureThe.removeRoleCommand()
showRoleCommand         = configureThe.showRoleCommand()
kickCommand             = configureThe.kickCommand()
googleCmd               = configureThe.googleCommand()
googleResultCount       = configureThe.googleResultCount()

########### Configuration ###########



########### Bot Information ###########
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
########### Bot Information ###########



########### Welcome Message ###########
@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await client.send_message(server, fmt.format(member, server))
########### Welcome Message ###########



@client.event
async def on_message(message):
    if message.author == client.user:
        return

########### HELP ###########
    if message.content == helpCommand:
        response = fetchThis.helpThing(message)
        await client.send_message(message.channel, embed=response)

########### User Managment ###########

    #### Adding a role ##
    if message.content.startswith(addRoleCommand):
        if roleChannel in message.channel.name:
            for role in message.server.roles:
                if role.name in message.content:
                    await client.send_typing(message.channel)
                    await client.add_roles(message.author, role)
                    return await client.send_message(message.channel, 'Okay, ' + message.author.name +
                                                     'I have successfully added you to \n ```Role: '
                                                     + role.name + '```')

            await client.send_message(message.channel, 'Sorry, not sorry but.. I couldnt perform this '
                                                       'command. \n ' + '```' + message.content + '```')
     #### Removing a role ##
    if message.content.startswith(removeRoleCommand):
        if roleChannel in message.channel.name:
            for role in message.server.roles:
                if role.name in message.content:
                    await client.send_typing(message.channel)
                    await client.remove_roles(message.author, role)
                    return await client.send_message(message.channel, 'Okay, ' + message.author.name +
                                                     'I have successfully removed you from \n ```Role: '
                                                     + role.name + '```')

            await client.send_message(message.channel, 'Sorry, not sorry but.. I couldnt perform this '
                                                                      'command. \n ' + '```' + message.content + '```')


    ####Displaying the roles ####
    if message.content.startswith(showRoleCommand):
        if roleChannel in message.channel.name:
            await client.send_typing(message.channel)
            return await client.send_message(message.channel, 'Okay, ' + message.author.name +
                                                     ', here you go! \n ```Available Roles: \n'
                                                     'Senior Developer - @mentionable Helper Role \n'
                                                     'Junior Developer - Always Learning```')

    #### Kicking users ####
    if message.content.startswith(kickCommand):
        checkAuthority = configureThe.modAuthority(message)
        if checkAuthority is True:
            for user in message.mentions:
                response = fetchThis.kicked(message, user)
                await client.send_message(user, embed=response)
                await client.send_message(message.channel, user.name + ' err rip, bye felica. :unamused: ')
                await client.kick(user)


############## User Managment ##############
        #### Google Stuff ####
    if googleCmd in message.content:
        from gsearch.googlesearch import search
        query = message.content.split()
        query.remove(googleCmd)
        results = search(str(query))  # returns 10 or less results
        for count in range(0, googleResultCount):
            await client.send_message(message.channel, results[count])

############## AnonMessages ##############

    if message.content.startswith(anonCommand):
        await client.send_message(message.author, 'What would you like to `Subject:` your confession?')

        subject = await client.wait_for_message(timeout=60.0, author=message.author)

        if subject is None:
            await client.send_message(message.author, '`Sorry` but your confession time `ran out` (`60 Seconds`).\n'
                                                      'Please resubmit your confession and `fill out the subject line`.')

        response = fetchThis.anonMessage(message, anonCommand, subject.content)
        for server in client.servers:
            for channel in server.channels:
                if anonChannel == channel.name:
                    return await client.send_message(channel, embed=response)


client.run(payTheBridgeToll)