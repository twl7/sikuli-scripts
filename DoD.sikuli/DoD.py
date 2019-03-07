import dod_basic
reload(dod_basic)
from dod_basic import *

import sikuli_tools
reload(sikuli_tools)
from sikuli_tools import *

### SETTINGS
Settings.MinSimilarity = 0.90
Settings.MoveMouseDelay = 0.05
### /SETTINGS
testing = 0

def test():
    pass

def routine():
    summon_guild_raids()
    dismiss_logoff()
    #collect_guild_campaigns()

try:
    if(testing):
        test()   
    else:
        routine()
except Exception:
    pass