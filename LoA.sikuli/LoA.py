from loa_basic import *

import sikuli_tools
reload(sikuli_tools)
from sikuli_tools import *

### SETTINGS
Settings.MinSimilarity = 0.78
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
    clear_invasions()
    clear_dungeon()
    complete_activity()
#return_to_main_screen()
 
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
        sri.exists(png.mainscreen_adventure,20)
        routine()
    
    type(Key.TAB,KeyModifier.ALT)
    sleep(3)
