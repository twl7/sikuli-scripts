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
def claim_gift():
    return_to_main_screen()
    sri.click(png.mainscreen_gift,5)
    sri.click(png.buttons_gift_claim,5)
    return_to_main_screen()
    
def routine():
    return_to_main_screen()
    
    clear_dungeon()
    return_to_main_screen()
    
    clear_invasions()
    
    return_to_main_screen()
    complete_honor()
    complete_activity()
    
    complete_events()
    claim_gift()
    
#return_to_main_screen()
#use_temple(800)
windows = 2
last_login = Pattern(png.container_server_last_login).similar(0.95)

sleep_action_list = [[0,routine],[300,claim_gift],[600,claim_gift],[1200,claim_gift],[1800,claim_gift],[1800,claim_gift]]   
for [sleep_time,the_action] in sleep_action_list[:0]:
    sleep(sleep_time)
    for i in xrange(windows):
        for image in [png.container_server_kong_kings_landing,png.container_server_kong_winterfell][::-1]:
            pattern = Pattern(image).similar(0.80)
            
            while(not sri.click_best_match(Pattern(png.container_select_server).similar(0.60),10)):
                pass
            if(not sri.click_best_match(pattern,10)):
                sri.click_best_match(last_login,10)
            #type("r",KeyModifier.CTRL)
            sri.exists(png.mainscreen_adventure,20)
            the_action()
        if(i < windows-1):
            type(Key.TAB,KeyModifier.ALT)
        sleep(3)
routine()
def next_tab():
    type(Key.TAB,KeyModifier.CTRL)
    sleep(10)
    routine()
def next_window():
    type(Key.TAB,KeyModifier.ALT)
    sleep(10)
    routine()
next_window()