from loa_basic import *

import sikuli_tools
reload(sikuli_tools)
from sikuli_tools import *

### SETTINGS
Settings.MinSimilarity = 0.83
Settings.MoveMouseDelay = 0.1
### /SETTINGS

def auto_battle():    
    click_best_match(png.battle_auto_fight,90)
    
    click_best_match(png.battle_pass_fight,10)
    fail = png.battle_fail
    if(click_best_match(fail,2)):
        waitVanish(fail,2)
        return 0
    success = png.battle_success
    if(click_best_match(success,2)):
        waitVanish(success,2)
        return 1
    
    
def return_to_main_screen():
    
    for png in ["buttons/close_button_small.png","buttons/close_button.png","buttons/return_button"]:
        click_best_match(png,1)
        
def clear_invasions():
    return_to_main_screen()
    inv_s = png.ADVENTURE_INVASION_SMALL
    inv = png.ADVENTURE_INVASION_LARGE 
    click_best_match(png.MAINSCREEN_ADVENTURE)
    for iter in xrange(15): #number of stages minus 5
        while(exists(inv_s,1)):
            click_best_match(inv_s)
            if(exists(inv,1)):
                if(click_best_match(inv)):
                    auto_battle()
        click_best_match(png.ADVENTURE_SCROLL_LEFT_BUTTON)
    return_to_main_screen()


    


### ROUTINE GOES HERE
click_best_match(png.BUTTONS_CLOSE_BUTTON_SMALL,1)
    