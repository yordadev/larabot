## Larabot Configuration File ##

def token():
    token = 'MzY4Mzc2Nzk0NzE5NzE1MzM4.DMggiw.ljQj9j5pYQ8mYudaeQo06LCazGQ'
    return token

def googleKey():
    this = 'AIzaSyCA0fy-aH6QPHp9sWrLd0Ox_PMvsvQf0aM'
    return this

def modAuthority(message):
    approvedRoles = ['support', 'admin']
    for role in message.server.roles:
        for approved in approvedRoles:
            if approved == role.name:
                return True

def roleChannel():
    this = 'role_request'
    return this

def googleCommand():
    this = 'g>'
    return this

def addRoleCommand():
    this = './add'
    return this

def removeRoleCommand():
    this = './remove'
    return this

def showRoleCommand():
    this = './roles'
    return this

def kickCommand():
    this = './kick'
    return this