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

gold_trades =  [
                png.fzone_good_to_gold,
                png.fzone_rare_to_gold,
                png.fzone_epic_to_gold,
                #png.fzone_legendary_to_gold,
                png.FZONE_SILVER_TO_GOLD
                ]
#silver_trades = [png.fzone_elixir_to_silver]
fzone_trades = pre_2K_trades + [png.FZONE_SILVER_TO_GOLD] + gold_trades
### /PARAMETERS



def fz_boss(tabs = 2):
    for i in xrange(100):
        run_bosses(tabs,14)
        make_fzone_trades(5,fzone_trades,1,1,separate_trades=False)  

def fz_boss_tab():
    for run_time in [2800] + [2800] * 200:
        tab_bosses(run_time)
        for j in xrange(5):
            sleep(1)
            auto_battle(0)
            sri.switch_tab_right()
        sleep(240)
        make_fzone_trades(5,fzone_trades,1,1,separate_trades=False)  
        
def towers(x):  
    auto_towers(x)
    sleep(200)
    for i in xrange(5):
        sri.click(png.battle_victory,7)
        sri.switch_tab_right()


###   SET UP YOUR ROUTINE HERE

#run_world_boss(2,100)    
#run_bosses(2,31)
tab_bosses(run_time=70000)


#towers(180)
#fz_boss(2)  
#fz_boss_tab()
rush = fzone_trades + [png.fzone_rare_to_gold]
go = gold_trades
fz = fzone_trades
curr_array = [rush]*0 + [fz+go]*4 + [go]*0 #[go,go,go,go]
#make_fzone_trades(4, curr_array,1000,wait_time= 1000,separate_trades= True)  
#make_fzone_trades(4,gold_trades,-1,wait_time= 1000,separate_trades= False) 