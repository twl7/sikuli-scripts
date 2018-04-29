#"energy_to_epic.png""soul_to_epic.png""magic_to_epic.png""good_to_gold.png"
from rom_basic import *

import sikuli_tools
reload(sikuli_tools)
from sikuli_tools import *

### SETTINGS
Settings.MinSimilarity = 0.90
Settings.MoveMouseDelay = 0.05
### /SETTINGS


### PARAMETERS - Modify this area to set certain priorities
epic_trades = [ png.fzone_energy_to_epic,
                png.fzone_magic_to_epic,
                png.fzone_soul_to_epic]
pre_2K_trades = epic_trades + [png.fzone_good_to_gold]

gold_trades =  [png.fzone_good_to_gold,
                png.fzone_rare_to_gold,
                png.fzone_epic_to_gold,
                png.FZONE_SILVER_TO_GOLD]
#silver_trades = [png.fzone_elixir_to_silver]
fzone_trades = pre_2K_trades + [png.FZONE_SILVER_TO_GOLD]
### /PARAMETERS

#SET UP YOUR ROUTINE HERE

def fz_boss():
    for i in xrange(100):
        run_bosses(2,14)
        make_fzone_trades(3,fzone_trades,1,1)    
#sleep(10800)
tab_bosses(time=72000)
#run_bosses(2,800)
#run_bosses(1,400)
#run_world_boss(2,50)
#fz_boss()
#auto_towers(20)
#make_fzone_trades(3,fzone_trades,-1,1000)  