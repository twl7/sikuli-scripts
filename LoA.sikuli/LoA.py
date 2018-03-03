from loa_basic import *

import sikuli_tools
reload(sikuli_tools)
from sikuli_tools import *

### SETTINGS
Settings.MinSimilarity = 0.75
Settings.MoveMouseDelay = 0.15
Settings.OcrTextSearch = True
Settings.OcrTextRead = True
### /SETTINGS

### PARAMETERS
towers = range(2,9)
###
### SET UP YOUR ROUTINE HERE

def routine():
    return_to_main_screen()
    complete_honor()
    #complete_events()
    complete_activity()
    clear_invasions()
    fight_dungeon()
    
windows = 2   
for i in xrange(windows):
    for image in [png.container_other_server,png.container_new_server]:
        pattern = Pattern(image).similar(0.7)
        while(not sri.click_best_match(Pattern(png.container_select_server).similar(0.60),3)):
            pass
        sri.click_best_match(pattern,20)
        #type("r",KeyModifier.CTRL)
        sleep(20)
        routine()
    type(Key.TAB,KeyModifier.ALT)
