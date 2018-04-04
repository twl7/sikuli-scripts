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
        sri.waitVanish(fail,2)
        return 0
    success = png.battle_success
    if(sri.click_best_match(success,2)):
        sri.waitVanish(success,2)
        return 1    


activity_orders = {#png.activity_chest1_ready:[],
                   #png.activity_explore_map:[png.adventure_star],
                   png.activity_open_starter_pack:[png.store_starter_pack_tab_unselected, png.store_buy_pack, png.store_skip],
                   # png.activity_enchant_card: [],
                   png.activity_meditate_once: [png.temple_meditate, png.temple_quick_process],
                   png.activity_send_energy_once: [png.friends_send, png.buttons_notification_close]
                   #png.activity_join_free_match: [png.icon_magic_chip_small, png.arena_fight, auto_battle] 
                }

def complete_activity():
    def return_to_activity():
        return_to_main_screen()
        sri.click(png.mainscreen_activity,5,last_match = True)
        sri.wait(png.activity_send_energy_once,30)
        
    go_to = png.activity_go_to_button

    return_to_activity()
    for activity in activity_orders:
        
        search_space = None
        try:
            search_space = sri.find(activity).right()
        except:
            continue
        
        if(sri.exists(go_to,2,search_space)):
            sri.click(go_to,2,search_space,True)            
            for target in activity_orders[activity]:
                
                if(isinstance(target,type(callable))):
                    target()
                else:
                    sleep(3)
                    sri.click(target,10)
            return_to_activity()
    return_to_main_screen()
    
        
def clear_invasions():
    return_to_main_screen()
    inv_s = png.ADVENTURE_INVASION_SMALL
    inv = png.ADVENTURE_INVASION_LARGE 
    sri.click(png.MAINSCREEN_ADVENTURE,10,last_match = True)
    sri.wait(png.ADVENTURE_SCROLL_LEFT_BUTTON,30)
    
    for iteration in xrange(15): #number of stages minus 5
        while(sri.exists(inv_s,1)):
            sri.click_best_match(inv_s)
            if(sri.exists(inv,1)):
                if(sri.click_best_match(inv)):
                    auto_battle()
        sri.click(png.ADVENTURE_SCROLL_LEFT_BUTTON,last_match = True)
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
    sri.click(png.mainscreen_honor,10,last_match = True)
    for i in xrange(7):
        sri.click(png.honor_worship,5)
    return_to_main_screen()

def clear_dungeon():
    arr = [png.mainscreen_arena,png.arena_dungeon,png.arena_dungeon_sweep,png.buttons_return_button,png.arena_dungeon,png.arena_dungeon_continue]
    s = sum([sri.click_best_match(image,5) for image in arr])
    
    continue_fight = 1
    fight_button = Pattern(png.arena_dungeon_fight).similar(0.8)
    while(continue_fight == 1):
        sri.exists(fight_button,10)
        while(sri.click_best_match(fight_button,1)):
            if(sri.exists(png.arena_dungeon_recharge,1)):
                continue_fight = 0
                break
    
        continue_fight = continue_fight and auto_battle()
                

    return_to_main_screen()
 

def claim_friends_energy():
    sri.click_best_match("")
    return_to_main_screen()

def reset_towers(towers_to_reset):
    return_to_main_screen()
    sri.click(png.MAINSCREEN_ADVENTURE,last_match = True)
    sri.wait(png.ADVENTURE_SCROLL_LEFT_BUTTON,30)
    
    for i in range(8,2,-1):
        to_clear = Pattern(getattr(png, "adventure_map" + str(i))).similar(0.95)
           
        while(not sri.exists(to_clear,1)):
            sri.click(png.ADVENTURE_SCROLL_LEFT_BUTTON,last_match=True)
        for target in [to_clear, png.adventure_tower_icon,
                      png.tower_free_reset, png.tower_confirm_button,
                      png.tower_reset,png.buttons_close_button_small,
                      png.tower_return_button]:
            sri.click(target,3,last_match=True)
            
    return_to_main_screen()

def clear_maze():
    pass

def clear_towers(towers_to_clear):
    return_to_main_screen()
    sri.click_best_match(png.MAINSCREEN_ADVENTURE)
    sri.wait(png.ADVENTURE_SCROLL_LEFT_BUTTON,30)
    
    for iteration in xrange(15): 
        pass
        sri.click_best_match(png.ADVENTURE_SCROLL_LEFT_BUTTON)
    return_to_main_screen()
