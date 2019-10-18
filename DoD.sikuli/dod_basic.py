import os, sys
parent_directory = os.path.dirname(sys.path[0])

if(not parent_directory in sys.path): sys.path.append(parent_directory)

from org.sikuli.basics import Debug
from org.sikuli.script import *
from sikuli_tools import *

import time
import datetime


sri = SRI()
png = png_manifest(sys.path[0])

# helper
damage_stamina = [png.raid_battlescreen_s_1, png.raid_battlescreen_s_5, 
              png.raid_battlescreen_s_20, png.raid_battlescreen_s_20x5]

#damage_energy = [png.raid_battlescreen_e_1, png.raid_battlescreen_e_5, 
#              png.raid_battlescreen_e_20, png.raid_battlescreen_e_20x5]

damage_honor = [png.raid_battlescreen_h_1, png.raid_battlescreen_h_5, 
              png.raid_battlescreen_h_20, png.raid_battlescreen_h_20x5]


### GUILD
def summon_guild_raids(limit, skip = 0):
    limit = max(limit, 1)
    dismiss_mod = 10
    d_t = 5
    for pic in [png.mainscreen_tab_guild, png.guild_war_room]:
        sri.click(pic, 5)
    for pic in [png.guild_war_room_join_all, png.popup_choice_yes]:
        sri.click(pic, d_t)
    scroll_down = sri.find(Pattern(png.guild_war_room_scroll_bottom).similar(0.98))
    summon = Pattern(png.guild_war_room_summon).similar(0.80)
    hov = sri.find(png.mainscreen_tab_guild_selected, d_t)
    for i in xrange(skip):
        sri.click(scroll_down)
        sri.hover(hov)
        time.sleep(0.2)
    for i in xrange(limit):
        if((i+1)%dismiss_mod == 0):
            dismiss_logoff()
        sri.click_top(summon,d_t)
        sri.click(png.popup_ok_confirm)
        #sri.click_all(summon, wait_between = 0.1)
        sri.click(scroll_down)
        sri.hover(hov)
        time.sleep(0.2)
    for pic in [png.guild_war_room_join_all, png.popup_choice_yes]:
        sri.click(pic, d_t)
    sri.click(png.mainscreen_tab_home)
        
def collect_guild_campaigns():
    default_time = d_t = 6
    completed = Pattern(png.guild_campaign_menu_tab_completed).similar(0.98)
    gtabselect = png.mainscreen_tab_guild_selected
    hov = sri.find(png.mainscreen_tab_guild) or Location(0,0)
    for pic in [png.mainscreen_tab_guild, png.guild_campaign, completed]:
        sri.click(pic, timeout = d_t )

    
    while(sri.exists(png.guild_campaign_menu_join, d_t)):

        ##collect
        ##count = 0
        ##for jo in sri.find_all(png.guild_campaign_menu_join):
        ##  count += 1
        time.sleep(1)
        sri.click_top(png.guild_campaign_menu_join)
        sri.click(png.guild_campaign_map_close_result, d_t)
        sri.click(png.guild_campaign_map_close_result, 2)
        while(sri.exists(png.guild_campaign_map_node_collect, d_t)):
            for pic in [png.guild_campaign_map_node_collect, \
                        png.guild_campaign_map_node_loot] + [gtabselect]*4:
                sri.click(pic, d_t)
                sri.hover(hov)
        for pic in [png.guild_campaign_map_close, png.guild_campaign, completed]:
            sri.click(pic, d_t)
        time.sleep(1)

        #loot
        #for i in xrange(count):
        for pic in [png.guild_campaign_menu_loot, png.popup_ok_confirm] + [gtabselect]*4:
            sri.click(pic, d_t)
        #end while menu join
    sri.click(png.mainscreen_tab_home)
    return True
    

### RAIDS

def load_raid_information():
    pass
"""
Call in raid_menu
"""
def join_raid(engage_only = False):
    d_t = 2
    def check_popup():
        return sri.click(png.popup_ok_confirm, timeout = 1)
    
    for pic in [png.raid_menu_join]*(1-engage_only) + [png.raid_menu_engage]:
        sri.click_top(pic, timeout = d_t)
        if(check_popup()):
            return False
    
    return True

"""
Called in raid battle screen
"""
def hit_raid(damage_index = 0, share = False):
    d_t = 5
    #arr = [damage_stamina, damage_honor, damage_energy]
    sri.click(damage_honor[damage_index], d_t)
    if(sri.click(png.popup_ok_confirm, 1)):
        time.sleep(0.5)
        return
    if(share == True):
        for pic in [png.raid_battlescreen_share, 
                    png.raid_battlescreen_share_public]:
            sri.click(pic, d_t)
        
        sri.click(png.popup_ok_confirm, 1) or sri.click(png.popup_close, 1)
    sri.click(png.raid_battlescreen_close, d_t)
    
def join_and_hit_raid(damage_index = 0, share = False):
    join_raid()
    hit_raid(damage_index, share)

#call from home tab
def summon_and_hit_raids(num_to_summon):
    d_t = 7
    dismiss_mod = 8
    hov = sri.find(png.mainscreen_tab_raid) or \
          sri.find(png.mainscreen_tab_raid_selected)
    for pic in [png.mainscreen_tab_raid, png.raid_menu_refresh]:
        sri.click(pic, d_t)
        
    time.sleep(2)
    summon = Pattern(png.raid_tab_summon).similar(0.95)
    for pic in [png.raid_tab_summon, png.raid_menu_available_summon]:
        sri.click(pic,d_t)
    for index in xrange(num_to_summon):
        if(sri.click_top(png.raid_menu_summon, d_t)):
            sri.hover(hov)
            sri.click(png.raid_menu_engage_summon, d_t)
            hit_raid(0, True)
        sri.click(png.raid_menu_refresh,d_t)
        if((index+1)%dismiss_mod == 0):
            dismiss_logoff()
    sri.click(png.mainscreen_tab_home,d_t)

def hit_new_raids(damage_index):
    d_t = 5
    dismiss_mod = 10
    sri.click(png.mainscreen_tab_raid, d_t)
    i = 0
    while(sri.click(png.raid_menu_engage, d_t)):
        hit_raid(damage_index, False)
        i+=1
        if(i % dismiss_mod == 0):
            dismiss_logoff()

    sri.click(png.mainscreen_tab_home,d_t)

def hit_active_raids(damage_index, num_times):
    d_t = 5
    
    sri.click(png.mainscreen_tab_raid, d_t)
    time.sleep(4)
    sri.click(png.raid_tab_active, d_t)
    for i in xrange(num_times):
        join_raid(engage_only = True)
        hit_raid(damage_index, False)

    sri.click(png.mainscreen_tab_home,d_t)

def loot_raids(num_times):
    d_t = 5
    sri.click(png.mainscreen_tab_raid,d_t)
    time.sleep(4)
    sri.click(png.raid_tab_completed, d_t)
    sri.click(png.raid_menu_close_unhit,d_t)
    location = sri.find(png.raid_menu_loot,d_t)
    if(location == None):
        return
    for i in xrange(2*num_times):
        sri.click(location)
        time.sleep(0.7)

    sri.click(png.mainscreen_tab_raid_selected,d_t)
    sri.click(png.mainscreen_tab_home,d_t)

def hit_raid_for_tier(tier = 1):
    pass


### stuff

def dismiss_logoff():
    sri.click(png.popup_logoff_dismiss, 2)
    sri.click(png.popup_choice_yes, 2)

