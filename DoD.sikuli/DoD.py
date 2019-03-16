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


def cycle():
    summon_guild_raids(40)
    dismiss_logoff()
    hit_new_raids(0)
    dismiss_logoff()
    hit_active_raids(0,10)
    dismiss_logoff()
    loot_raids(10)
    dismiss_logoff()
    
def test():
    #sri.click_top(png.raid_menu_engage,5)
    #summon_and_hit_raids(35)
    timetime = time.clock()
    #cycle()
    Debug.log(str(time.clock()-timetime))    
    #hit_active_raids(0,5)
    #hit_new_raids(0)
    collect_guild_campaigns() 
    
def routine():
    #hit_new_raids(0)
    #collect_guild_campaigns() 
    for i in xrange(55):
            cycle()
    for repeats in xrange(5):
        summon_and_hit_raids(45)
        for i in xrange(59):
            cycle()
            
testing = 0
if(testing):
    test()   
else:
    routine()
