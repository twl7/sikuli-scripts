import os,sys
parent = os.path.dirname(sys.path[0])
if(not parent in sys.path): sys.path.append(parent)

from org.sikuli.basics import Debug
from org.sikuli.script import *
from sikuli_tools import *
from time import *

sri = SRI()
png = png_manifest(sys.path[0])


def return_to_main_screen():
    small = png.buttons_close_button_small
    large = png.buttons_close_button
    ret = png.buttons_return_button
    cont = True
    while(cont):
        cont = False
        for image in [small,large,ret]:
            if(sri.click_best_match(image,1)):
                cont = True
                

def auto_battle():    
    clicked = sri.click_best_match(png.battle_auto_fight,90)
    if(clicked == 0):
        return -1
    sri.click_best_match(png.battle_pass_fight,10)
    fail = png.battle_fail_menu
    if(sri.click_best_match(fail,2)):
        sri.region.waitVanish(fail,2)
        return 0
    success = png.battle_success
    if(sri.click_best_match(success,2)):
        sri.region.waitVanish(success,2)
        return 1    


activity_orders = {#png.activity_explore_map:[png.adventure_star],
                   png.activity_open_starter_pack:[png.store_starter_pack_tab_unselected, png.store_buy_pack, png.store_skip],
                   # png.activity_enchant_card: [],
                   png.activity_meditate_once: [png.temple_meditate, png.temple_quick_process],
                   png.activity_send_energy_once: [png.friends_send, png.buttons_notification_close]
                   #png.activity_join_free_match: [png.icon_magic_chip_small, png.arena_fight, auto_battle] 
                }

def complete_activity():
    def return_to_activity():
        return_to_main_screen()
        sri.click_best_match(png.mainscreen_activity,5)
        sri.region.wait(png.activity_explore_map,30)
        
    go_to = png.activity_go_to_button

    return_to_activity()
    for activity in activity_orders:
        
        search_space = None
        try:
            search_space = sri.region.find(activity).right()
        except:
            continue
        
        if(search_space.exists(go_to)):
            search_space.click(go_to)            
            for target in activity_orders[activity]:
                
                if(isinstance(target,type(callable))):
                    target()
                else:
                    sleep(3)
                    sri.click_best_match(target,10)
            return_to_activity()
    return_to_main_screen()
    
        
def clear_invasions():
    return_to_main_screen()
    inv_s = png.ADVENTURE_INVASION_SMALL
    inv = png.ADVENTURE_INVASION_LARGE 
    sri.click_best_match(png.MAINSCREEN_ADVENTURE)
    sri.region.wait(png.ADVENTURE_SCROLL_LEFT_BUTTON,30)
    
    for iter in xrange(15): #number of stages minus 5
        while(sri.region.exists(inv_s,1)):
            sri.click_best_match(inv_s)
            if(sri.region.exists(inv,1)):
                if(sri.click_best_match(inv)):
                    auto_battle()
        sri.click_best_match(png.ADVENTURE_SCROLL_LEFT_BUTTON)
    return_to_main_screen()

def complete_events():
    return_to_main_screen()
    if(sri.click_best_match(png.event_raider)):
        sri.click_best_match(png.event_raider_friend_contribution,60)
        while(sri.click_best_match(png.event_raider_claim,10)):
            pass
        return_to_main_screen()
    
def complete_honor():
    return_to_main_screen()
    sri.click_best_match(png.mainscreen_honor,10)
    for i in xrange(7):
        sri.click_best_match(png.honor_worship,5)
    return_to_main_screen()

def fight_dungeon():
    arr = [png.mainscreen_arena,png.arena_dungeon,png.arena_dungeon_sweep,png.buttons_return_button,png.arena_dungeon,png.arena_dungeon_continue]
    s = sum([sri.click_best_match(image,5) for image in arr])
    
    continue_fight = 1
    fight_button = Pattern(png.arena_dungeon_fight).similar(0.8)
    while(continue_fight == 1):
        sleep(5)
        while(sri.click_best_match(fight_button,1)):
            if(sri.region.exists(png.arena_dungeon_recharge,5)):
                continue_fight = 0
                break
    
        continue_fight = continue_fight and auto_battle()
                

    return_to_main_screen()
 

def claim_friends_energy():
    sri.click_best_match("d")
    return_to_main_screen()

def reset_mazes():
    pass


def clear_maze():
    pass
