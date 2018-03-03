from rom_basic import *

import sikuli_tools
reload(sikuli_tools)
from sikuli_tools import *

### SETTINGS
Settings.MinSimilarity = 0.83
Settings.MoveMouseDelay = 0.05
### /SETTINGS


### PARAMETERS - Modify this area to set certain priorities
fzone_trades = [png.fzone_energy_to_epic,
                png.fzone_magic_to_epic,
                png.fzone_soul_to_epic,
                png.fzone_good_to_gold,
                #png.fzone_rare_to_gold,
                #png.fzone_epic_to_gold,
                png.FZONE_SILVER_TO_GOLD]
### /PARAMETERS

#SET UP YOUR ROUTINE HERE

sleep(0.5)
make_fzone_trades(3,fzone_trades)
#run_bosses(1,14)
#run_bosses(2,200)
#run_world_boss(2,40)
