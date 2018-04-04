from loa_basic import *

import sikuli_tools
reload(sikuli_tools)
from sikuli_tools import *

### SETTINGS
Settings.MinSimilarity = 0.80
Settings.MoveMouseDelay = 0.15
Settings.OcrTextSearch = True
Settings.OcrTextRead = True
### /SETTINGS

### PARAMETERS
towers = range(8,1,-1)
###

### SET UP YOUR ROUTINE HERE

def routine():
    return_to_main_screen()
    complete_honor()
    #complete_events()
    complete_activity()
    clear_invasions()
    clear_dungeon()

    
windows = 2
last_login = Pattern(png.container_server_last_login).similar(0.95)
for i in xrange(windows):
    for image in [png.container_server_kong_kings_landing,png.container_server_kong_winterfell]:
        pattern = Pattern(image).similar(0.95)
        
        while(not sri.click_best_match(Pattern(png.container_select_server).similar(0.60),3)):
            pass
        if(not sri.click_best_match(pattern,10)):
            sri.click_best_match(last_login,10)
        #type("r",KeyModifier.CTRL)
        sleep(30)
        routine()
    type(Key.TAB,KeyModifier.ALT)
