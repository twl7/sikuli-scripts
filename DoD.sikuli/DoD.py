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
    #event no's: 23, 35.39,46    
    shi = False
    if(shi):
        summon_guild_raids(1,22) #shi
        dismiss_logoff()
        hit_new_raids(0)
        dismiss_logoff()
        hit_active_raids(0,3)
        dismiss_logoff()
        loot_raids(2)
        dismiss_logoff()
    else: #twd
        summon_guild_raids(1,34)
        dismiss_logoff()
        hit_new_raids(0)
        dismiss_logoff()
        hit_active_raids(0,4)
        dismiss_logoff()
        loot_raids(2)
        dismiss_logoff()
def test():
    #sri.click_top(png.raid_menu_engage,5)
    #summon_and_hit_raids(10)
    timetime = time.clock()
    #cycle()
      
    #hit_active_raids(0,5)
   
    #hit_new_raids(0) 
    summon_and_hit_raids(55)
    collect_guild_campaigns() 
    hit_new_raids(0)
    dismiss_logoff()
    #loot_raids(300)
    Debug.log(str(time.clock()-timetime))  
    
def routine():
    #hit_new_raids(0)
    #collect_guild_campaigns() 
    six = six_hours = 6*60*60
    x = time.clock()
    ti = 0
    while(time.clock() -x < ti):
            cycle()
    for repeats in xrange(50):
        collect_guild_campaigns() 
        summon_and_hit_raids(65)
        x = time.clock()
        while(time.clock()-x < six_hours):
            cycle()
 
testing = 0
if(testing):
    test()   
else:
    routine()
