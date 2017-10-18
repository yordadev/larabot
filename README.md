<p align="center"><img src='https://www.shareicon.net/download/2015/11/13/671320_people_512x512.png' width=150 height=100/></p>

# About Larabot

Discord server management bot. Build for myself but Genericly made & easily modified.

> Note - I am still developing this, this is a fresh project.

## Larabot Documentation

### Installing Larabot

Install the necessary dependencies

```
pip install discordpy
pip install gsearch
```

## Requirements

- Python 3.4.2+
- `aiohttp` library
- `websockets` library
- `PyNaCl` library (optional, for voice only)
    - On Linux systems this requires the `libffi` library. You can install in
      debian based systems by doing `sudo apt-get install libffi-dev`.

Usually `pip` will handle these for you.


### Setting up Larabot
Get your Discord Token and Google Custom Search API Key & place in `<insert key here>`

```python 
from lib import config as configureThe

def token():
    token = '<insert key here>'
    return token

def googleKey():
    this = '<insert key here>'
    return this
```

Add what current roles on your server can access `admin` capabilities.

```python
def modAuthority(message):
    approvedRoles = ['<add role name>', '<add role name>']
    for role in message.server.roles:
        for approved in approvedRoles:
            if approved == role.name:
                return True
```

### Configure your commands

- Setup what you want your channel to be to manage roles, the bot will only listen in that channel. 
- Setup your commands for server management

```Python
def roleChannel():
    this = '<set this up>'
    return this

def googleCommand():
    this = '<set this up>'
    return this

def addRoleCommand():
    this = '<set this up>'
    return this

def removeRoleCommand():
    this = '<set this up>'
    return this

def showRoleCommand():
    this = '<set this up>'
    return this

def kickCommand():
    this = '<set this up>'
    return this
```
### Useage

Use bot in discord by:

```markup
<addRoleCommand> [role_name]
<removeRoleCommand> [role_name]
<showRoleCommand>
<kickCommand> @mention
```

>Note - When kicking, you can select multiple people to kick at once by `<kickCommand> @mention @mention @mention>`

### Features Coming
- Googling Memes and returning meme Img
- Banning
- Create Roles
- Games

### Support

Buy me a [coffee](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=FN4Q4KATUUU76)? or [contribute](https://github.com/Devitgg/larabot/pulls).
