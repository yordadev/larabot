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
        ## Discord Stuff ##
client                  = discord.Client()
payTheBridgeToll        = configureThe.token()

             ## Commands ##
helpCommand             = configureThe.helpCommand()
anonCommand             = configureThe.anonCommand()
addRoleCommand          = configureThe.addRoleCommand()
removeRoleCommand       = configureThe.removeRoleCommand()
kickCommand             = configureThe.kickCommand()
banCommand              = configureThe.banCommand()
codeCommand             = configureThe.codeCommand()
clearCommand            = configureThe.clearCommand()
searchCommand           = configureThe.searchCommand()
googleResultCount       = configureThe.googleResultCount()
roleInfoCommand         = configureThe.roleInfoCommand()

             ## Channels ##
anonChannel             = configureThe.anonChannel()
roleChannel             = configureThe.roleChannel()
########### Configuration ###########


########### Bot Information ###########
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print(client.get_all_emojis())
    for server in client.servers:
        for channel in server.channels:
            print(channel.id + '\n ' + channel.name)
    print('------')
########### Bot Information ###########



@client.event
async def on_message(message):



########### HELP ###########
    if message.content == helpCommand:
        response = fetchThis.helpThing(message)
        this = await client.send_message(message.channel, embed=response)
        await client.add_reaction(this, '\U0001F44D')
        await client.add_reaction(this, '👎')

    if message.content.startswith(codeCommand):
        response = fetchThis.codeType(message, codeCommand)
        await client.delete_message(message)
        this = await client.send_message(message.channel, response)
        await client.add_reaction(this, '\U0001F44D')
        await client.add_reaction(this, '👎')

########### User Managment ###########
    ##### Role Request Information ####
    if message.content.startswith(roleInfoCommand):
        if roleChannel in message.channel.name:
            response = fetchThis.roleInfo()
            await client.send_message(message.channel, embed=response)


    #### Adding a role ##
    if message.content.startswith(addRoleCommand):
        if roleChannel in message.channel.name:
            for role in message.server.roles:
                if role.name in message.content:
                    if role.name == 'support':
                        await client.send_message(message.channel, 'Sorry, not sorry but.. I couldnt perform this '
                                                                   'command. \n ' + '```' + message.content + '```')
                    else:
                        await client.send_typing(message.channel)
                        await client.add_roles(message.author, role)
                        response = fetchThis.accessAdded(role.name)
                        return await client.send_message(message.author, embed=response)


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




############## Google Stuff ##############
    if searchCommand in message.content:

        from gsearch.googlesearch import search

        query = message.content.split()
        query.remove(searchCommand)
        results = search(str(query))  # returns 10 or less results

        if len(results) > 0:
            await client.send_message(message.channel, 'Thanks for using oogle, here are your results!')

            tmp = []

            for each in results:
                tmp.append('*`' + each[0] + '`* \n<' + each[1] + '>\n\n')

            await client.send_message(message.channel, ''.join(tmp))
        else:
            await client.send_message(message.channel, 'No results found!!! WTF ??')


############## AnonMessages ##############

    if message.content.startswith(anonCommand):
        await client.send_message(message.author, 'What would you like to `Subject:` your confession?')

        subject = await client.wait_for_message(timeout=60.0, author=message.author)

        if subject is None:
            await client.send_message(message.author, '`Sorry` but your confession time `ran out` (`60 Seconds`).\n'
                                                      'Please resubmit your confession and `fill out the subject line`.')
        if subject.author == message.author:
            response = fetchThis.anonMessage(message, anonCommand, subject.content)
            for server in client.servers:
                for channel in server.channels:
                    if anonChannel == channel.name:
                        this = await client.send_message(channel, embed=response)
                        await client.add_reaction(this, '\U0001F44D')
                        await client.add_reaction(this, '😂')
                        await client.add_reaction(this, '❤')
                        await client.add_reaction(this, '💔')
                        await client.add_reaction(this, '👎')



############## Server Management ##############

    #### Kicking users ####
    if message.content.startswith(kickCommand):
        checkAuthority = configureThe.modAuthority(message)
        if checkAuthority is True:
            for user in message.mentions:
                response = fetchThis.kicked(message, user)
                await client.send_message(user, embed=response)
                this = await client.send_message(message.channel, user.name + ' err rip, bye felica. :unamused: ')
                await client.add_reaction(this, '\U0001F44D')
                await client.add_reaction(this, '👎')
                await client.kick(user)

    #### Banning Users ####
    if message.content.startswith(banCommand):
        checkAuthority = configureThe.adminAuthority(message)
        if checkAuthority is True:
            for user in message.mentions:
                response = fetchThis.banned(message, user)
            await client.send_message(user, embed=response)
            this = await client.send_message(message.channel, user.name + ' err rip, bye felica. :unamused: ')
            await client.add_reaction(this, '\U0001F44D')
            await client.add_reaction(this, '👎')
            await client.ban(user)

    #### Clear Messages ####
    if message.content.startswith(clearCommand):
        checkAuthority = configureThe.modAuthority(message)
        if checkAuthority is True:
            numOfMessages = message.content.split()
            numOfMessages.remove(clearCommand)
            numOfMessages = ' '.join(numOfMessages)
            count = 0
            async for msg in client.logs_from(message.channel):
                if count == int(numOfMessages):
                    return await client.send_message(message.channel, 'Alright ' + message.author.mention +
                                                     '. I have removed ' + numOfMessages + ' messages from this channel!')
                else:
                    await client.delete_message(msg)
                    count = count + 1
                    print(count)

    #### Moderator Help ####

client.run(payTheBridgeToll)