from rom_basic import *

import sikuli_tools
reload(sikuli_tools)
from sikuli_tools import *

### SETTINGS
Settings.MinSimilarity = 0.78
Settings.MoveMouseDelay = 0.05
### /SETTINGS


### PARAMETERS - Modify this area to set certain priorities
epic_trades = [ png.fzone_energy_to_epic,
                png.fzone_magic_to_epic,
                png.fzone_soul_to_epic]
gold_trades =  [png.fzone_good_to_gold,
                png.fzone_rare_to_gold,
                png.fzone_epic_to_gold,
                png.FZONE_SILVER_TO_GOLD]
#silver_trades = [png.fzone_elixir_to_silver]
fzone_trades = epic_trades+gold_trades
### /PARAMETERS

#SET UP YOUR ROUTINE HERE


#run_bosses(1,22)
#sri.switch_tab_right()
#run_bosses(2,24)
#sri.switch_tab_right()
run_bosses(1,400)
#run_world_boss(2,40)
def fz_boss():
    for i in xrange(10):
        run_bosses(2,16)
        make_fzone_trades(1,gold_trades,1,1)    
#fz_boss()
#make_fzone_trades(3,fzone_trades,1000)  