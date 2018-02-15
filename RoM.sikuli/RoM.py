from rom_basic import *

import sikuli_tools
reload(sikuli_tools)
from sikuli_tools import *

import datetime

SikuliInterface(
    find = find,findAll = findAll,wait = wait, waitVanish = waitVanish, exists = exists, 
    click = click, doubleClick = doubleClick,rightClick = rightClick, hover = hover,
    dragDrop = dragDrop, type = type, paste = paste  #, Key = Key, KeyModifier = KeyModifier
    )
KeyInterface(Key,KeyModifier)

### SETTINGS
Settings.MinSimilarity = 0.83
Settings.MoveMouseDelay = 0.1
### /SETTINGS

png = png_manifest()
### PARAMETERS - Modify this area to set certain priorities
fzone_trades = [Pattern(png.FZONE_SILVER_TO_GOLD).similar(0.94).targetOffset(9,191)]

### /PARAMETERS



def run_bosses(number_of_tabs,number_of_fights):
    if(number_of_tabs <= 0):
        return
    current_time = lambda : datetime.datetime.now()
    for iteration in xrange(number_of_fights):
        for tab in xrange(number_of_tabs - 1):
            click_best_match("boss/ready_button.png")
            switch_tab_left()
            sleep(1)
        exists("boss/go_button.png",5)
        click_best_match("boss/go_button.png")
        
        for tab in xrange(number_of_tabs):
            reshuffle = Pattern("battle/reshuffle_prompt.png").targetOffset(50,26)
                
            if(exists(reshuffle,10-6*tab)):
                click_best_match(reshuffle)
                waitVanish(reshuffle)
            hover(Location(0,0))
            click_best_match("battle/auto_button.png")
            
            switch_tab_right()
        switch_tab_left()
        hover(Location(0,0))
        
        timing = current_time()
        
        exists("boss/ready_button.png",1000)
        write_to_file("boss times.txt","a",(current_time()-timing).total_seconds())



#SET UP YOUR ROUTINE HERE

#make_fzone_trades(2,fzone_trades)
run_bosses(2,120)

