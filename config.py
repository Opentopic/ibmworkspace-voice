# use local_config.py to overwrite those settings

# username and password for IBM Watson Speech to Text Service
IBM_USERNAME = 'xxx'
IBM_PASSWORD = 'xxx'

# app id and secret to IBM Workspace application
VOICE_APP_ID = 'xxx'
VOICE_APP_SECRET = 'xxx'

# IBM Workspace space id - it's where text is going to be send
WORKSPACE_SPACE_ID = 'xxx'

try:
    from local_config import *
except ImportError:
    pass
