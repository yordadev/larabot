from lib import config as configureThe
from lib import responses as fetchThis
import discord
import asyncio



########### Configuration ###########

client                  = discord.Client()
payTheBridgeToll        = configureThe.token()
roleChannel             = configureThe.roleChannel()
addRoleCommand          = configureThe.addRoleCommand()
removeRoleCommand       = configureThe.removeRoleCommand()
showRoleCommand         = configureThe.showRoleCommand()
kickCommand             = configureThe.kickCommand()
googleCmd               = configureThe.googleCommand()

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

########### User Managment ###########

    # Adding a role #
    if roleChannel in message.channel.name:
        if message.content.startswith(addRoleCommand):
            for role in message.server.roles:
                if role.name in message.content:
                    await client.send_typing(message.channel)
                    await client.add_roles(message.author, role)
                    return await client.send_message(message.channel, 'Okay, ' + message.author.name +
                                                     'I have successfully added you to \n ```Role: '
                                                     + role.name + '```')

            await client.send_message(message.channel, 'Sorry, not sorry but.. I couldnt perform this '
                                                       'command. \n ' + '```' + message.content + '```')
    # Removing a role #
    if roleChannel in message.channel.name:
        if message.content.startswith(removeRoleCommand):
            for role in message.server.roles:
                if role.name in message.content:
                    await client.send_typing(message.channel)
                    await client.remove_roles(message.author, role)
                    return await client.send_message(message.channel, 'Okay, ' + message.author.name +
                                                     'I have successfully removed you from \n ```Role: '
                                                     + role.name + '```')

            await client.send_message(message.channel, 'Sorry, not sorry but.. I couldnt perform this '
                                                                      'command. \n ' + '```' + message.content + '```')


    # Displaying the roles #
    if roleChannel in message.channel.name:
        if message.content.startswith(showRoleCommand):
            await client.send_typing(message.channel)
            return await client.send_message(message.channel, 'Okay, ' + message.author.name +
                                                     'I have successfully removed you from \n ```Available Roles: \n'
                                                     'Guru - Helpers \n'
                                                     'Student - Always Learning```')

    ## Kicking users ##
    checkAuthority = configureThe.modAuthority(message)
    if checkAuthority is True:
        if message.content.startswith(kickCommand):
            for user in message.mentions:
                response = fetchThis.kicked(message, user)
                await client.send_message(user, embed=response)
                await client.send_message(message.channel, user.name + ' err rip, bye felica. :unamused: ')
                await client.kick(user)


########### User Managment ###########
        ## Google Stuff ##
    if googleCmd in message.content:
        from gsearch.googlesearch import search
        query = message.content.split()
        query.remove('g>')
        results = search(str(query))  # returns 10 or less results
        for count in range(0, 5):
            await client.send_message(message.channel, results[count])



client.run(payTheBridgeToll)