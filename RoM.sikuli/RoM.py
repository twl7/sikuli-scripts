from rom_basic import *

import sikuli_tools
reload(sikuli_tools)
from sikuli_tools import *

### SETTINGS
Settings.MinSimilarity = 0.83
Settings.MoveMouseDelay = 0.05
### /SETTINGS


### PARAMETERS - Modify this area to set certain priorities
fzone_trades = [Pattern(png.FZONE_SILVER_TO_GOLD).similar(0.94).targetOffset(9,191)]

### /PARAMETERS

#SET UP YOUR ROUTINE HERE

#make_fzone_trades(2,fzone_trades)
run_bosses(2,200)

