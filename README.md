<p align="center"><img src='https://www.shareicon.net/download/2015/11/13/671320_people_512x512.png' width=150 height=100/></p>

# Welcome to the Larabot Repo

Discord server management bot. Genericly made & easily modified.

## Docs

### Configure your API Keys
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

### Support

Buy me a [coffee]()? or [contribute]().
