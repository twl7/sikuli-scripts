from loa_basic import *

import sikuli_tools
reload(sikuli_tools)
from sikuli_tools import *

SikuliInterface(
    find = find,findAll = findAll,wait = wait, waitVanish = waitVanish, exists = exists, 
    click = click, doubleClick = doubleClick,rightClick = rightClick, hover = hover,
    dragDrop = dragDrop, type = type, paste = paste
    )
KeyInterface(Key,KeyModifier)

### SETTINGS
Settings.MinSimilarity = 0.83
Settings.MoveMouseDelay = 0.3
### /SETTINGS

def auto_battle():    
    click_best_match("battle/auto_fight.png",100)
    
    click_best_match("battle/pass_fight.png",10)
    if(click_best_match("battle/fail.png",2)):
        waitVanish("battle/fail.png",2)
    if(click_best_match("battle/success.png",2)):
        waitVanish("battle/success.png",2)
    
    
def return_to_main_screen():
    for i in xrange(3):
        for png in ["buttons/close_button_small.png","buttons/close_button.png","buttons/return_button"]:
            click_best_match(png)
        
def clear_invasions():
    return_to_main_screen()
    click_best_match("mainscreen/adventure.png")
    for iter in xrange(15): #number of stages minus 5
        while(exists("adventure/invasion_small.png",1)):
            click_best_match("adventure/invasion_small.png")
            if(exists("adventure/invasion_large.png",1)):
                if(click_best_match("adventure/invasion_large.png")):
                    auto_battle()
        click_best_match("adventure/scroll_left_button.png")
    return_to_main_screen()


def buy_starter_pack():
    pass
def get_honor():
    click_all()
    

def fight_dungeon():
    pass

### ROUTINE GOES HERE

clear_invasions()
    